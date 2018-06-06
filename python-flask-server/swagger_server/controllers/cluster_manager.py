class ClusterManager(object):

    def deploy_app(self, app_info):
        """Deploys an application in the platform

        :param app_info: Application object to be deployed
        :type app_info: dict | bytes

        :return: True if the deployment was successful, False otherwise
        :rtype: bool
        """
        raise NotImplementedError

    def get_app(self, name):        # TODO Return type doc
        """Gets all information about a specific application in the platform

        :param name: Name of the application to get information
        :type name: str

        :return: Application information in a       # TODO Return type doc
        :rtype: AppTotalInfo
        """
        raise NotImplementedError

    def start_app(self, name, stateless):
        """Starts an application in the platform

        :param name: Name of the application to Start
        :type name: str
        :param stateless: True if the application is stateless, False otherwise
        :type stateless: bool

        :return: True if the application was started successfully, False otherwise.
        :rtype: bool
        """
        raise NotImplementedError

    def stop_app(self, name, stateless):
        """Stops an application from running in the platform

        :param name: Name of the application to Stop
        :type name: str
        :param stateless: True if the application is stateless, False otherwise
        :type stateless: bool

        :return: True if the application was stopped successfully, False otherwise.
        :rtype: bool
        """
        raise NotImplementedError

    def delete_app(self, name):
        """Deletes an application from the platform

        :param name: Name of the application to be deleted
        :type name: str

        :return: True if the application was deleted successfully, False otherwise
        :rtype: bool
        """
        raise NotImplementedError

    def scale_app(self, name, replicas):
        """Scales an application in the platform

        :param name: Name of the application to Scale
        :type name: str
        :param replicas: Number of replicas of the application that must be running in the platform.
        :type replicas: int

        :return: True if the application was scaled successfully, False otherwise
        :rtype: bool
        """
        raise NotImplementedError
