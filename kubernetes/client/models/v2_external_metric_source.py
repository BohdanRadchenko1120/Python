# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.23
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V2ExternalMetricSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'metric': 'V2MetricIdentifier',
        'target': 'V2MetricTarget'
    }

    attribute_map = {
        'metric': 'metric',
        'target': 'target'
    }

    def __init__(self, metric=None, target=None, local_vars_configuration=None):  # noqa: E501
        """V2ExternalMetricSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._metric = None
        self._target = None
        self.discriminator = None

        self.metric = metric
        self.target = target

    @property
    def metric(self):
        """Gets the metric of this V2ExternalMetricSource.  # noqa: E501


        :return: The metric of this V2ExternalMetricSource.  # noqa: E501
        :rtype: V2MetricIdentifier
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this V2ExternalMetricSource.


        :param metric: The metric of this V2ExternalMetricSource.  # noqa: E501
        :type: V2MetricIdentifier
        """
        if self.local_vars_configuration.client_side_validation and metric is None:  # noqa: E501
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def target(self):
        """Gets the target of this V2ExternalMetricSource.  # noqa: E501


        :return: The target of this V2ExternalMetricSource.  # noqa: E501
        :rtype: V2MetricTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this V2ExternalMetricSource.


        :param target: The target of this V2ExternalMetricSource.  # noqa: E501
        :type: V2MetricTarget
        """
        if self.local_vars_configuration.client_side_validation and target is None:  # noqa: E501
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, V2ExternalMetricSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2ExternalMetricSource):
            return True

        return self.to_dict() != other.to_dict()
