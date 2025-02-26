from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import directory_object

class PolicyBase(directory_object.DirectoryObject):
    """
    Provides operations to manage the collection of agreementAcceptance entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new policyBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.policyBase"
        # Description for this policy. Required.
        self._description: Optional[str] = None
        # Display name for this policy. Required.
        self._display_name: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PolicyBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PolicyBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PolicyBase()

    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description for this policy. Required.
        Returns: Optional[str]
        """
        return self._description

    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description for this policy. Required.
        Args:
            value: Value to set for the description property.
        """
        self._description = value

    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name for this policy. Required.
        Returns: Optional[str]
        """
        return self._display_name

    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name for this policy. Required.
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
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)


