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


class QualityMetrics(object):
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
        'metric': 'str',
        'values': 'str'
    }

    attribute_map = {
        'metric': 'metric',
        'values': 'values'
    }

    def __init__(self, metric=None, values=None):  # noqa: E501
        """QualityMetrics - a model defined in Swagger"""  # noqa: E501

        self._metric = None
        self._values = None
        self.discriminator = None

        self.metric = metric
        self.values = values

    @property
    def metric(self):
        """Gets the metric of this QualityMetrics.  # noqa: E501

        Name of the quality metric  # noqa: E501

        :return: The metric of this QualityMetrics.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this QualityMetrics.

        Name of the quality metric  # noqa: E501

        :param metric: The metric of this QualityMetrics.  # noqa: E501
        :type: str
        """
        if metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def values(self):
        """Gets the values of this QualityMetrics.  # noqa: E501

        Values of the quality metric  # noqa: E501

        :return: The values of this QualityMetrics.  # noqa: E501
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this QualityMetrics.

        Values of the quality metric  # noqa: E501

        :param values: The values of this QualityMetrics.  # noqa: E501
        :type: str
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

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
        if not isinstance(other, QualityMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
