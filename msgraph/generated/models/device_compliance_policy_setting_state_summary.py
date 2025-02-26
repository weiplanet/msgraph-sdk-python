from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import device_compliance_setting_state, entity, policy_platform_type

class DeviceCompliancePolicySettingStateSummary(entity.Entity):
    """
    Device Compilance Policy Setting State summary across the account.
    """
    @property
    def compliant_device_count(self,) -> Optional[int]:
        """
        Gets the compliantDeviceCount property value. Number of compliant devices
        Returns: Optional[int]
        """
        return self._compliant_device_count

    @compliant_device_count.setter
    def compliant_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the compliantDeviceCount property value. Number of compliant devices
        Args:
            value: Value to set for the compliantDeviceCount property.
        """
        self._compliant_device_count = value

    @property
    def conflict_device_count(self,) -> Optional[int]:
        """
        Gets the conflictDeviceCount property value. Number of conflict devices
        Returns: Optional[int]
        """
        return self._conflict_device_count

    @conflict_device_count.setter
    def conflict_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the conflictDeviceCount property value. Number of conflict devices
        Args:
            value: Value to set for the conflictDeviceCount property.
        """
        self._conflict_device_count = value

    def __init__(self,) -> None:
        """
        Instantiates a new deviceCompliancePolicySettingStateSummary and sets the default values.
        """
        super().__init__()
        # Number of compliant devices
        self._compliant_device_count: Optional[int] = None
        # Number of conflict devices
        self._conflict_device_count: Optional[int] = None
        # Not yet documented
        self._device_compliance_setting_states: Optional[List[device_compliance_setting_state.DeviceComplianceSettingState]] = None
        # Number of error devices
        self._error_device_count: Optional[int] = None
        # Number of NonCompliant devices
        self._non_compliant_device_count: Optional[int] = None
        # Number of not applicable devices
        self._not_applicable_device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Supported platform types for policies.
        self._platform_type: Optional[policy_platform_type.PolicyPlatformType] = None
        # Number of remediated devices
        self._remediated_device_count: Optional[int] = None
        # The setting class name and property name.
        self._setting: Optional[str] = None
        # Name of the setting.
        self._setting_name: Optional[str] = None
        # Number of unknown devices
        self._unknown_device_count: Optional[int] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicySettingStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicySettingStateSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceCompliancePolicySettingStateSummary()

    @property
    def device_compliance_setting_states(self,) -> Optional[List[device_compliance_setting_state.DeviceComplianceSettingState]]:
        """
        Gets the deviceComplianceSettingStates property value. Not yet documented
        Returns: Optional[List[device_compliance_setting_state.DeviceComplianceSettingState]]
        """
        return self._device_compliance_setting_states

    @device_compliance_setting_states.setter
    def device_compliance_setting_states(self,value: Optional[List[device_compliance_setting_state.DeviceComplianceSettingState]] = None) -> None:
        """
        Sets the deviceComplianceSettingStates property value. Not yet documented
        Args:
            value: Value to set for the deviceComplianceSettingStates property.
        """
        self._device_compliance_setting_states = value

    @property
    def error_device_count(self,) -> Optional[int]:
        """
        Gets the errorDeviceCount property value. Number of error devices
        Returns: Optional[int]
        """
        return self._error_device_count

    @error_device_count.setter
    def error_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorDeviceCount property value. Number of error devices
        Args:
            value: Value to set for the errorDeviceCount property.
        """
        self._error_device_count = value

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compliant_device_count": lambda n : setattr(self, 'compliant_device_count', n.get_int_value()),
            "conflict_device_count": lambda n : setattr(self, 'conflict_device_count', n.get_int_value()),
            "device_compliance_setting_states": lambda n : setattr(self, 'device_compliance_setting_states', n.get_collection_of_object_values(device_compliance_setting_state.DeviceComplianceSettingState)),
            "error_device_count": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "non_compliant_device_count": lambda n : setattr(self, 'non_compliant_device_count', n.get_int_value()),
            "not_applicable_device_count": lambda n : setattr(self, 'not_applicable_device_count', n.get_int_value()),
            "platform_type": lambda n : setattr(self, 'platform_type', n.get_enum_value(policy_platform_type.PolicyPlatformType)),
            "remediated_device_count": lambda n : setattr(self, 'remediated_device_count', n.get_int_value()),
            "setting": lambda n : setattr(self, 'setting', n.get_str_value()),
            "setting_name": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "unknown_device_count": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    @property
    def non_compliant_device_count(self,) -> Optional[int]:
        """
        Gets the nonCompliantDeviceCount property value. Number of NonCompliant devices
        Returns: Optional[int]
        """
        return self._non_compliant_device_count

    @non_compliant_device_count.setter
    def non_compliant_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the nonCompliantDeviceCount property value. Number of NonCompliant devices
        Args:
            value: Value to set for the nonCompliantDeviceCount property.
        """
        self._non_compliant_device_count = value

    @property
    def not_applicable_device_count(self,) -> Optional[int]:
        """
        Gets the notApplicableDeviceCount property value. Number of not applicable devices
        Returns: Optional[int]
        """
        return self._not_applicable_device_count

    @not_applicable_device_count.setter
    def not_applicable_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notApplicableDeviceCount property value. Number of not applicable devices
        Args:
            value: Value to set for the notApplicableDeviceCount property.
        """
        self._not_applicable_device_count = value

    @property
    def platform_type(self,) -> Optional[policy_platform_type.PolicyPlatformType]:
        """
        Gets the platformType property value. Supported platform types for policies.
        Returns: Optional[policy_platform_type.PolicyPlatformType]
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self,value: Optional[policy_platform_type.PolicyPlatformType] = None) -> None:
        """
        Sets the platformType property value. Supported platform types for policies.
        Args:
            value: Value to set for the platformType property.
        """
        self._platform_type = value

    @property
    def remediated_device_count(self,) -> Optional[int]:
        """
        Gets the remediatedDeviceCount property value. Number of remediated devices
        Returns: Optional[int]
        """
        return self._remediated_device_count

    @remediated_device_count.setter
    def remediated_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the remediatedDeviceCount property value. Number of remediated devices
        Args:
            value: Value to set for the remediatedDeviceCount property.
        """
        self._remediated_device_count = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("compliantDeviceCount", self.compliant_device_count)
        writer.write_int_value("conflictDeviceCount", self.conflict_device_count)
        writer.write_collection_of_object_values("deviceComplianceSettingStates", self.device_compliance_setting_states)
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("nonCompliantDeviceCount", self.non_compliant_device_count)
        writer.write_int_value("notApplicableDeviceCount", self.not_applicable_device_count)
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_int_value("remediatedDeviceCount", self.remediated_device_count)
        writer.write_str_value("setting", self.setting)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_int_value("unknownDeviceCount", self.unknown_device_count)

    @property
    def setting(self,) -> Optional[str]:
        """
        Gets the setting property value. The setting class name and property name.
        Returns: Optional[str]
        """
        return self._setting

    @setting.setter
    def setting(self,value: Optional[str] = None) -> None:
        """
        Sets the setting property value. The setting class name and property name.
        Args:
            value: Value to set for the setting property.
        """
        self._setting = value

    @property
    def setting_name(self,) -> Optional[str]:
        """
        Gets the settingName property value. Name of the setting.
        Returns: Optional[str]
        """
        return self._setting_name

    @setting_name.setter
    def setting_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingName property value. Name of the setting.
        Args:
            value: Value to set for the settingName property.
        """
        self._setting_name = value

    @property
    def unknown_device_count(self,) -> Optional[int]:
        """
        Gets the unknownDeviceCount property value. Number of unknown devices
        Returns: Optional[int]
        """
        return self._unknown_device_count

    @unknown_device_count.setter
    def unknown_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownDeviceCount property value. Number of unknown devices
        Args:
            value: Value to set for the unknownDeviceCount property.
        """
        self._unknown_device_count = value


