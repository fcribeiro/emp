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

    name = 'Songs Aplication'
    docker_image = 'fcribeiro/Songs_MS'
    stateless = True
    state = 'Running'
    quality_metrics = []
    qm = QualityMetrics(metric="metric", values="val")
    quality_metrics.append(qm)

    return AppTotalInfo(id=app_id, name=name, state=state, docker_image=docker_image, stateless=stateless,
                        quality_metrics=quality_metrics)


def create_user(user_info):
    """Creates a user with all the necessary information

    :param user_info: User information
    :type user_info: dict | bytes

    :rtype: str
    """
    name = "user:"+user_info.username
    if rs.hsetnx(name, "username", user_info.username):
        rs.hset(name, "password", user_info.password)

    return "User Created"


def delete_app(app_id):
    """Removes an application from the platform

    :param app_id: ID of the application to remove
    :type app_id: str

    :rtype: AppInfo
    """

    # app = cluster.get_app_general_info(app_id)
    # if app is None:
    #     return
    # if cluster.delete_app(app_id):
    #     app.state = "Deleted"
    # else:
    #     return

    # ****************************************************************************************** #
    name = 'Songs Aplication'
    state = 'Deleted'

    app = AppInfo(id=app_id, name=name, state=state)
    # ****************************************************************************************** #
    # TODO Decide what to return when an application is deleted successfully
    # TODO Delete in Redis?
    username = "fabio"
    user_apps = "apps:" + username
    rs.srem(user_apps, app_id)
    app = "appdata:" + app_id
    rs.delete(app)

    return app


def deploy_app(app_info):
    """Deploys an application in the platform

    :param app_info: Application object to be deployed
    :type app_info: dict | bytes

    :rtype: AppInfo
    """

    username = "ribeiro"          # TODO Get username from authentication token

    user_apps = "apps:" + username
    app_id = str(base62uuid())       # Generates a random uuid
    print(app_id)

    # app = {}
    # app["name"] = app_info.name
    # app["docker_image"] = app_info.docker_image
    # app["stateless"] = app_info.stateless
    # app["quality_metrics"] = app_info.quality_metrics
    print(app_info.__dict__)
    frozen = jsonpickle.encode(app_info.__dict__)
    # print(frozen)
    # app = json.dumps(app_info.__dict__)

    # rs.hset(user_apps, app_id, app)

    # ****************************************************************************************** #

    name = 'Songs Aplication'
    state = 'Running'

    return AppInfo(id=app_id, name=name, state=state)        # TODO Change ID to string



def get_all_apps():
    """Gets general information about all applications

    :rtype: ArrayOfApps
    """
    return 'All Apps Listed Here'


def get_app(app_id):
    """Gets all information about a specific application

    :param app_id: ID of the application to get information
    :type app_id: str

    :rtype: AppTotalInfo
    """

    username = "ribeiro"  # TODO Get username from authentication token
    # TODO str = str.replace("\'", "\"")

    user_apps = "apps:" + username
    resp = rs.hget(user_apps, app_id)
    print(resp)
    resp = json.loads(resp)
    #
    # print(resp['name'])

    name = 'Songs Aplication'
    docker_image = 'fcribeiro/Songs_MS'
    stateless = True
    state = 'Running'
    quality_metrics = []
    qm = QualityMetrics(metric="metric", values="val")
    quality_metrics.append(qm)

    return AppTotalInfo(id=app_id, name=name, state=state, docker_image=docker_image, stateless=stateless,
                        quality_metrics=quality_metrics)


def get_app_tracing(app_id):
    """Gets information about tracing of a specific application

    :param app_id: ID of the application
    :type app_id: str

    :rtype: str
    """
    app_link = "http://localhost:8080"

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
    result = redis.hgetall(key)
    print(result)
    if not result:  # Checks if dictionary is empty, meaning that no user with that username was found
        return "No user found with that username"

    print(result['username'])
    print(result['password'])
    return "User %s logged in successfully" % (result['username'])



