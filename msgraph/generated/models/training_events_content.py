from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import assigned_training_info

class TrainingEventsContent(AdditionalDataHolder, Parsable):
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
    def assigned_trainings_infos(self,) -> Optional[List[assigned_training_info.AssignedTrainingInfo]]:
        """
        Gets the assignedTrainingsInfos property value. List of assigned trainings and their information in an attack simulation and training campaign.
        Returns: Optional[List[assigned_training_info.AssignedTrainingInfo]]
        """
        return self._assigned_trainings_infos

    @assigned_trainings_infos.setter
    def assigned_trainings_infos(self,value: Optional[List[assigned_training_info.AssignedTrainingInfo]] = None) -> None:
        """
        Sets the assignedTrainingsInfos property value. List of assigned trainings and their information in an attack simulation and training campaign.
        Args:
            value: Value to set for the assignedTrainingsInfos property.
        """
        self._assigned_trainings_infos = value

    def __init__(self,) -> None:
        """
        Instantiates a new trainingEventsContent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # List of assigned trainings and their information in an attack simulation and training campaign.
        self._assigned_trainings_infos: Optional[List[assigned_training_info.AssignedTrainingInfo]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Number of users who were assigned trainings in an attack simulation and training campaign.
        self._trainings_assigned_user_count: Optional[int] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TrainingEventsContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TrainingEventsContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TrainingEventsContent()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assigned_trainings_infos": lambda n : setattr(self, 'assigned_trainings_infos', n.get_collection_of_object_values(assigned_training_info.AssignedTrainingInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "trainings_assigned_user_count": lambda n : setattr(self, 'trainings_assigned_user_count', n.get_int_value()),
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
        writer.write_collection_of_object_values("assignedTrainingsInfos", self.assigned_trainings_infos)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("trainingsAssignedUserCount", self.trainings_assigned_user_count)
        writer.write_additional_data_value(self.additional_data)

    @property
    def trainings_assigned_user_count(self,) -> Optional[int]:
        """
        Gets the trainingsAssignedUserCount property value. Number of users who were assigned trainings in an attack simulation and training campaign.
        Returns: Optional[int]
        """
        return self._trainings_assigned_user_count

    @trainings_assigned_user_count.setter
    def trainings_assigned_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the trainingsAssignedUserCount property value. Number of users who were assigned trainings in an attack simulation and training campaign.
        Args:
            value: Value to set for the trainingsAssignedUserCount property.
        """
        self._trainings_assigned_user_count = value


