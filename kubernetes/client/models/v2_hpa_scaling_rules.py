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


class V2HPAScalingRules(object):
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
        'policies': 'list[V2HPAScalingPolicy]',
        'select_policy': 'str',
        'stabilization_window_seconds': 'int'
    }

    attribute_map = {
        'policies': 'policies',
        'select_policy': 'selectPolicy',
        'stabilization_window_seconds': 'stabilizationWindowSeconds'
    }

    def __init__(self, policies=None, select_policy=None, stabilization_window_seconds=None, local_vars_configuration=None):  # noqa: E501
        """V2HPAScalingRules - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._policies = None
        self._select_policy = None
        self._stabilization_window_seconds = None
        self.discriminator = None

        if policies is not None:
            self.policies = policies
        if select_policy is not None:
            self.select_policy = select_policy
        if stabilization_window_seconds is not None:
            self.stabilization_window_seconds = stabilization_window_seconds

    @property
    def policies(self):
        """Gets the policies of this V2HPAScalingRules.  # noqa: E501

        policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the HPAScalingRules will be discarded as invalid  # noqa: E501

        :return: The policies of this V2HPAScalingRules.  # noqa: E501
        :rtype: list[V2HPAScalingPolicy]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this V2HPAScalingRules.

        policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the HPAScalingRules will be discarded as invalid  # noqa: E501

        :param policies: The policies of this V2HPAScalingRules.  # noqa: E501
        :type: list[V2HPAScalingPolicy]
        """

        self._policies = policies

    @property
    def select_policy(self):
        """Gets the select_policy of this V2HPAScalingRules.  # noqa: E501

        selectPolicy is used to specify which policy should be used. If not set, the default value Max is used.  # noqa: E501

        :return: The select_policy of this V2HPAScalingRules.  # noqa: E501
        :rtype: str
        """
        return self._select_policy

    @select_policy.setter
    def select_policy(self, select_policy):
        """Sets the select_policy of this V2HPAScalingRules.

        selectPolicy is used to specify which policy should be used. If not set, the default value Max is used.  # noqa: E501

        :param select_policy: The select_policy of this V2HPAScalingRules.  # noqa: E501
        :type: str
        """

        self._select_policy = select_policy

    @property
    def stabilization_window_seconds(self):
        """Gets the stabilization_window_seconds of this V2HPAScalingRules.  # noqa: E501

        StabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long).  # noqa: E501

        :return: The stabilization_window_seconds of this V2HPAScalingRules.  # noqa: E501
        :rtype: int
        """
        return self._stabilization_window_seconds

    @stabilization_window_seconds.setter
    def stabilization_window_seconds(self, stabilization_window_seconds):
        """Sets the stabilization_window_seconds of this V2HPAScalingRules.

        StabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long).  # noqa: E501

        :param stabilization_window_seconds: The stabilization_window_seconds of this V2HPAScalingRules.  # noqa: E501
        :type: int
        """

        self._stabilization_window_seconds = stabilization_window_seconds

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
        if not isinstance(other, V2HPAScalingRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2HPAScalingRules):
            return True

        return self.to_dict() != other.to_dict()
