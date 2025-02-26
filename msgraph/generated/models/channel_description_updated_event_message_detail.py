from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import event_message_detail, identity_set

class ChannelDescriptionUpdatedEventMessageDetail(event_message_detail.EventMessageDetail):
    @property
    def channel_description(self,) -> Optional[str]:
        """
        Gets the channelDescription property value. The updated description of the channel.
        Returns: Optional[str]
        """
        return self._channel_description

    @channel_description.setter
    def channel_description(self,value: Optional[str] = None) -> None:
        """
        Sets the channelDescription property value. The updated description of the channel.
        Args:
            value: Value to set for the channelDescription property.
        """
        self._channel_description = value

    @property
    def channel_id(self,) -> Optional[str]:
        """
        Gets the channelId property value. Unique identifier of the channel.
        Returns: Optional[str]
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self,value: Optional[str] = None) -> None:
        """
        Sets the channelId property value. Unique identifier of the channel.
        Args:
            value: Value to set for the channelId property.
        """
        self._channel_id = value

    def __init__(self,) -> None:
        """
        Instantiates a new ChannelDescriptionUpdatedEventMessageDetail and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.channelDescriptionUpdatedEventMessageDetail"
        # The updated description of the channel.
        self._channel_description: Optional[str] = None
        # Unique identifier of the channel.
        self._channel_id: Optional[str] = None
        # Initiator of the event.
        self._initiator: Optional[identity_set.IdentitySet] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChannelDescriptionUpdatedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChannelDescriptionUpdatedEventMessageDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChannelDescriptionUpdatedEventMessageDetail()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "channel_description": lambda n : setattr(self, 'channel_description', n.get_str_value()),
            "channel_id": lambda n : setattr(self, 'channel_id', n.get_str_value()),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    @property
    def initiator(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the initiator property value. Initiator of the event.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._initiator

    @initiator.setter
    def initiator(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the initiator property value. Initiator of the event.
        Args:
            value: Value to set for the initiator property.
        """
        self._initiator = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("channelDescription", self.channel_description)
        writer.write_str_value("channelId", self.channel_id)
        writer.write_object_value("initiator", self.initiator)


