from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class GetCachedReportPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the getCachedReport method.
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
        Instantiates a new getCachedReportPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The groupBy property
        self._group_by: Optional[List[str]] = None
        # The id property
        self._id: Optional[str] = None
        # The orderBy property
        self._order_by: Optional[List[str]] = None
        # The search property
        self._search: Optional[str] = None
        # The select property
        self._select: Optional[List[str]] = None
        # The skip property
        self._skip: Optional[int] = None
        # The top property
        self._top: Optional[int] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetCachedReportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetCachedReportPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetCachedReportPostRequestBody()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "group_by": lambda n : setattr(self, 'group_by', n.get_collection_of_primitive_values(str)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "order_by": lambda n : setattr(self, 'order_by', n.get_collection_of_primitive_values(str)),
            "search": lambda n : setattr(self, 'search', n.get_str_value()),
            "select": lambda n : setattr(self, 'select', n.get_collection_of_primitive_values(str)),
            "skip": lambda n : setattr(self, 'skip', n.get_int_value()),
            "top": lambda n : setattr(self, 'top', n.get_int_value()),
        }
        return fields

    @property
    def group_by(self,) -> Optional[List[str]]:
        """
        Gets the groupBy property value. The groupBy property
        Returns: Optional[List[str]]
        """
        return self._group_by

    @group_by.setter
    def group_by(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the groupBy property value. The groupBy property
        Args:
            value: Value to set for the groupBy property.
        """
        self._group_by = value

    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The id property
        Returns: Optional[str]
        """
        return self._id

    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The id property
        Args:
            value: Value to set for the id property.
        """
        self._id = value

    @property
    def order_by(self,) -> Optional[List[str]]:
        """
        Gets the orderBy property value. The orderBy property
        Returns: Optional[List[str]]
        """
        return self._order_by

    @order_by.setter
    def order_by(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the orderBy property value. The orderBy property
        Args:
            value: Value to set for the orderBy property.
        """
        self._order_by = value

    @property
    def search(self,) -> Optional[str]:
        """
        Gets the search property value. The search property
        Returns: Optional[str]
        """
        return self._search

    @search.setter
    def search(self,value: Optional[str] = None) -> None:
        """
        Sets the search property value. The search property
        Args:
            value: Value to set for the search property.
        """
        self._search = value

    @property
    def select(self,) -> Optional[List[str]]:
        """
        Gets the select property value. The select property
        Returns: Optional[List[str]]
        """
        return self._select

    @select.setter
    def select(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the select property value. The select property
        Args:
            value: Value to set for the select property.
        """
        self._select = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("groupBy", self.group_by)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_primitive_values("orderBy", self.order_by)
        writer.write_str_value("search", self.search)
        writer.write_collection_of_primitive_values("select", self.select)
        writer.write_int_value("skip", self.skip)
        writer.write_int_value("top", self.top)
        writer.write_additional_data_value(self.additional_data)

    @property
    def skip(self,) -> Optional[int]:
        """
        Gets the skip property value. The skip property
        Returns: Optional[int]
        """
        return self._skip

    @skip.setter
    def skip(self,value: Optional[int] = None) -> None:
        """
        Sets the skip property value. The skip property
        Args:
            value: Value to set for the skip property.
        """
        self._skip = value

    @property
    def top(self,) -> Optional[int]:
        """
        Gets the top property value. The top property
        Returns: Optional[int]
        """
        return self._top

    @top.setter
    def top(self,value: Optional[int] = None) -> None:
        """
        Sets the top property value. The top property
        Args:
            value: Value to set for the top property.
        """
        self._top = value


