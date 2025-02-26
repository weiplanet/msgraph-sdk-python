from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class LicenseAssignmentState(AdditionalDataHolder, Parsable):
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

    @property
    def assigned_by_group(self,) -> Optional[str]:
        """
        Gets the assignedByGroup property value. The assignedByGroup property
        Returns: Optional[str]
        """
        return self._assigned_by_group

    @assigned_by_group.setter
    def assigned_by_group(self,value: Optional[str] = None) -> None:
        """
        Sets the assignedByGroup property value. The assignedByGroup property
        Args:
            value: Value to set for the assignedByGroup property.
        """
        self._assigned_by_group = value

    def __init__(self,) -> None:
        """
        Instantiates a new licenseAssignmentState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The assignedByGroup property
        self._assigned_by_group: Optional[str] = None
        # The disabledPlans property
        self._disabled_plans: Optional[List[str]] = None
        # The error property
        self._error: Optional[str] = None
        # The lastUpdatedDateTime property
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The skuId property
        self._sku_id: Optional[str] = None
        # The state property
        self._state: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LicenseAssignmentState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LicenseAssignmentState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LicenseAssignmentState()

    @property
    def disabled_plans(self,) -> Optional[List[str]]:
        """
        Gets the disabledPlans property value. The disabledPlans property
        Returns: Optional[List[str]]
        """
        return self._disabled_plans

    @disabled_plans.setter
    def disabled_plans(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the disabledPlans property value. The disabledPlans property
        Args:
            value: Value to set for the disabledPlans property.
        """
        self._disabled_plans = value

    @property
    def error(self,) -> Optional[str]:
        """
        Gets the error property value. The error property
        Returns: Optional[str]
        """
        return self._error

    @error.setter
    def error(self,value: Optional[str] = None) -> None:
        """
        Sets the error property value. The error property
        Args:
            value: Value to set for the error property.
        """
        self._error = value

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assigned_by_group": lambda n : setattr(self, 'assigned_by_group', n.get_str_value()),
            "disabled_plans": lambda n : setattr(self, 'disabled_plans', n.get_collection_of_primitive_values(str)),
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sku_id": lambda n : setattr(self, 'sku_id', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
        }
        return fields

    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. The lastUpdatedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time

    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. The lastUpdatedDateTime property
        Args:
            value: Value to set for the lastUpdatedDateTime property.
        """
        self._last_updated_date_time = value

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
        writer.write_str_value("assignedByGroup", self.assigned_by_group)
        writer.write_collection_of_primitive_values("disabledPlans", self.disabled_plans)
        writer.write_str_value("error", self.error)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("skuId", self.sku_id)
        writer.write_str_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)

    @property
    def sku_id(self,) -> Optional[str]:
        """
        Gets the skuId property value. The skuId property
        Returns: Optional[str]
        """
        return self._sku_id

    @sku_id.setter
    def sku_id(self,value: Optional[str] = None) -> None:
        """
        Sets the skuId property value. The skuId property
        Args:
            value: Value to set for the skuId property.
        """
        self._sku_id = value

    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. The state property
        Returns: Optional[str]
        """
        return self._state

    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value


