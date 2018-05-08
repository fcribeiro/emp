import json
import redis
import uuid
import swagger_server.controllers.cluster_manager as cluster
from swagger_server.models.app_deploy import AppDeploy  # noqa: E501
from swagger_server.models.app_info import AppInfo  # noqa: E501
from swagger_server.models.app_state import AppState  # noqa: E501
from swagger_server.models.user_info import UserInfo
from swagger_server.models.app_total_info import AppTotalInfo  # noqa: E501
from swagger_server.models.array_of_apps import ArrayOfApps  # noqa: E501
from swagger_server import util


redis = redis.StrictRedis(host='172.17.0.2', port=6379, db=0, decode_responses=True)


def change_app_state(app_id, app_state):
    """Changes an application state

    :param app_id: ID of the application to change its state
    :type app_id: int
    :param app_state: Parameters that will change the state of the application
    :type app_state: dict | bytes

    :rtype: AppTotalInfo
    """

    # TODO Update redis state

    app = cluster.get_app(app_id)
    if app is None:
        return

    if cluster.change_app_state(app_id=app_id, state=app_state):
        app_info = cluster.get_app(app_id)
        return app_info

    else:
        return


def create_user(user_info):
    """Creates a user with all the necessary information

    :param user_info: User information
    :type user_info: dict | bytes

    :rtype: str
    """

    return 'User Created'


def delete_app(app_id):
    """Removes an application from the platform

    :param app_id: ID of the application to remove
    :type app_id: int

    :rtype: AppInfo
    """

    app = cluster.get_app_general_info(app_id)
    if app is None:
        return
    if cluster.delete_app(app_id):
        app.state = "Deleted"
    else:
        return

    # TODO Decide what to return when an application is deleted successfully
    # TODO Delete in Redis?

    return app


def deploy_app(app_info):
    """Deploys an application in the platform

    :param app_info: Application object to be deployed
    :type app_info: dict | bytes

    :rtype: AppInfo
    """

    # TODO Store in redis

    app = 'app_%s' % app_info
    redis.set(app, app_info)
    # r.execute_command()
    value = redis.get('app')
    test = value(AppDeploy)
    print(test)

    app_id = cluster.deploy_app(app_info)
    if app_id is None:
        return

    app_info = cluster.get_app_general_info(app_id)
    return app_info


def get_all_apps():
    """Gets general information about all applications

    :rtype: ArrayOfApps
    """
    return 'All Apps Listed Here'


def get_app(app_id):
    """Gets all information about a specific application

    :param app_id: ID of the application to get information
    :type app_id: int

    :rtype: AppTotalInfo
    """
    app_info = cluster.get_app(app_id)
    if app_info is None:
        return
    return app_info


def get_app_tracing(app_id):
    """Gets information about tracing of a specific application

    :param app_id: ID of the application
    :type app_id: int

    :rtype: str
    """
    app_link = cluster.get_app_tracing(app_id)

    return app_link


def hello_world():
    """EMP Working!

    :rtype: str
    """

    # print(str(value, 'utf-8'))

    return "EMP WORKING!"


def login(user_id, user_info):
    """User login

    :param user_id: ID of the user to login
    :type user_id: int
    :param user_info: User information
    :type user_info: dict | bytes

    :rtype: str
    """

    return "Login"



