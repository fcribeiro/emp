from os import path
import yaml
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from pprint import pprint
from swagger_server.models.app_deploy import AppDeploy
from swagger_server.models.app_total_info import AppTotalInfo
from swagger_server.controllers.cluster_manager import ClusterManager
import time
import os


config.load_kube_config(config_file=os.environ['KUBECONFIG'])


def create_deployment_object(name, docker_image, envs):
    # Add Environment Variables to Pod
    kafka_address = get_kafka_ip("my-kafka", "default")
    all_envs = [client.V1EnvVar(name="KAFKAADDRESS", value=kafka_address)]
    # all_envs = [client.V1EnvVar(name="USERSADDRESS", value=KAFKAADDRESS)]
    if len(envs) != 0:
        for i in range(len(envs)):
            all_envs.append(client.V1EnvVar(name=envs[i].name, value=envs[i].value))
    # Configureate Pod template container
    container = client.V1Container(
        name=name,
        image=docker_image,
        env=all_envs,
        ports=[client.V1ContainerPort(container_port=80)])
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": name}),
        spec=client.V1PodSpec(containers=[container]))
    # Create the specification of deployment
    spec = client.ExtensionsV1beta1DeploymentSpec(
        replicas=1,
        template=template)
    # Instantiate the deployment object
    deployment = client.ExtensionsV1beta1Deployment(
        api_version="extensions/v1beta1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=name),
        spec=spec)
    return deployment


def create_service(name, namespace, app_port):
    api_instance = client.CoreV1Api()

    body = client.V1Service()  # V1Service

    # Creating Meta Data
    metadata = client.V1ObjectMeta()
    metadata.name = name

    body.metadata = metadata

    # Creating spec
    spec = client.V1ServiceSpec()
    spec.type = "LoadBalancer"

    # Creating Port object
    port = client.V1ServicePort(port=app_port, target_port=app_port)

    spec.ports = [port]
    spec.selector = {"app": name}
    body.spec = spec

    pretty = 'pretty_example'  # str | If 'true', then the output is pretty printed. (optional)
    try:
        api_response = api_instance.create_namespaced_service(namespace, body, pretty=pretty)
        # pprint(api_response)
        return True
    except ApiException as e:
        print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)
        return False


def create_namespace(namespace):
    api_instance = client.CoreV1Api()
    body = client.V1Namespace()  # V1Namespace |
    body.metadata = {"name": namespace}
    pretty = 'pretty_example'  # str | If 'true', then the output is pretty printed. (optional)

    try:
        api_response = api_instance.create_namespace(body, pretty=pretty)
        # pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->create_namespace: %s\n" % e)


def delete_namespace(namespace):
    # create an instance of the API class
    api_instance = client.CoreV1Api()
    body = client.V1DeleteOptions()  # V1DeleteOptions |
    pretty = 'pretty_example'  # str | If 'true', then the output is pretty printed. (optional)
    grace_period_seconds = 56  # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
    orphan_dependents = True  # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
    propagation_policy = 'propagation_policy_example'  # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

    try:
        api_response = api_instance.delete_namespace(namespace, body, pretty=pretty,
                                                     grace_period_seconds=grace_period_seconds,
                                                     propagation_policy=propagation_policy)
        # pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->delete_namespace: %s\n" % e)


def get_kafka_ip(name, namespace):
    api_instance = client.CoreV1Api()
    try:
        api_response = api_instance.read_namespaced_service(name, namespace)
        # pprint(api_response)
        internal_ip = api_response.spec.cluster_ip

        return internal_ip

    except ApiException as e:
        print("Exception when calling CoreV1Api->read_namespaced_service: %s\n" % e)


