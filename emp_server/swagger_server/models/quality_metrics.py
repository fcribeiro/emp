# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class QualityMetrics(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metric: str=None, value: str=None):  # noqa: E501
        """QualityMetrics - a model defined in Swagger

        :param metric: The metric of this QualityMetrics.  # noqa: E501
        :type metric: str
        :param value: The value of this QualityMetrics.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'metric': str,
            'value': str
        }

        self.attribute_map = {
            'metric': 'metric',
            'value': 'value'
        }

        self._metric = metric
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'QualityMetrics':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QualityMetrics of this QualityMetrics.  # noqa: E501
        :rtype: QualityMetrics
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metric(self) -> str:
        """Gets the metric of this QualityMetrics.


        :return: The metric of this QualityMetrics.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric: str):
        """Sets the metric of this QualityMetrics.


        :param metric: The metric of this QualityMetrics.
        :type metric: str
        """

        self._metric = metric

    @property
    def value(self) -> str:
        """Gets the value of this QualityMetrics.


        :return: The value of this QualityMetrics.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this QualityMetrics.


        :param value: The value of this QualityMetrics.
        :type value: str
        """

        self._value = value