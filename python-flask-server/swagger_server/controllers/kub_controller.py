import json


def change_app_state(app_id, state):  
    """Changes an application state

    :param app_id: ID of the application to change its state
    :type app_id: int
    :param state: Parameters that will change the state of the application
    :type state: dict | bytes

    :rtype: AppInfo
    """
    return ''


def delete_app(app_id):  
    """Removes an application from the platform

    :param app_id: ID of the application to remove
    :type app_id: int

    :rtype: AppInfo
    """
    payload = {"id": app_id, "name": "Songs Application", "state": "Stopped"}
    payload = json.dumps(payload)
    return json.loads(payload)


def deploy_app(deploy):  
    """Deploys an application in the platform

    :param deploy: Application object to be deployed
    :type deploy: dict | bytes

    :rtype: AppTotalInfo
    """
    return ''


def get_all_apps():  
    """Gets general information about all applications

    :rtype: ArrayOfApps
    """
    return 'apps list'


def get_app(app_id):  
    """Gets all information about a specific application

    :param app_id: ID of the application to get information
    :type app_id: int

    :rtype: AppTotalInfo
    """
    return ''


def get_app_tracing(app_id):  
    """Gets information about tracing of a specific application

    :param app_id: ID of the application
    :type app_id: int

    :rtype: str
    """
    return 'http://localhost:8080'


def hello_world():  
    """EMP Working!

    :rtype: None
    """
    return 'EMP WORKING!'
