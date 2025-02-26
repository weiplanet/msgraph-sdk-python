from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class BookingWorkTimeSlot(AdditionalDataHolder, Parsable):
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
        Instantiates a new bookingWorkTimeSlot and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The time of the day when work stops. For example, 17:00:00.0000000.
        self._end_time: Optional[Time] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The time of the day when work starts. For example, 08:00:00.0000000.
        self._start_time: Optional[Time] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingWorkTimeSlot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingWorkTimeSlot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingWorkTimeSlot()

    @property
    def end_time(self,) -> Optional[Time]:
        """
        Gets the endTime property value. The time of the day when work stops. For example, 17:00:00.0000000.
        Returns: Optional[Time]
        """
        return self._end_time

    @end_time.setter
    def end_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the endTime property value. The time of the day when work stops. For example, 17:00:00.0000000.
        Args:
            value: Value to set for the endTime property.
        """
        self._end_time = value

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "end_time": lambda n : setattr(self, 'end_time', n.get_object_value(Time)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start_time": lambda n : setattr(self, 'start_time', n.get_object_value(Time)),
        }
        return fields

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
        writer.write_object_value("endTime", self.end_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("startTime", self.start_time)
        writer.write_additional_data_value(self.additional_data)

    @property
    def start_time(self,) -> Optional[Time]:
        """
        Gets the startTime property value. The time of the day when work starts. For example, 08:00:00.0000000.
        Returns: Optional[Time]
        """
        return self._start_time

    @start_time.setter
    def start_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the startTime property value. The time of the day when work starts. For example, 08:00:00.0000000.
        Args:
            value: Value to set for the startTime property.
        """
        self._start_time = value


