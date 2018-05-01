import json
import swagger_server.controllers.kubernetes_controller as kubernetes

from swagger_server.models.app_deploy import AppDeploy
from swagger_server.models.app_info import AppInfo
from swagger_server.models.app_state import AppState
from swagger_server.models.quality_metrics import QualityMetrics
from swagger_server.models.app_total_info import AppTotalInfo
from swagger_server.models.array_of_apps import ArrayOfApps
from swagger_server import util


def change_app_state(app_id, state):
    """Changes an application state

    :param app_id: ID of the application to change its state
    :type app_id: int
    :param state: Parameters that will change the state of the application
    :type state: dict | bytes

    :rtype: boolean
    """

    # TODO Change application state using kubernetes_controller (return true is successful or false otherwise)

    return True


def delete_app(app_id):
    """Removes an application from the platform

    :param app_id: ID of the application to remove
    :type app_id: int

    :rtype: boolean
    """

    # TODO Delete application using kubernetes_controller (return true is successful or false otherwise)

    return True


def deploy_app(deploy):
    """Deploys an application in the platform

    :param deploy: Application object to be deployed
    :type deploy: dict | bytes

    :rtype: boolean
    """

    # TODO Call all kubernetes_controller functions to deploy a new application
    # TODO (return application ID)

    app_id = 10

    return app_id


def get_all_apps():
    """Gets general information about all applications

    :rtype: ArrayOfApps
    """

    # TODO Decide how to implement this because some kind of user ID is necessary

    return 'All Apps Listed Here'


def get_app(app_id):
    """Gets all information about a specific application

    :param app_id: ID of the application to get information
    :type app_id: int

    :rtype: AppTotalInfo
    """

    # TODO Call kubernetes_controller function to return all the information about a specific application

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
    :type app_id: int

    :rtype: str
    """

    # TODO Request for the specific application tracing link

    app_link = 'http://localhost:8080'

    return app_link


def hello_world():
    """EMP Working!

    :rtype: None
    """
    return 'EMP WORKING!'
