import connexion
import six

import swagger_server.controllers.emp_server as emp
from swagger_server.models.app_deploy import AppDeploy  # noqa: E501
from swagger_server.models.app_info import AppInfo  # noqa: E501
from swagger_server.models.app_state import AppState  # noqa: E501
from swagger_server.models.app_total_info import AppTotalInfo  # noqa: E501
from swagger_server.models.array_of_apps import ArrayOfApps  # noqa: E501
from swagger_server import util


def application_change_app_state(app_id, state):  # noqa: E501
    """Changes an application state

     # noqa: E501

    :param app_id: ID of the application to change its state
    :type app_id: int
    :param state: Parameters that will change the state of the application
    :type state: dict | bytes

    :rtype: AppTotalInfo
    """
    if connexion.request.is_json:
        state = AppState.from_dict(connexion.request.get_json())  # noqa: E501
    return emp.change_app_state(app_id=app_id, state=state)


def application_delete_app(app_id):  # noqa: E501
    """Removes an application from the platform

     # noqa: E501

    :param app_id: ID of the application to remove
    :type app_id: int

    :rtype: AppInfo
    """
    return emp.delete_app(app_id)


def application_deploy_app(deploy):  # noqa: E501
    """Deploys an application in the platform

     # noqa: E501

    :param deploy: Application object to be deployed
    :type deploy: dict | bytes

    :rtype: AppInfo
    """
    if connexion.request.is_json:
        deploy = AppDeploy.from_dict(connexion.request.get_json())  # noqa: E501
    return emp.deploy_app(deploy)


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
    :type app_id: int

    :rtype: AppTotalInfo
    """
    return emp.get_app(app_id)


def application_get_app_tracing(app_id):  # noqa: E501
    """Gets information about tracing of a specific application

     # noqa: E501

    :param app_id: ID of the application
    :type app_id: int

    :rtype: str
    """
    return emp.get_app_tracing(app_id)


def application_hello_world():  # noqa: E501
    """EMP Working!

     # noqa: E501


    :rtype: None
    """
    return emp.hello_world()
