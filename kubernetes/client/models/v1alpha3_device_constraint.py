# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.32
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1alpha3DeviceConstraint(object):
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
        'match_attribute': 'str',
        'requests': 'list[str]'
    }

    attribute_map = {
        'match_attribute': 'matchAttribute',
        'requests': 'requests'
    }

    def __init__(self, match_attribute=None, requests=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha3DeviceConstraint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._match_attribute = None
        self._requests = None
        self.discriminator = None

        if match_attribute is not None:
            self.match_attribute = match_attribute
        if requests is not None:
            self.requests = requests

    @property
    def match_attribute(self):
        """Gets the match_attribute of this V1alpha3DeviceConstraint.  # noqa: E501

        MatchAttribute requires that all devices in question have this attribute and that its type and value are the same across those devices.  For example, if you specified \"dra.example.com/numa\" (a hypothetical example!), then only devices in the same NUMA node will be chosen. A device which does not have that attribute will not be chosen. All devices should use a value of the same type for this attribute because that is part of its specification, but if one device doesn't, then it also will not be chosen.  Must include the domain qualifier.  # noqa: E501

        :return: The match_attribute of this V1alpha3DeviceConstraint.  # noqa: E501
        :rtype: str
        """
        return self._match_attribute

    @match_attribute.setter
    def match_attribute(self, match_attribute):
        """Sets the match_attribute of this V1alpha3DeviceConstraint.

        MatchAttribute requires that all devices in question have this attribute and that its type and value are the same across those devices.  For example, if you specified \"dra.example.com/numa\" (a hypothetical example!), then only devices in the same NUMA node will be chosen. A device which does not have that attribute will not be chosen. All devices should use a value of the same type for this attribute because that is part of its specification, but if one device doesn't, then it also will not be chosen.  Must include the domain qualifier.  # noqa: E501

        :param match_attribute: The match_attribute of this V1alpha3DeviceConstraint.  # noqa: E501
        :type: str
        """

        self._match_attribute = match_attribute

    @property
    def requests(self):
        """Gets the requests of this V1alpha3DeviceConstraint.  # noqa: E501

        Requests is a list of the one or more requests in this claim which must co-satisfy this constraint. If a request is fulfilled by multiple devices, then all of the devices must satisfy the constraint. If this is not specified, this constraint applies to all requests in this claim.  # noqa: E501

        :return: The requests of this V1alpha3DeviceConstraint.  # noqa: E501
        :rtype: list[str]
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this V1alpha3DeviceConstraint.

        Requests is a list of the one or more requests in this claim which must co-satisfy this constraint. If a request is fulfilled by multiple devices, then all of the devices must satisfy the constraint. If this is not specified, this constraint applies to all requests in this claim.  # noqa: E501

        :param requests: The requests of this V1alpha3DeviceConstraint.  # noqa: E501
        :type: list[str]
        """

        self._requests = requests

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
        if not isinstance(other, V1alpha3DeviceConstraint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha3DeviceConstraint):
            return True

        return self.to_dict() != other.to_dict()
