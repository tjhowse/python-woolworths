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

class InlineResponse2007(object):
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
        'order_id': 'object',
        'amend_cutoff_time': 'object',
        'is_amending_market_order': 'bool'
    }

    attribute_map = {
        'order_id': 'OrderId',
        'amend_cutoff_time': 'AmendCutoffTime',
        'is_amending_market_order': 'IsAmendingMarketOrder'
    }

    def __init__(self, order_id=None, amend_cutoff_time=None, is_amending_market_order=None):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger"""  # noqa: E501
        self._order_id = None
        self._amend_cutoff_time = None
        self._is_amending_market_order = None
        self.discriminator = None
        if order_id is not None:
            self.order_id = order_id
        if amend_cutoff_time is not None:
            self.amend_cutoff_time = amend_cutoff_time
        if is_amending_market_order is not None:
            self.is_amending_market_order = is_amending_market_order

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse2007.  # noqa: E501


        :return: The order_id of this InlineResponse2007.  # noqa: E501
        :rtype: object
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse2007.


        :param order_id: The order_id of this InlineResponse2007.  # noqa: E501
        :type: object
        """

        self._order_id = order_id

    @property
    def amend_cutoff_time(self):
        """Gets the amend_cutoff_time of this InlineResponse2007.  # noqa: E501


        :return: The amend_cutoff_time of this InlineResponse2007.  # noqa: E501
        :rtype: object
        """
        return self._amend_cutoff_time

    @amend_cutoff_time.setter
    def amend_cutoff_time(self, amend_cutoff_time):
        """Sets the amend_cutoff_time of this InlineResponse2007.


        :param amend_cutoff_time: The amend_cutoff_time of this InlineResponse2007.  # noqa: E501
        :type: object
        """

        self._amend_cutoff_time = amend_cutoff_time

    @property
    def is_amending_market_order(self):
        """Gets the is_amending_market_order of this InlineResponse2007.  # noqa: E501


        :return: The is_amending_market_order of this InlineResponse2007.  # noqa: E501
        :rtype: bool
        """
        return self._is_amending_market_order

    @is_amending_market_order.setter
    def is_amending_market_order(self, is_amending_market_order):
        """Sets the is_amending_market_order of this InlineResponse2007.


        :param is_amending_market_order: The is_amending_market_order of this InlineResponse2007.  # noqa: E501
        :type: bool
        """

        self._is_amending_market_order = is_amending_market_order

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
        if issubclass(InlineResponse2007, dict):
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
        if not isinstance(other, InlineResponse2007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other