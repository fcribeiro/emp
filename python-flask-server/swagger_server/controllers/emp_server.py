import json
import redis
import swagger_server.controllers.cluster_manager as cluster
from swagger_server.models.app_deploy import AppDeploy  # noqa: E501
from swagger_server.models.app_info import AppInfo  # noqa: E501
from swagger_server.models.app_state import AppState  # noqa: E501
from swagger_server.models.app_total_info import AppTotalInfo  # noqa: E501
from swagger_server.models.array_of_apps import ArrayOfApps  # noqa: E501
from swagger_server import util


def change_app_state(app_id, state):
    """Changes an application state

    :param app_id: ID of the application to change its state
    :type app_id: int
    :param state: Parameters that will change the state of the application
    :type state: dict | bytes

    :rtype: AppTotalInfo
    """

    # TODO Update redis state

    app = cluster.get_app(app_id)
    if app is None:
        return

    if cluster.change_app_state(app_id=app_id, state=state):
        app_info = cluster.get_app(app_id)
        return app_info

    else:
        return


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


def deploy_app(deploy):
    """Deploys an application in the platform

    :param deploy: Application object to be deployed
    :type deploy: dict | bytes

    :rtype: AppTotalInfo
    """

    app_id = cluster.deploy_app(deploy)
    if app_id is None:
        return

    # TODO Store in redis

    r = redis.StrictRedis(host='172.17.0.2', port=6379, db=0)
    app = 'app_%s' % app_id
    r.set(app, deploy)
    # r.execute_command()
    value = r.get('app')
    test = value(AppDeploy)
    print(test)

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

    :rtype: None
    """
    return 'EMP WORKING!'
