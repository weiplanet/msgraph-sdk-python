from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class GetByIdsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the getByIds method.
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
        Instantiates a new getByIdsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The ids property
        self._ids: Optional[List[str]] = None
        # The types property
        self._types: Optional[List[str]] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetByIdsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetByIdsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetByIdsPostRequestBody()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "ids": lambda n : setattr(self, 'ids', n.get_collection_of_primitive_values(str)),
            "types": lambda n : setattr(self, 'types', n.get_collection_of_primitive_values(str)),
        }
        return fields

    @property
    def ids(self,) -> Optional[List[str]]:
        """
        Gets the ids property value. The ids property
        Returns: Optional[List[str]]
        """
        return self._ids

    @ids.setter
    def ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the ids property value. The ids property
        Args:
            value: Value to set for the ids property.
        """
        self._ids = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("ids", self.ids)
        writer.write_collection_of_primitive_values("types", self.types)
        writer.write_additional_data_value(self.additional_data)

    @property
    def types(self,) -> Optional[List[str]]:
        """
        Gets the types property value. The types property
        Returns: Optional[List[str]]
        """
        return self._types

    @types.setter
    def types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the types property value. The types property
        Args:
            value: Value to set for the types property.
        """
        self._types = value


