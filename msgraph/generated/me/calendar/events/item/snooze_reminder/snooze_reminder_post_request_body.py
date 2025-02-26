from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from ......models import date_time_time_zone

class SnoozeReminderPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the snoozeReminder method.
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
        Instantiates a new snoozeReminderPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The NewReminderTime property
        self._new_reminder_time: Optional[date_time_time_zone.DateTimeTimeZone] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SnoozeReminderPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SnoozeReminderPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SnoozeReminderPostRequestBody()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "new_reminder_time": lambda n : setattr(self, 'new_reminder_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
        }
        return fields

    @property
    def new_reminder_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the newReminderTime property value. The NewReminderTime property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._new_reminder_time

    @new_reminder_time.setter
    def new_reminder_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the newReminderTime property value. The NewReminderTime property
        Args:
            value: Value to set for the NewReminderTime property.
        """
        self._new_reminder_time = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("NewReminderTime", self.new_reminder_time)
        writer.write_additional_data_value(self.additional_data)


