from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class GetMemberGroupsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the getMemberGroups method.
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

    def __init__(self,) -> None:
        """
        Instantiates a new getMemberGroupsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The securityEnabledOnly property
        self._security_enabled_only: Optional[bool] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetMemberGroupsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetMemberGroupsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetMemberGroupsPostRequestBody()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "security_enabled_only": lambda n : setattr(self, 'security_enabled_only', n.get_bool_value()),
        }
        return fields

    @property
    def security_enabled_only(self,) -> Optional[bool]:
        """
        Gets the securityEnabledOnly property value. The securityEnabledOnly property
        Returns: Optional[bool]
        """
        return self._security_enabled_only

    @security_enabled_only.setter
    def security_enabled_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityEnabledOnly property value. The securityEnabledOnly property
        Args:
            value: Value to set for the securityEnabledOnly property.
        """
        self._security_enabled_only = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("securityEnabledOnly", self.security_enabled_only)
        writer.write_additional_data_value(self.additional_data)


