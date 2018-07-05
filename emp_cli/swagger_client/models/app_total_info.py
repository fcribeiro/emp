# coding: utf-8

"""
    EMP_Server_Controller

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.environment_variables import EnvironmentVariables  # noqa: F401,E501
from swagger_client.models.quality_metrics import QualityMetrics  # noqa: F401,E501


class AppTotalInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'state': 'str',
        'docker_image': 'str',
        'envs': 'list[EnvironmentVariables]',
        'stateless': 'bool',
        'quality_metrics': 'list[QualityMetrics]',
        'port': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'docker_image': 'docker_image',
        'envs': 'envs',
        'stateless': 'stateless',
        'quality_metrics': 'quality_metrics',
        'port': 'port'
    }

    def __init__(self, id=None, name=None, state=None, docker_image=None, envs=None, stateless=None, quality_metrics=None, port=None):  # noqa: E501
        """AppTotalInfo - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._state = None
        self._docker_image = None
        self._envs = None
        self._stateless = None
        self._quality_metrics = None
        self._port = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.state = state
        self.docker_image = docker_image
        self.envs = envs
        self.stateless = stateless
        self.quality_metrics = quality_metrics
        self.port = port

    @property
    def id(self):
        """Gets the id of this AppTotalInfo.  # noqa: E501

        The application ID.  # noqa: E501

        :return: The id of this AppTotalInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppTotalInfo.

        The application ID.  # noqa: E501

        :param id: The id of this AppTotalInfo.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this AppTotalInfo.  # noqa: E501

        Name of the deployed application  # noqa: E501

        :return: The name of this AppTotalInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppTotalInfo.

        Name of the deployed application  # noqa: E501

        :param name: The name of this AppTotalInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def state(self):
        """Gets the state of this AppTotalInfo.  # noqa: E501

        Current state of the application  # noqa: E501

        :return: The state of this AppTotalInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AppTotalInfo.

        Current state of the application  # noqa: E501

        :param state: The state of this AppTotalInfo.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def docker_image(self):
        """Gets the docker_image of this AppTotalInfo.  # noqa: E501

        Name of the docker image  # noqa: E501

        :return: The docker_image of this AppTotalInfo.  # noqa: E501
        :rtype: str
        """
        return self._docker_image

    @docker_image.setter
    def docker_image(self, docker_image):
        """Sets the docker_image of this AppTotalInfo.

        Name of the docker image  # noqa: E501

        :param docker_image: The docker_image of this AppTotalInfo.  # noqa: E501
        :type: str
        """
        if docker_image is None:
            raise ValueError("Invalid value for `docker_image`, must not be `None`")  # noqa: E501

        self._docker_image = docker_image

    @property
    def envs(self):
        """Gets the envs of this AppTotalInfo.  # noqa: E501


        :return: The envs of this AppTotalInfo.  # noqa: E501
        :rtype: list[EnvironmentVariables]
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this AppTotalInfo.


        :param envs: The envs of this AppTotalInfo.  # noqa: E501
        :type: list[EnvironmentVariables]
        """
        if envs is None:
            raise ValueError("Invalid value for `envs`, must not be `None`")  # noqa: E501

        self._envs = envs

    @property
    def stateless(self):
        """Gets the stateless of this AppTotalInfo.  # noqa: E501

        Stateless apps use true, stateful use false.  # noqa: E501

        :return: The stateless of this AppTotalInfo.  # noqa: E501
        :rtype: bool
        """
        return self._stateless

    @stateless.setter
    def stateless(self, stateless):
        """Sets the stateless of this AppTotalInfo.

        Stateless apps use true, stateful use false.  # noqa: E501

        :param stateless: The stateless of this AppTotalInfo.  # noqa: E501
        :type: bool
        """
        if stateless is None:
            raise ValueError("Invalid value for `stateless`, must not be `None`")  # noqa: E501

        self._stateless = stateless

    @property
    def quality_metrics(self):
        """Gets the quality_metrics of this AppTotalInfo.  # noqa: E501


        :return: The quality_metrics of this AppTotalInfo.  # noqa: E501
        :rtype: list[QualityMetrics]
        """
        return self._quality_metrics

    @quality_metrics.setter
    def quality_metrics(self, quality_metrics):
        """Sets the quality_metrics of this AppTotalInfo.


        :param quality_metrics: The quality_metrics of this AppTotalInfo.  # noqa: E501
        :type: list[QualityMetrics]
        """
        if quality_metrics is None:
            raise ValueError("Invalid value for `quality_metrics`, must not be `None`")  # noqa: E501

        self._quality_metrics = quality_metrics

    @property
    def port(self):
        """Gets the port of this AppTotalInfo.  # noqa: E501

        Port number of the application  # noqa: E501

        :return: The port of this AppTotalInfo.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AppTotalInfo.

        Port number of the application  # noqa: E501

        :param port: The port of this AppTotalInfo.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AppTotalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
