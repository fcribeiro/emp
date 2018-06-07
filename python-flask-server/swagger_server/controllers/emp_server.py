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
from swagger_server.controllers.kubernetes_controller import KubernetesController
from swagger_server import util


ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
USER_APPS = "apps:"
USER_DATA = "user:"
NAMESPACE = "user-"
rs = redis.StrictRedis(host='172.17.0.2', port=6379, db=0, decode_responses=True)
kub = KubernetesController()

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

    username = "fcribeiro"  # TODO Get username from authentication token

    user_apps = USER_APPS + username

    app = rs.hget(user_apps, app_id)
    if app is None:
        return "Application not found", 400
    app = json.loads(app)

    if app_state.state is not None:
        if app_state.state:
            state = "Running"
            if not kub.start_app(name=app["name"], stateless=app["stateless"], namespace=NAMESPACE + username):
                return "Error Starting the Application", 400
        else:
            state = "Stopped"
            if not kub.stop_app(name=app["name"], stateless=app["stateless"], namespace=NAMESPACE + username):
                return "Error Stopping the Application", 400
        app["state"] = state

    if app_state.quality_metrics is not None:
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
    key = USER_DATA + user_info.username.lower()
    if rs.hsetnx(key, "username", user_info.username.lower()):
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

    username = "fcribeiro"  # TODO Get username from authentication token

    user_apps = USER_APPS + username

    app = rs.hget(user_apps, app_id)
    if app is None:
        return "Application not found", 400
    app = json.loads(app)

    if not kub.delete_app(name=app["name"], namespace=NAMESPACE + username):
        return "Error Deleting the Application", 400
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

    user_apps = USER_APPS + username
    app_id = str(base62uuid())       # Generates a random uuid
    app = app_info.to_dict()
    app["state"] = "Deployed"
    app["name"] = app["name"].lower()
    app = json.dumps(app)
    if rs.hsetnx(user_apps, app_id, app):   # If the uuid already exists it returns zero
        kub.deploy_app(app_info=app_info, namespace=NAMESPACE + username)
        return AppInfo(id=app_id, name=app_info.name, state="Deployed")
    else:
        return "This operation could not be performed due to a duplicate uuid generated. Please try again", 400


def get_all_apps():
    """Gets general information about all applications

    :rtype: ArrayOfApps
    """

    username = "fcribeiro"  # TODO Get username from authentication token

    user_apps = USER_APPS + username

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
    user_apps = USER_APPS + username
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
    variable = False        # TODO REMOVE THIS

    if variable:   # TODO IN CASE THE APP DOES NOT EXIST
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