class KubernetesController(ClusterManager):

    def deploy_app(self, app_info, namespace=None):
        deployment = create_deployment_object(name=app_info.name, docker_image=app_info.docker_image,
                                              envs=app_info.envs)
        # Create Namespace
        create_namespace(namespace=namespace)
        # Create deployement
        api_instance = client.ExtensionsV1beta1Api()
        try:
            api_response = api_instance.create_namespaced_deployment(
                body=deployment,
                namespace=namespace,
                pretty=True)

            if create_service(name=app_info.name, namespace=namespace, app_port=app_info.port):
                return True
            else:
                return False
        except ApiException as e:
            print("Exception when calling ExtensionsV1beta1Api->create_namespaced_deployment: %s\n" % e)
            return False

    def scale_app(self, name, replicas, namespace=None):
        api_instance = client.ExtensionsV1beta1Api()
        deployment = self.get_app(name, namespace=namespace)
        deployment.spec.replicas = replicas
        # Update the deployment
        try:
            api_response = api_instance.patch_namespaced_deployment(
                name=name,
                namespace=namespace,
                body=deployment)
            # print(api_response.status)
            # print("Deployment updated. status='%s'" % str(api_response.status))
            return True
        except ApiException as e:
            print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_deployment: %s\n" % e)
            return False

    def delete_app(self, name, namespace=None):
        api_instance = client.ExtensionsV1beta1Api()
        # Delete deployment
        try:
            api_response = api_instance.delete_namespaced_deployment(
                name=name,
                namespace=namespace,
                body=client.V1DeleteOptions(
                    propagation_policy='Foreground',
                    grace_period_seconds=5))

            # Delete Service
            api_instance = client.CoreV1Api()
            body = client.V1DeleteOptions()  # V1DeleteOptions |
            pretty = 'pretty_example'  # str | If 'true', then the output is pretty printed. (optional)
            grace_period_seconds = 56  # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
            orphan_dependents = True  # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
            propagation_policy = 'propagation_policy_example'
            try:
                api_response = api_instance.delete_namespaced_service(name, namespace, body, pretty=pretty,
                                                                      grace_period_seconds=grace_period_seconds,
                                                                      orphan_dependents=orphan_dependents,
                                                                      propagation_policy=propagation_policy)
                return True
            except ApiException as e:
                print("Exception when calling CoreV1Api->delete_namespaced_service: %s\n" % e)
                return False
        except ApiException as e:
            print("Exception when calling ExtensionsV1beta1Api->delete_namespaced_deployment: %s\n" % e)
            return False

    def stop_app(self, name, stateless, namespace=None):
        # api_instance = client.ExtensionsV1beta1Api()
        if stateless:           # If true, the application is stateless
            if self.scale_app(name=name, replicas=0, namespace=namespace):
                return True
            else:
                return False
        else:                   # TODO It is also necessary to delete the volume
            if self.scale_app(name=name, replicas=0, namespace=namespace):
                return True
            else:
                return False

    def start_app(self, name, stateless, namespace=None):
        # api_instance = client.ExtensionsV1beta1Api()
        if stateless:  # If true, the application is stateless
            if self.scale_app(name=name, replicas=1, namespace=namespace):
                return True
            else:
                return False
        else:  # TODO It is also necessary to start the volume
            if self.scale_app(name=name, replicas=1, namespace=namespace):
                return True
            else:
                return False

    def get_app(self, name, namespace=None):
        api_instance = client.ExtensionsV1beta1Api()
        try:
            api_response = api_instance.read_namespaced_deployment(name, namespace, pretty=True, exact=True, export=True)
            pprint(api_response)
            return api_response         # TODO Decide what to return
        except ApiException as e:
            print("Exception when calling ExtensionsV1beta1Api->read_namespaced_deployment: %s\n" % e)
            return None

    @staticmethod
    def get_ip(name, namespace):
        api_instance = client.ExtensionsV1beta1Api()
        try:
            api_response = api_instance.read_namespaced_deployment(name, namespace, pretty=True, exact=True, export=True)
            # pprint(api_response)
            replicas = api_response.spec.replicas
        except ApiException as e:
            print("Exception when calling ExtensionsV1beta1Api->read_namespaced_deployment: %s\n" % e)
            return None

        api_instance = client.CoreV1Api()
        try:
            api_response = api_instance.read_namespaced_service(name, namespace)
            # pprint(api_response)
            # internal_ip = api_response.spec.cluster_ip

            if api_response.status.load_balancer.ingress is None:
                external_ip = "Not Ready Yet"
            else:
                external_ip = api_response.status.load_balancer.ingress[0].ip

            app_info = AppTotalInfo(name=name, external_ip=external_ip, replicas=replicas,
                                    state=None)
            print(app_info)
            return app_info

        except ApiException as e:
            print("Exception when calling CoreV1Api->read_namespaced_service: %s\n" % e)

    @staticmethod
    def get_app_tracing_ip(name, namespace):
        api_instance = client.CoreV1Api()
        try:
            api_response = api_instance.read_namespaced_service(name, namespace)

            if api_response.status.load_balancer.ingress is None:
                external_ip = None
            else:
                external_ip = api_response.status.load_balancer.ingress[0].ip

            return external_ip

        except ApiException as e:
            print("Exception when calling CoreV1Api->read_namespaced_service: %s\n" % e)


def main():
    namespace = "user-fcribeiro"
    name = "songs-ms"
    kub = KubernetesController()
    kub.scale_app(name=name, replicas=20, namespace=namespace)


if __name__ == '__main__':
    main()
