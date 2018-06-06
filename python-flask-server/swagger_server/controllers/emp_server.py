import json
import redis
import uuid
import hashlib
import baseconv
import jsonpickle

from swagger_server.models.app_deploy import AppDeploy
from swagger_server.models.app_info import AppInfo
from swagger_server.models.app_state import AppState
from swagger_server.models.user_info import UserInfo
from swagger_server.models.quality_metrics import QualityMetrics
from swagger_server.models.app_total_info import AppTotalInfo
from swagger_server.models.array_of_apps import ArrayOfApps
from swagger_server import util


ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
USER_APPS = "apps:"
USER_DATA = "user:"
rs = redis.StrictRedis(host='172.17.0.2', port=6379, db=0, decode_responses=True)


# while True:
#     try:
#         resp = rs.ping()
#         if resp == "PONG":
#             print("DEU")
#             break
#     except Exception as ex:
#         print("Could not connect to Redis")


def base62uuid():
    converter = baseconv.BaseConverter(ALPHABET)
    uuid4_as_hex = str(uuid.uuid4()).replace('-', '')
    uuid4_as_int = int(uuid4_as_hex, 16)
    return converter.encode(uuid4_as_int)


def change_app_state(app_id, app_state):
    """Changes an application state

    :param app_id: ID of the application to change its state
    :type app_id: str
    :param app_state: Parameters that will change the state of the application
    :type app_state: dict | bytes

    :rtype: AppTotalInfo
    """

    # TODO Update redis state

    # app = cluster.get_app(app_id)
    # if app is None:
    #     return
    #
    # if cluster.change_app_state(app_id=app_id, state=app_state):
    #     app_info = cluster.get_app(app_id)
    #     return app_info
    #
    # else:
    #     return

    username = "fcribeiro"  # TODO Get username from authentication token

    user_apps = "apps:" + username

    app = rs.hget(user_apps, app_id)
    if app is None:
        return "Application not found", 400
    app = json.loads(app)

    if app_state.state is not None:
        if app_state.state:     # TODO Start application in kubernetes
            state = "Running"
        else:
            state = "Stopped"   # TODO Stop application in kubernetes
        app["state"] = state

    if app_state.quality_metrics is not None:       # TODO Change quality metrics in kubernetes application
        qm = app_state.to_dict()
        app["quality_metrics"] = qm["quality_metrics"]

    app_update = json.dumps(app)
    rs.hset(user_apps, app_id, app_update)
    return AppTotalInfo(id=app_id, name=app["name"], state=app["state"], docker_image=app["docker_image"],
                        stateless=app["stateless"], quality_metrics=app["quality_metrics"])


def create_user(user_info):
    """Creates a user with all the necessary information

    :param user_info: User information
    :type user_info: dict | bytes

    :rtype: str
    """
    key = USER_DATA + user_info.username
    if rs.hsetnx(key, "username", user_info.username):
        rs.hset(key, "password", user_info.password)
    else:
        return "Username already exists"

    return "Account created successfully"


def delete_app(app_id):     # TODO CHECK IF EXISTS
    """Removes an application from the platform

    :param app_id: ID of the application to remove
    :type app_id: str

    :rtype: str
    """

    # app = cluster.get_app_general_info(app_id)
    # if app is None:
    #     return
    # if cluster.delete_app(app_id):
    #     app.state = "Deleted"
    # else:
    #     return

    # TODO Delete in Redis?
    username = "fcribeiro"
    user_apps = USER_APPS + username
    if rs.hdel(user_apps, app_id):
        return "Application Deleted Successfully"
    else:
        return "Application not found", 400


def deploy_app(app_info):
    """Deploys an application in the platform

    :param app_info: Application object to be deployed
    :type app_info: dict | bytes

    :rtype: AppInfo
    """

    username = "fcribeiro"          # TODO Get username from authentication token

    user_apps = "apps:" + username
    app_id = str(base62uuid())       # Generates a random uuid
    app = app_info.to_dict()
    app["state"] = "Deployed"
    app = json.dumps(app)
    if rs.hsetnx(user_apps, app_id, app):   # If the uuid already exists it returns zero
        # TODO Deploy on Kubernetes
        return AppInfo(id=app_id, name=app_info.name, state="Deployed")
    else:
        return "This operation could not be performed due to a duplicate uuid generated. Please try again", 400


def get_all_apps():
    """Gets general information about all applications

    :rtype: ArrayOfApps
    """

    username = "fcribeiro"  # TODO Get username from authentication token

    user_apps = "apps:" + username

    apps = rs.hgetall(user_apps)
    for key in apps:
        apps[key] = json.loads(apps[key])
    return apps


def get_app(app_id):
    """Gets all information about a specific application

    :param app_id: ID of the application to get information
    :type app_id: str

    :rtype: AppTotalInfo
    """

    username = "fcribeiro"    # TODO Get username from authentication token
    # TODO GET STATE
    user_apps = "apps:" + username
    resp = rs.hget(user_apps, app_id)
    if resp is None:            # TODO App Not Found
        return "Application not found", 400
    app = json.loads(resp)

    return AppTotalInfo(id=app_id, name=app["name"], state=app["state"], docker_image=app["docker_image"],
                        stateless=app["stateless"], quality_metrics=app["quality_metrics"])


def get_app_tracing(app_id):
    """Gets information about tracing of a specific application

    :param app_id: ID of the application
    :type app_id: str

    :rtype: str
    """
    # TODO Get the applications tracing link
    app_link = "http://localhost:8080"

    if False:   # TODO IN CASE THE APP DOES NOT EXIST
        return "Application not found", 400

    return app_link


def hello_world():
    """EMP Working!

    :rtype: str
    """

    return "EMP WORKING!"


def login(user_info):
    """User login

    :param user_info: User information
    :type user_info: dict | bytes

    :rtype: str
    """
    key = "user:" + user_info.username
    result = rs.hgetall(key)
    if not result:  # Checks if dictionary is empty, meaning that no user with that username was found
        return "Login failed"
    return "Login successful"



