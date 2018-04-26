import connexion
import six

from swagger_server.models.app_deploy import AppDeploy  # noqa: E501
from swagger_server.models.app_info import AppInfo  # noqa: E501
from swagger_server.models.app_total_info import AppTotalInfo  # noqa: E501
from swagger_server.models.array_of_apps import ArrayOfApps  # noqa: E501
from swagger_server import util


def application_delete_app(appID):  # noqa: E501
    """Removes an application from the platform

     # noqa: E501

    :param appID: ID of the application to remove
    :type appID: int

    :rtype: AppInfo
    """
    return 'do some magic!'


def application_deploy_app(body):  # noqa: E501
    """Deploy App

     # noqa: E501

    :param body: Application object to be deployed
    :type body: dict | bytes

    :rtype: AppTotalInfo
    """
    if connexion.request.is_json:
        body = AppDeploy.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def application_get_all_apps():  # noqa: E501
    """Gets information about all applications

     # noqa: E501


    :rtype: ArrayOfApps
    """
    return 'do some magic!'


def application_get_app(appID):  # noqa: E501
    """Gets information about a specific application

     # noqa: E501

    :param appID: ID of the application to get information
    :type appID: int

    :rtype: AppTotalInfo
    """
    return 'do some magic!'


def application_get_app_tracing(appID):  # noqa: E501
    """Gets information about tracing of a specific application

     # noqa: E501

    :param appID: ID of the application
    :type appID: int

    :rtype: str
    """
    return 'do some magic!'


def application_hello_world():  # noqa: E501
    """Hello World!

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def application_stop_app(appID):  # noqa: E501
    """Stop an application

     # noqa: E501

    :param appID: ID of the application to stop
    :type appID: int

    :rtype: AppInfo
    """
    return 'do some magic!'
