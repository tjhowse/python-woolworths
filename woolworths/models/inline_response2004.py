# coding: utf-8

"""
    flows_filtered Mitmproxy2Swagger

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2004(object):
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
        'authentication_method': 'str',
        'is_impersonated': 'bool'
    }

    attribute_map = {
        'authentication_method': 'AuthenticationMethod',
        'is_impersonated': 'IsImpersonated'
    }

    def __init__(self, authentication_method=None, is_impersonated=None):  # noqa: E501
        """InlineResponse2004 - a model defined in Swagger"""  # noqa: E501
        self._authentication_method = None
        self._is_impersonated = None
        self.discriminator = None
        if authentication_method is not None:
            self.authentication_method = authentication_method
        if is_impersonated is not None:
            self.is_impersonated = is_impersonated

    @property
    def authentication_method(self):
        """Gets the authentication_method of this InlineResponse2004.  # noqa: E501


        :return: The authentication_method of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, authentication_method):
        """Sets the authentication_method of this InlineResponse2004.


        :param authentication_method: The authentication_method of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._authentication_method = authentication_method

    @property
    def is_impersonated(self):
        """Gets the is_impersonated of this InlineResponse2004.  # noqa: E501


        :return: The is_impersonated of this InlineResponse2004.  # noqa: E501
        :rtype: bool
        """
        return self._is_impersonated

    @is_impersonated.setter
    def is_impersonated(self, is_impersonated):
        """Sets the is_impersonated of this InlineResponse2004.


        :param is_impersonated: The is_impersonated of this InlineResponse2004.  # noqa: E501
        :type: bool
        """

        self._is_impersonated = is_impersonated

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
        if issubclass(InlineResponse2004, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2004):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
