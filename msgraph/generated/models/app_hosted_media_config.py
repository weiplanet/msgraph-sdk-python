from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import media_config

class AppHostedMediaConfig(media_config.MediaConfig):
    @property
    def blob(self,) -> Optional[str]:
        """
        Gets the blob property value. The media configuration blob generated by smart media agent.
        Returns: Optional[str]
        """
        return self._blob

    @blob.setter
    def blob(self,value: Optional[str] = None) -> None:
        """
        Sets the blob property value. The media configuration blob generated by smart media agent.
        Args:
            value: Value to set for the blob property.
        """
        self._blob = value

    def __init__(self,) -> None:
        """
        Instantiates a new AppHostedMediaConfig and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.appHostedMediaConfig"
        # The media configuration blob generated by smart media agent.
        self._blob: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppHostedMediaConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppHostedMediaConfig
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppHostedMediaConfig()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "blob": lambda n : setattr(self, 'blob', n.get_str_value()),
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
        writer.write_str_value("blob", self.blob)


