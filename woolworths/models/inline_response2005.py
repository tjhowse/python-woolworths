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

class InlineResponse2005(object):
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
        'first_name': 'str',
        'login_result': 'str',
        'authentication_error_message': 'object',
        'login_collection_zone_messages': 'list[object]',
        'password_reset_token': 'object',
        'has_collection_zone_messages': 'bool',
        'login_via_agent': 'object',
        'preferred_channel': 'float',
        'valid_phone': 'bool',
        'otp_result': 'bool',
        'masked_channel': 'str'
    }

    attribute_map = {
        'first_name': 'FirstName',
        'login_result': 'LoginResult',
        'authentication_error_message': 'AuthenticationErrorMessage',
        'login_collection_zone_messages': 'LoginCollectionZoneMessages',
        'password_reset_token': 'PasswordResetToken',
        'has_collection_zone_messages': 'HasCollectionZoneMessages',
        'login_via_agent': 'LoginViaAgent',
        'preferred_channel': 'PreferredChannel',
        'valid_phone': 'ValidPhone',
        'otp_result': 'OtpResult',
        'masked_channel': 'MaskedChannel'
    }

    def __init__(self, first_name=None, login_result=None, authentication_error_message=None, login_collection_zone_messages=None, password_reset_token=None, has_collection_zone_messages=None, login_via_agent=None, preferred_channel=None, valid_phone=None, otp_result=None, masked_channel=None):  # noqa: E501
        """InlineResponse2005 - a model defined in Swagger"""  # noqa: E501
        self._first_name = None
        self._login_result = None
        self._authentication_error_message = None
        self._login_collection_zone_messages = None
        self._password_reset_token = None
        self._has_collection_zone_messages = None
        self._login_via_agent = None
        self._preferred_channel = None
        self._valid_phone = None
        self._otp_result = None
        self._masked_channel = None
        self.discriminator = None
        if first_name is not None:
            self.first_name = first_name
        if login_result is not None:
            self.login_result = login_result
        if authentication_error_message is not None:
            self.authentication_error_message = authentication_error_message
        if login_collection_zone_messages is not None:
            self.login_collection_zone_messages = login_collection_zone_messages
        if password_reset_token is not None:
            self.password_reset_token = password_reset_token
        if has_collection_zone_messages is not None:
            self.has_collection_zone_messages = has_collection_zone_messages
        if login_via_agent is not None:
            self.login_via_agent = login_via_agent
        if preferred_channel is not None:
            self.preferred_channel = preferred_channel
        if valid_phone is not None:
            self.valid_phone = valid_phone
        if otp_result is not None:
            self.otp_result = otp_result
        if masked_channel is not None:
            self.masked_channel = masked_channel

    @property
    def first_name(self):
        """Gets the first_name of this InlineResponse2005.  # noqa: E501


        :return: The first_name of this InlineResponse2005.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this InlineResponse2005.


        :param first_name: The first_name of this InlineResponse2005.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def login_result(self):
        """Gets the login_result of this InlineResponse2005.  # noqa: E501


        :return: The login_result of this InlineResponse2005.  # noqa: E501
        :rtype: str
        """
        return self._login_result

    @login_result.setter
    def login_result(self, login_result):
        """Sets the login_result of this InlineResponse2005.


        :param login_result: The login_result of this InlineResponse2005.  # noqa: E501
        :type: str
        """

        self._login_result = login_result

    @property
    def authentication_error_message(self):
        """Gets the authentication_error_message of this InlineResponse2005.  # noqa: E501


        :return: The authentication_error_message of this InlineResponse2005.  # noqa: E501
        :rtype: object
        """
        return self._authentication_error_message

    @authentication_error_message.setter
    def authentication_error_message(self, authentication_error_message):
        """Sets the authentication_error_message of this InlineResponse2005.


        :param authentication_error_message: The authentication_error_message of this InlineResponse2005.  # noqa: E501
        :type: object
        """

        self._authentication_error_message = authentication_error_message

    @property
    def login_collection_zone_messages(self):
        """Gets the login_collection_zone_messages of this InlineResponse2005.  # noqa: E501


        :return: The login_collection_zone_messages of this InlineResponse2005.  # noqa: E501
        :rtype: list[object]
        """
        return self._login_collection_zone_messages

    @login_collection_zone_messages.setter
    def login_collection_zone_messages(self, login_collection_zone_messages):
        """Sets the login_collection_zone_messages of this InlineResponse2005.


        :param login_collection_zone_messages: The login_collection_zone_messages of this InlineResponse2005.  # noqa: E501
        :type: list[object]
        """

        self._login_collection_zone_messages = login_collection_zone_messages

    @property
    def password_reset_token(self):
        """Gets the password_reset_token of this InlineResponse2005.  # noqa: E501


        :return: The password_reset_token of this InlineResponse2005.  # noqa: E501
        :rtype: object
        """
        return self._password_reset_token

    @password_reset_token.setter
    def password_reset_token(self, password_reset_token):
        """Sets the password_reset_token of this InlineResponse2005.


        :param password_reset_token: The password_reset_token of this InlineResponse2005.  # noqa: E501
        :type: object
        """

        self._password_reset_token = password_reset_token

    @property
    def has_collection_zone_messages(self):
        """Gets the has_collection_zone_messages of this InlineResponse2005.  # noqa: E501


        :return: The has_collection_zone_messages of this InlineResponse2005.  # noqa: E501
        :rtype: bool
        """
        return self._has_collection_zone_messages

    @has_collection_zone_messages.setter
    def has_collection_zone_messages(self, has_collection_zone_messages):
        """Sets the has_collection_zone_messages of this InlineResponse2005.


        :param has_collection_zone_messages: The has_collection_zone_messages of this InlineResponse2005.  # noqa: E501
        :type: bool
        """

        self._has_collection_zone_messages = has_collection_zone_messages

    @property
    def login_via_agent(self):
        """Gets the login_via_agent of this InlineResponse2005.  # noqa: E501


        :return: The login_via_agent of this InlineResponse2005.  # noqa: E501
        :rtype: object
        """
        return self._login_via_agent

    @login_via_agent.setter
    def login_via_agent(self, login_via_agent):
        """Sets the login_via_agent of this InlineResponse2005.


        :param login_via_agent: The login_via_agent of this InlineResponse2005.  # noqa: E501
        :type: object
        """

        self._login_via_agent = login_via_agent

    @property
    def preferred_channel(self):
        """Gets the preferred_channel of this InlineResponse2005.  # noqa: E501


        :return: The preferred_channel of this InlineResponse2005.  # noqa: E501
        :rtype: float
        """
        return self._preferred_channel

    @preferred_channel.setter
    def preferred_channel(self, preferred_channel):
        """Sets the preferred_channel of this InlineResponse2005.


        :param preferred_channel: The preferred_channel of this InlineResponse2005.  # noqa: E501
        :type: float
        """

        self._preferred_channel = preferred_channel

    @property
    def valid_phone(self):
        """Gets the valid_phone of this InlineResponse2005.  # noqa: E501


        :return: The valid_phone of this InlineResponse2005.  # noqa: E501
        :rtype: bool
        """
        return self._valid_phone

    @valid_phone.setter
    def valid_phone(self, valid_phone):
        """Sets the valid_phone of this InlineResponse2005.


        :param valid_phone: The valid_phone of this InlineResponse2005.  # noqa: E501
        :type: bool
        """

        self._valid_phone = valid_phone

    @property
    def otp_result(self):
        """Gets the otp_result of this InlineResponse2005.  # noqa: E501


        :return: The otp_result of this InlineResponse2005.  # noqa: E501
        :rtype: bool
        """
        return self._otp_result

    @otp_result.setter
    def otp_result(self, otp_result):
        """Sets the otp_result of this InlineResponse2005.


        :param otp_result: The otp_result of this InlineResponse2005.  # noqa: E501
        :type: bool
        """

        self._otp_result = otp_result

    @property
    def masked_channel(self):
        """Gets the masked_channel of this InlineResponse2005.  # noqa: E501


        :return: The masked_channel of this InlineResponse2005.  # noqa: E501
        :rtype: str
        """
        return self._masked_channel

    @masked_channel.setter
    def masked_channel(self, masked_channel):
        """Sets the masked_channel of this InlineResponse2005.


        :param masked_channel: The masked_channel of this InlineResponse2005.  # noqa: E501
        :type: str
        """

        self._masked_channel = masked_channel

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
        if issubclass(InlineResponse2005, dict):
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
        if not isinstance(other, InlineResponse2005):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
