from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class UpdateDevicePropertiesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the updateDeviceProperties method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value

    @property
    def addressable_user_name(self,) -> Optional[str]:
        """
        Gets the addressableUserName property value. The addressableUserName property
        Returns: Optional[str]
        """
        return self._addressable_user_name

    @addressable_user_name.setter
    def addressable_user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the addressableUserName property value. The addressableUserName property
        Args:
            value: Value to set for the addressableUserName property.
        """
        self._addressable_user_name = value

    def __init__(self,) -> None:
        """
        Instantiates a new updateDevicePropertiesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The addressableUserName property
        self._addressable_user_name: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The groupTag property
        self._group_tag: Optional[str] = None
        # The userPrincipalName property
        self._user_principal_name: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateDevicePropertiesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateDevicePropertiesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateDevicePropertiesPostRequestBody()

    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name

    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "addressable_user_name": lambda n : setattr(self, 'addressable_user_name', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "group_tag": lambda n : setattr(self, 'group_tag', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields

    @property
    def group_tag(self,) -> Optional[str]:
        """
        Gets the groupTag property value. The groupTag property
        Returns: Optional[str]
        """
        return self._group_tag

    @group_tag.setter
    def group_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the groupTag property value. The groupTag property
        Args:
            value: Value to set for the groupTag property.
        """
        self._group_tag = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("addressableUserName", self.addressable_user_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("groupTag", self.group_tag)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)

    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The userPrincipalName property
        Returns: Optional[str]
        """
        return self._user_principal_name

    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The userPrincipalName property
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value


