from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class LocalizedLabel(AdditionalDataHolder, Parsable):
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
        Instantiates a new localizedLabel and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether the label is the default label.
        self._is_default: Optional[bool] = None
        # The language tag for the label.
        self._language_tag: Optional[str] = None
        # The name of the label.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LocalizedLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LocalizedLabel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LocalizedLabel()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "language_tag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields

    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. Indicates whether the label is the default label.
        Returns: Optional[bool]
        """
        return self._is_default

    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. Indicates whether the label is the default label.
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value

    @property
    def language_tag(self,) -> Optional[str]:
        """
        Gets the languageTag property value. The language tag for the label.
        Returns: Optional[str]
        """
        return self._language_tag

    @language_tag.setter
    def language_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the languageTag property value. The language tag for the label.
        Args:
            value: Value to set for the languageTag property.
        """
        self._language_tag = value

    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the label.
        Returns: Optional[str]
        """
        return self._name

    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the label.
        Args:
            value: Value to set for the name property.
        """
        self._name = value

    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type

    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)


