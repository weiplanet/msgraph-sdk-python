from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import education_resource

class EducationFileResource(education_resource.EducationResource):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationFileResource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationFileResource"
        # Location on disk of the file resource.
        self._file_url: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationFileResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationFileResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationFileResource()

    @property
    def file_url(self,) -> Optional[str]:
        """
        Gets the fileUrl property value. Location on disk of the file resource.
        Returns: Optional[str]
        """
        return self._file_url

    @file_url.setter
    def file_url(self,value: Optional[str] = None) -> None:
        """
        Sets the fileUrl property value. Location on disk of the file resource.
        Args:
            value: Value to set for the fileUrl property.
        """
        self._file_url = value

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "file_url": lambda n : setattr(self, 'file_url', n.get_str_value()),
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
        writer.write_str_value("fileUrl", self.file_url)


