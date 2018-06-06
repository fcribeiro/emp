class ClusterManager(object):
    def __init__(self, cluster_address):
        self.cluster_address = cluster_address

    def deploy_app(self, name):
        """Deploys an application in the platform

        :param name: Name of the application to be deployed
        :type name: str

        :rtype: AppInfo
        """
        raise NotImplementedError

    def get_app(self, name):
        raise NotImplementedError

    def start_app(self, name):
        raise NotImplementedError

    def stop_app(self, name):
        raise NotImplementedError

    def update_app_metrics(self):
        raise NotImplementedError

    def delete_app(self, name):
        raise NotImplementedError

    def get_app_tracing(self, name):
        raise NotImplementedError

    def scale_app(self, scale):
        raise NotImplementedError
