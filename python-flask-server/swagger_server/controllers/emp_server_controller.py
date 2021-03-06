import connexion
import six

from swagger_server.models.app_deploy import AppDeploy  # noqa: E501
from swagger_server.models.app_info import AppInfo  # noqa: E501
from swagger_server.models.app_state import AppState  # noqa: E501
from swagger_server.models.app_total_info import AppTotalInfo  # noqa: E501
from swagger_server.models.array_of_apps import ArrayOfApps  # noqa: E501
from swagger_server.models.user_info import UserInfo  # noqa: E501
from swagger_server import util
import swagger_server.controllers.emp_server as emp


def application_change_app_state(app_id, app_state):  # noqa: E501
    """Changes an application state

     # noqa: E501

    :param app_id: ID of the application to change its state
    :type app_id: str
    :param app_state: Parameters that will change the state of the application
    :type app_state: dict | bytes

    :rtype: AppInfo
    """
    if connexion.request.is_json:
        app_state = AppState.from_dict(connexion.request.get_json())  # noqa: E501
    return emp.change_app_state(app_id=app_id, app_state=app_state)


def application_create_user(user_info):  # noqa: E501
    """Creates a user with all the necessary information

     # noqa: E501

    :param user_info: User information
    :type user_info: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        user_info = UserInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return emp.create_user(user_info=user_info)


def application_delete_app(app_id):  # noqa: E501
    """Removes an application from the platform

     # noqa: E501

    :param app_id: ID of the application to remove
    :type app_id: str

    :rtype: str
    """
    return emp.delete_app(app_id=app_id)


def application_deploy_app(app_deploy):  # noqa: E501
    """Deploys an application in the platform

     # noqa: E501

    :param app_deploy: Application object to be deployed
    :type app_deploy: dict | bytes

    :rtype: AppInfo
    """
    if connexion.request.is_json:
        app_deploy = AppDeploy.from_dict(connexion.request.get_json())  # noqa: E501
    return emp.deploy_app(app_info=app_deploy)


def application_get_all_apps():  # noqa: E501
    """Gets general information about all applications

     # noqa: E501


    :rtype: ArrayOfApps
    """
    return emp.get_all_apps()


def application_get_app(app_id):  # noqa: E501
    """Gets all information about a specific application

     # noqa: E501

    :param app_id: ID of the application to get information
    :type app_id: str

    :rtype: AppTotalInfo
    """
    return emp.get_app(app_id=app_id)


def application_get_app_tracing(app_id):  # noqa: E501
    """Gets tracing information about a specific application

     # noqa: E501

    :param app_id: ID of the application
    :type app_id: str

    :rtype: str
    """
    return emp.get_app_tracing(app_id=app_id)


def application_hello_world():  # noqa: E501
    """EMP Working!

     # noqa: E501


    :rtype: str
    """
    return emp.hello_world()


def application_login_user(user_info):  # noqa: E501
    """User login

     # noqa: E501

    :param user_info: User information
    :type user_info: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        user_info = UserInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return emp.login(user_info=user_info)


def application_scale_app(app_id, replicas):  # noqa: E501
    """Changes an application state

     # noqa: E501

    :param app_id: ID of the application to change its state
    :type app_id: str
    :param replicas: Number of Replicas
    :type replicas: int

    :rtype: str
    """
    return emp.scale_app(app_id=app_id, replicas=replicas)
