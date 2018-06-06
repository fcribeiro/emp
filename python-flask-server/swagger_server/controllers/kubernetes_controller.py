from os import path
import yaml
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from pprint import pprint
import time


config.load_kube_config(config_file="/home/fabio/Desktop/Projects/emp/python-flask-server/kube-config")
NAMESPACE = "default"


def create_deployment_object(name, deployment_name, docker_image):
    # Configureate Pod template container
    container = client.V1Container(
        name=name,
        image=docker_image,
        ports=[client.V1ContainerPort(container_port=80)])
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": name}),
        spec=client.V1PodSpec(containers=[container]))
    # Create the specification of deployment
    # client.V1EnvVar
    spec = client.ExtensionsV1beta1DeploymentSpec(
        replicas=1,
        template=template)
    # Instantiate the deployment object
    deployment = client.ExtensionsV1beta1Deployment(
        api_version="extensions/v1beta1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=deployment_name),
        spec=spec)

    return deployment


def deploy_app(deployment):
    # Create deployement
    api_instance = client.ExtensionsV1beta1Api()
    try:
        api_response = api_instance.create_namespaced_deployment(
            body=deployment,
            namespace=NAMESPACE,
            pretty=True)
        # pprint(api_response)
        print("Deployment created. status='%s'" % str(api_response.status))
    except ApiException as e:
        print("Exception when calling ExtensionsV1beta1Api->create_namespaced_deployment: %s\n" % e)


def scale_app(name, scale):
    api_instance = client.ExtensionsV1beta1Api()
    deployment = get_app(name)
    if scale:   # If true, the app needs to scale up
        deployment.spec.replicas = deployment.spec.replicas + 1
    else:       # If false, the app needs to scale down
        if deployment.spec.replicas > 1:
            deployment.spec.replicas = deployment.spec.replicas - 1

    # Update the deployment
    try:
        api_response = api_instance.patch_namespaced_deployment(
            name=name,
            namespace=NAMESPACE,
            body=deployment)
        # print(api_response.status)
        print("Deployment updated. status='%s'" % str(api_response.status))
        return True
    except ApiException as e:
        print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_deployment: %s\n" % e)
        return False


def delete_app(name):
    api_instance = client.ExtensionsV1beta1Api()
    # Delete deployment
    try:
        api_response = api_instance.delete_namespaced_deployment(
            name=name,
            namespace=NAMESPACE,
            body=client.V1DeleteOptions(
                propagation_policy='Foreground',
                grace_period_seconds=5))
        # pprint(api_response)
        print("Deployment deleted. status='%s'" % str(api_response.status))
        return True
    except ApiException as e:
        print("Exception when calling ExtensionsV1beta1Api->delete_namespaced_deployment: %s\n" % e)
        return False


def get_app(name):
    api_instance = client.ExtensionsV1beta1Api()
    try:
        api_response = api_instance.read_namespaced_deployment(name, NAMESPACE, pretty=True, exact=True, export=True)
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling ExtensionsV1beta1Api->read_namespaced_deployment: %s\n" % e)
        return None


# def delete_pod(name):
#     api_instance = client.CoreV1Api()
#     body = client.V1DeleteOptions()
#     api_response = api_instance.delete_namespaced_pod(name, NAMESPACE, body)
#     return api_response


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.

    # Create a deployment object with client-python API. The deployment we
    # created is same as the `nginx-deployment.yaml` in the /examples folder.

    app_name = "nginx"
    deployment_name = "nginx-deployment"
    docker_image = "nginx:1.7.9"

    deployment = create_deployment_object(name=app_name, deployment_name=deployment_name, docker_image=docker_image)

    deploy_app(deployment=deployment)

    # scale_app(name=deployment_name, scale=True)

    # delete_app(name=deployment_name)


if __name__ == '__main__':
    main()
