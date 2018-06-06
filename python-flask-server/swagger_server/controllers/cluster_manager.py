class ClusterManager(object):

    def deploy_app(self, app_info):
        raise NotImplementedError

    def get_app(self, name):
        raise NotImplementedError

    def start_app(self, name, stateless):
        raise NotImplementedError

    def stop_app(self, name, stateless):
        raise NotImplementedError

    def delete_app(self, name):
        raise NotImplementedError

    def scale_app(self, name, replicas):
        raise NotImplementedError
