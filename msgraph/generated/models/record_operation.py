from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import comms_operation

class RecordOperation(comms_operation.CommsOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new RecordOperation and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The access token required to retrieve the recording.
        self._recording_access_token: Optional[str] = None
        # The location where the recording is located.
        self._recording_location: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecordOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecordOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RecordOperation()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "recording_access_token": lambda n : setattr(self, 'recording_access_token', n.get_str_value()),
            "recording_location": lambda n : setattr(self, 'recording_location', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    @property
    def recording_access_token(self,) -> Optional[str]:
        """
        Gets the recordingAccessToken property value. The access token required to retrieve the recording.
        Returns: Optional[str]
        """
        return self._recording_access_token

    @recording_access_token.setter
    def recording_access_token(self,value: Optional[str] = None) -> None:
        """
        Sets the recordingAccessToken property value. The access token required to retrieve the recording.
        Args:
            value: Value to set for the recordingAccessToken property.
        """
        self._recording_access_token = value

    @property
    def recording_location(self,) -> Optional[str]:
        """
        Gets the recordingLocation property value. The location where the recording is located.
        Returns: Optional[str]
        """
        return self._recording_location

    @recording_location.setter
    def recording_location(self,value: Optional[str] = None) -> None:
        """
        Sets the recordingLocation property value. The location where the recording is located.
        Args:
            value: Value to set for the recordingLocation property.
        """
        self._recording_location = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("recordingAccessToken", self.recording_access_token)
        writer.write_str_value("recordingLocation", self.recording_location)


