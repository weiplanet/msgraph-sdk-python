from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, Union

from ...models import user
from ...models.o_data_errors import o_data_error
from .activities import activities_request_builder
from .activities.item import user_activity_item_request_builder
from .agreement_acceptances import agreement_acceptances_request_builder
from .agreement_acceptances.item import agreement_acceptance_item_request_builder
from .app_role_assignments import app_role_assignments_request_builder
from .app_role_assignments.item import app_role_assignment_item_request_builder
from .assign_license import assign_license_request_builder
from .authentication import authentication_request_builder
from .calendar import calendar_request_builder
from .calendar_groups import calendar_groups_request_builder
from .calendar_groups.item import calendar_group_item_request_builder
from .calendars import calendars_request_builder
from .calendars.item import calendar_item_request_builder
from .calendar_view import calendar_view_request_builder
from .calendar_view.item import event_item_request_builder
from .change_password import change_password_request_builder
from .chats import chats_request_builder
from .chats.item import chat_item_request_builder
from .check_member_groups import check_member_groups_request_builder
from .check_member_objects import check_member_objects_request_builder
from .contact_folders import contact_folders_request_builder
from .contact_folders.item import contact_folder_item_request_builder
from .contacts import contacts_request_builder
from .contacts.item import contact_item_request_builder
from .created_objects import created_objects_request_builder
from .created_objects.item import directory_object_item_request_builder
from .device_management_troubleshooting_events import device_management_troubleshooting_events_request_builder
from .device_management_troubleshooting_events.item import device_management_troubleshooting_event_item_request_builder
from .direct_reports import direct_reports_request_builder
from .direct_reports.item import directory_object_item_request_builder
from .drive import drive_request_builder
from .drives import drives_request_builder
from .drives.item import drive_item_request_builder
from .events import events_request_builder
from .events.item import event_item_request_builder
from .export_personal_data import export_personal_data_request_builder
from .extensions import extensions_request_builder
from .extensions.item import extension_item_request_builder
from .find_meeting_times import find_meeting_times_request_builder
from .followed_sites import followed_sites_request_builder
from .followed_sites.item import site_item_request_builder
from .get_mail_tips import get_mail_tips_request_builder
from .get_managed_app_diagnostic_statuses import get_managed_app_diagnostic_statuses_request_builder
from .get_managed_app_policies import get_managed_app_policies_request_builder
from .get_member_groups import get_member_groups_request_builder
from .get_member_objects import get_member_objects_request_builder
from .inference_classification import inference_classification_request_builder
from .insights import insights_request_builder
from .joined_teams import joined_teams_request_builder
from .joined_teams.item import team_item_request_builder
from .license_details import license_details_request_builder
from .license_details.item import license_details_item_request_builder
from .mail_folders import mail_folders_request_builder
from .mail_folders.item import mail_folder_item_request_builder
from .managed_app_registrations import managed_app_registrations_request_builder
from .managed_app_registrations.item import managed_app_registration_item_request_builder
from .managed_devices import managed_devices_request_builder
from .managed_devices.item import managed_device_item_request_builder
from .manager import manager_request_builder
from .member_of import member_of_request_builder
from .member_of.item import directory_object_item_request_builder
from .messages import messages_request_builder
from .messages.item import message_item_request_builder
from .oauth2_permission_grants import oauth2_permission_grants_request_builder
from .oauth2_permission_grants.item import o_auth2_permission_grant_item_request_builder
from .onenote import onenote_request_builder
from .online_meetings import online_meetings_request_builder
from .online_meetings.item import online_meeting_item_request_builder
from .outlook import outlook_request_builder
from .owned_devices import owned_devices_request_builder
from .owned_devices.item import directory_object_item_request_builder
from .owned_objects import owned_objects_request_builder
from .owned_objects.item import directory_object_item_request_builder
from .people import people_request_builder
from .people.item import person_item_request_builder
from .photo import photo_request_builder
from .photos import photos_request_builder
from .photos.item import profile_photo_item_request_builder
from .planner import planner_request_builder
from .presence import presence_request_builder
from .registered_devices import registered_devices_request_builder
from .registered_devices.item import directory_object_item_request_builder
from .reminder_view_with_start_date_time_with_end_date_time import reminder_view_with_start_date_time_with_end_date_time_request_builder
from .remove_all_devices_from_management import remove_all_devices_from_management_request_builder
from .reprocess_license_assignment import reprocess_license_assignment_request_builder
from .restore import restore_request_builder
from .revoke_sign_in_sessions import revoke_sign_in_sessions_request_builder
from .scoped_role_member_of import scoped_role_member_of_request_builder
from .scoped_role_member_of.item import scoped_role_membership_item_request_builder
from .send_mail import send_mail_request_builder
from .settings import settings_request_builder
from .teamwork import teamwork_request_builder
from .todo import todo_request_builder
from .transitive_member_of import transitive_member_of_request_builder
from .transitive_member_of.item import directory_object_item_request_builder
from .translate_exchange_ids import translate_exchange_ids_request_builder
from .wipe_managed_app_registrations_by_device_tag import wipe_managed_app_registrations_by_device_tag_request_builder

class UserItemRequestBuilder():
    """
    Provides operations to manage the collection of user entities.
    """
    def activities(self) -> activities_request_builder.ActivitiesRequestBuilder:
        """
        Provides operations to manage the activities property of the microsoft.graph.user entity.
        """
        return activities_request_builder.ActivitiesRequestBuilder(self.request_adapter, self.path_parameters)

    def agreement_acceptances(self) -> agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder:
        """
        Provides operations to manage the agreementAcceptances property of the microsoft.graph.user entity.
        """
        return agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder(self.request_adapter, self.path_parameters)

    def app_role_assignments(self) -> app_role_assignments_request_builder.AppRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the appRoleAssignments property of the microsoft.graph.user entity.
        """
        return app_role_assignments_request_builder.AppRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)

    def assign_license(self) -> assign_license_request_builder.AssignLicenseRequestBuilder:
        """
        Provides operations to call the assignLicense method.
        """
        return assign_license_request_builder.AssignLicenseRequestBuilder(self.request_adapter, self.path_parameters)

    def authentication(self) -> authentication_request_builder.AuthenticationRequestBuilder:
        """
        Provides operations to manage the authentication property of the microsoft.graph.user entity.
        """
        return authentication_request_builder.AuthenticationRequestBuilder(self.request_adapter, self.path_parameters)

    def calendar(self) -> calendar_request_builder.CalendarRequestBuilder:
        """
        Provides operations to manage the calendar property of the microsoft.graph.user entity.
        """
        return calendar_request_builder.CalendarRequestBuilder(self.request_adapter, self.path_parameters)

    def calendar_groups(self) -> calendar_groups_request_builder.CalendarGroupsRequestBuilder:
        """
        Provides operations to manage the calendarGroups property of the microsoft.graph.user entity.
        """
        return calendar_groups_request_builder.CalendarGroupsRequestBuilder(self.request_adapter, self.path_parameters)

    def calendars(self) -> calendars_request_builder.CalendarsRequestBuilder:
        """
        Provides operations to manage the calendars property of the microsoft.graph.user entity.
        """
        return calendars_request_builder.CalendarsRequestBuilder(self.request_adapter, self.path_parameters)

    def calendar_view(self) -> calendar_view_request_builder.CalendarViewRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.user entity.
        """
        return calendar_view_request_builder.CalendarViewRequestBuilder(self.request_adapter, self.path_parameters)

    def change_password(self) -> change_password_request_builder.ChangePasswordRequestBuilder:
        """
        Provides operations to call the changePassword method.
        """
        return change_password_request_builder.ChangePasswordRequestBuilder(self.request_adapter, self.path_parameters)

    def chats(self) -> chats_request_builder.ChatsRequestBuilder:
        """
        Provides operations to manage the chats property of the microsoft.graph.user entity.
        """
        return chats_request_builder.ChatsRequestBuilder(self.request_adapter, self.path_parameters)

    def check_member_groups(self) -> check_member_groups_request_builder.CheckMemberGroupsRequestBuilder:
        """
        Provides operations to call the checkMemberGroups method.
        """
        return check_member_groups_request_builder.CheckMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)

    def check_member_objects(self) -> check_member_objects_request_builder.CheckMemberObjectsRequestBuilder:
        """
        Provides operations to call the checkMemberObjects method.
        """
        return check_member_objects_request_builder.CheckMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)

    def contact_folders(self) -> contact_folders_request_builder.ContactFoldersRequestBuilder:
        """
        Provides operations to manage the contactFolders property of the microsoft.graph.user entity.
        """
        return contact_folders_request_builder.ContactFoldersRequestBuilder(self.request_adapter, self.path_parameters)

    def contacts(self) -> contacts_request_builder.ContactsRequestBuilder:
        """
        Provides operations to manage the contacts property of the microsoft.graph.user entity.
        """
        return contacts_request_builder.ContactsRequestBuilder(self.request_adapter, self.path_parameters)

    def created_objects(self) -> created_objects_request_builder.CreatedObjectsRequestBuilder:
        """
        Provides operations to manage the createdObjects property of the microsoft.graph.user entity.
        """
        return created_objects_request_builder.CreatedObjectsRequestBuilder(self.request_adapter, self.path_parameters)

    def device_management_troubleshooting_events(self) -> device_management_troubleshooting_events_request_builder.DeviceManagementTroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the deviceManagementTroubleshootingEvents property of the microsoft.graph.user entity.
        """
        return device_management_troubleshooting_events_request_builder.DeviceManagementTroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)

    def direct_reports(self) -> direct_reports_request_builder.DirectReportsRequestBuilder:
        """
        Provides operations to manage the directReports property of the microsoft.graph.user entity.
        """
        return direct_reports_request_builder.DirectReportsRequestBuilder(self.request_adapter, self.path_parameters)

    def drive(self) -> drive_request_builder.DriveRequestBuilder:
        """
        Provides operations to manage the drive property of the microsoft.graph.user entity.
        """
        return drive_request_builder.DriveRequestBuilder(self.request_adapter, self.path_parameters)

    def drives(self) -> drives_request_builder.DrivesRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.user entity.
        """
        return drives_request_builder.DrivesRequestBuilder(self.request_adapter, self.path_parameters)

    def events(self) -> events_request_builder.EventsRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.user entity.
        """
        return events_request_builder.EventsRequestBuilder(self.request_adapter, self.path_parameters)

    def export_personal_data(self) -> export_personal_data_request_builder.ExportPersonalDataRequestBuilder:
        """
        Provides operations to call the exportPersonalData method.
        """
        return export_personal_data_request_builder.ExportPersonalDataRequestBuilder(self.request_adapter, self.path_parameters)

    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.user entity.
        """
        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)

    def find_meeting_times(self) -> find_meeting_times_request_builder.FindMeetingTimesRequestBuilder:
        """
        Provides operations to call the findMeetingTimes method.
        """
        return find_meeting_times_request_builder.FindMeetingTimesRequestBuilder(self.request_adapter, self.path_parameters)

    def followed_sites(self) -> followed_sites_request_builder.FollowedSitesRequestBuilder:
        """
        Provides operations to manage the followedSites property of the microsoft.graph.user entity.
        """
        return followed_sites_request_builder.FollowedSitesRequestBuilder(self.request_adapter, self.path_parameters)

    def get_mail_tips(self) -> get_mail_tips_request_builder.GetMailTipsRequestBuilder:
        """
        Provides operations to call the getMailTips method.
        """
        return get_mail_tips_request_builder.GetMailTipsRequestBuilder(self.request_adapter, self.path_parameters)

    def get_member_groups(self) -> get_member_groups_request_builder.GetMemberGroupsRequestBuilder:
        """
        Provides operations to call the getMemberGroups method.
        """
        return get_member_groups_request_builder.GetMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)

    def get_member_objects(self) -> get_member_objects_request_builder.GetMemberObjectsRequestBuilder:
        """
        Provides operations to call the getMemberObjects method.
        """
        return get_member_objects_request_builder.GetMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)

    def inference_classification(self) -> inference_classification_request_builder.InferenceClassificationRequestBuilder:
        """
        Provides operations to manage the inferenceClassification property of the microsoft.graph.user entity.
        """
        return inference_classification_request_builder.InferenceClassificationRequestBuilder(self.request_adapter, self.path_parameters)

    def insights(self) -> insights_request_builder.InsightsRequestBuilder:
        """
        Provides operations to manage the insights property of the microsoft.graph.user entity.
        """
        return insights_request_builder.InsightsRequestBuilder(self.request_adapter, self.path_parameters)

    def joined_teams(self) -> joined_teams_request_builder.JoinedTeamsRequestBuilder:
        """
        Provides operations to manage the joinedTeams property of the microsoft.graph.user entity.
        """
        return joined_teams_request_builder.JoinedTeamsRequestBuilder(self.request_adapter, self.path_parameters)

    def license_details(self) -> license_details_request_builder.LicenseDetailsRequestBuilder:
        """
        Provides operations to manage the licenseDetails property of the microsoft.graph.user entity.
        """
        return license_details_request_builder.LicenseDetailsRequestBuilder(self.request_adapter, self.path_parameters)

    def mail_folders(self) -> mail_folders_request_builder.MailFoldersRequestBuilder:
        """
        Provides operations to manage the mailFolders property of the microsoft.graph.user entity.
        """
        return mail_folders_request_builder.MailFoldersRequestBuilder(self.request_adapter, self.path_parameters)

    def managed_app_registrations(self) -> managed_app_registrations_request_builder.ManagedAppRegistrationsRequestBuilder:
        """
        Provides operations to manage the managedAppRegistrations property of the microsoft.graph.user entity.
        """
        return managed_app_registrations_request_builder.ManagedAppRegistrationsRequestBuilder(self.request_adapter, self.path_parameters)

    def managed_devices(self) -> managed_devices_request_builder.ManagedDevicesRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
        """
        return managed_devices_request_builder.ManagedDevicesRequestBuilder(self.request_adapter, self.path_parameters)

    def manager(self) -> manager_request_builder.ManagerRequestBuilder:
        """
        Provides operations to manage the manager property of the microsoft.graph.user entity.
        """
        return manager_request_builder.ManagerRequestBuilder(self.request_adapter, self.path_parameters)

    def member_of(self) -> member_of_request_builder.MemberOfRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.user entity.
        """
        return member_of_request_builder.MemberOfRequestBuilder(self.request_adapter, self.path_parameters)

    def messages(self) -> messages_request_builder.MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.user entity.
        """
        return messages_request_builder.MessagesRequestBuilder(self.request_adapter, self.path_parameters)

    def oauth2_permission_grants(self) -> oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the oauth2PermissionGrants property of the microsoft.graph.user entity.
        """
        return oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)

    def onenote(self) -> onenote_request_builder.OnenoteRequestBuilder:
        """
        Provides operations to manage the onenote property of the microsoft.graph.user entity.
        """
        return onenote_request_builder.OnenoteRequestBuilder(self.request_adapter, self.path_parameters)

    def online_meetings(self) -> online_meetings_request_builder.OnlineMeetingsRequestBuilder:
        """
        Provides operations to manage the onlineMeetings property of the microsoft.graph.user entity.
        """
        return online_meetings_request_builder.OnlineMeetingsRequestBuilder(self.request_adapter, self.path_parameters)

    def outlook(self) -> outlook_request_builder.OutlookRequestBuilder:
        """
        Provides operations to manage the outlook property of the microsoft.graph.user entity.
        """
        return outlook_request_builder.OutlookRequestBuilder(self.request_adapter, self.path_parameters)

    def owned_devices(self) -> owned_devices_request_builder.OwnedDevicesRequestBuilder:
        """
        Provides operations to manage the ownedDevices property of the microsoft.graph.user entity.
        """
        return owned_devices_request_builder.OwnedDevicesRequestBuilder(self.request_adapter, self.path_parameters)

    def owned_objects(self) -> owned_objects_request_builder.OwnedObjectsRequestBuilder:
        """
        Provides operations to manage the ownedObjects property of the microsoft.graph.user entity.
        """
        return owned_objects_request_builder.OwnedObjectsRequestBuilder(self.request_adapter, self.path_parameters)

    def people(self) -> people_request_builder.PeopleRequestBuilder:
        """
        Provides operations to manage the people property of the microsoft.graph.user entity.
        """
        return people_request_builder.PeopleRequestBuilder(self.request_adapter, self.path_parameters)

    def photo(self) -> photo_request_builder.PhotoRequestBuilder:
        """
        Provides operations to manage the photo property of the microsoft.graph.user entity.
        """
        return photo_request_builder.PhotoRequestBuilder(self.request_adapter, self.path_parameters)

    def photos(self) -> photos_request_builder.PhotosRequestBuilder:
        """
        Provides operations to manage the photos property of the microsoft.graph.user entity.
        """
        return photos_request_builder.PhotosRequestBuilder(self.request_adapter, self.path_parameters)

    def planner(self) -> planner_request_builder.PlannerRequestBuilder:
        """
        Provides operations to manage the planner property of the microsoft.graph.user entity.
        """
        return planner_request_builder.PlannerRequestBuilder(self.request_adapter, self.path_parameters)

    def presence(self) -> presence_request_builder.PresenceRequestBuilder:
        """
        Provides operations to manage the presence property of the microsoft.graph.user entity.
        """
        return presence_request_builder.PresenceRequestBuilder(self.request_adapter, self.path_parameters)

    def registered_devices(self) -> registered_devices_request_builder.RegisteredDevicesRequestBuilder:
        """
        Provides operations to manage the registeredDevices property of the microsoft.graph.user entity.
        """
        return registered_devices_request_builder.RegisteredDevicesRequestBuilder(self.request_adapter, self.path_parameters)

    def remove_all_devices_from_management(self) -> remove_all_devices_from_management_request_builder.RemoveAllDevicesFromManagementRequestBuilder:
        """
        Provides operations to call the removeAllDevicesFromManagement method.
        """
        return remove_all_devices_from_management_request_builder.RemoveAllDevicesFromManagementRequestBuilder(self.request_adapter, self.path_parameters)

    def reprocess_license_assignment(self) -> reprocess_license_assignment_request_builder.ReprocessLicenseAssignmentRequestBuilder:
        """
        Provides operations to call the reprocessLicenseAssignment method.
        """
        return reprocess_license_assignment_request_builder.ReprocessLicenseAssignmentRequestBuilder(self.request_adapter, self.path_parameters)

    def restore(self) -> restore_request_builder.RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        return restore_request_builder.RestoreRequestBuilder(self.request_adapter, self.path_parameters)

    def revoke_sign_in_sessions(self) -> revoke_sign_in_sessions_request_builder.RevokeSignInSessionsRequestBuilder:
        """
        Provides operations to call the revokeSignInSessions method.
        """
        return revoke_sign_in_sessions_request_builder.RevokeSignInSessionsRequestBuilder(self.request_adapter, self.path_parameters)

    def scoped_role_member_of(self) -> scoped_role_member_of_request_builder.ScopedRoleMemberOfRequestBuilder:
        """
        Provides operations to manage the scopedRoleMemberOf property of the microsoft.graph.user entity.
        """
        return scoped_role_member_of_request_builder.ScopedRoleMemberOfRequestBuilder(self.request_adapter, self.path_parameters)

    def send_mail(self) -> send_mail_request_builder.SendMailRequestBuilder:
        """
        Provides operations to call the sendMail method.
        """
        return send_mail_request_builder.SendMailRequestBuilder(self.request_adapter, self.path_parameters)

    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.user entity.
        """
        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)

    def teamwork(self) -> teamwork_request_builder.TeamworkRequestBuilder:
        """
        Provides operations to manage the teamwork property of the microsoft.graph.user entity.
        """
        return teamwork_request_builder.TeamworkRequestBuilder(self.request_adapter, self.path_parameters)

    def todo(self) -> todo_request_builder.TodoRequestBuilder:
        """
        Provides operations to manage the todo property of the microsoft.graph.user entity.
        """
        return todo_request_builder.TodoRequestBuilder(self.request_adapter, self.path_parameters)

    def transitive_member_of(self) -> transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.user entity.
        """
        return transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder(self.request_adapter, self.path_parameters)

    def translate_exchange_ids(self) -> translate_exchange_ids_request_builder.TranslateExchangeIdsRequestBuilder:
        """
        Provides operations to call the translateExchangeIds method.
        """
        return translate_exchange_ids_request_builder.TranslateExchangeIdsRequestBuilder(self.request_adapter, self.path_parameters)

    def wipe_managed_app_registrations_by_device_tag(self) -> wipe_managed_app_registrations_by_device_tag_request_builder.WipeManagedAppRegistrationsByDeviceTagRequestBuilder:
        """
        Provides operations to call the wipeManagedAppRegistrationsByDeviceTag method.
        """
        return wipe_managed_app_registrations_by_device_tag_request_builder.WipeManagedAppRegistrationsByDeviceTagRequestBuilder(self.request_adapter, self.path_parameters)

    def activities_by_id(self,id: str) -> user_activity_item_request_builder.UserActivityItemRequestBuilder:
        """
        Provides operations to manage the activities property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: user_activity_item_request_builder.UserActivityItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userActivity%2Did"] = id
        return user_activity_item_request_builder.UserActivityItemRequestBuilder(self.request_adapter, url_tpl_params)

    def agreement_acceptances_by_id(self,id: str) -> agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder:
        """
        Provides operations to manage the agreementAcceptances property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreementAcceptance%2Did"] = id
        return agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder(self.request_adapter, url_tpl_params)

    def app_role_assignments_by_id(self,id: str) -> app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the appRoleAssignments property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["appRoleAssignment%2Did"] = id
        return app_role_assignment_item_request_builder.AppRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)

    def calendar_groups_by_id(self,id: str) -> calendar_group_item_request_builder.CalendarGroupItemRequestBuilder:
        """
        Provides operations to manage the calendarGroups property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: calendar_group_item_request_builder.CalendarGroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["calendarGroup%2Did"] = id
        return calendar_group_item_request_builder.CalendarGroupItemRequestBuilder(self.request_adapter, url_tpl_params)

    def calendars_by_id(self,id: str) -> calendar_item_request_builder.CalendarItemRequestBuilder:
        """
        Provides operations to manage the calendars property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: calendar_item_request_builder.CalendarItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["calendar%2Did"] = id
        return calendar_item_request_builder.CalendarItemRequestBuilder(self.request_adapter, url_tpl_params)

    def calendar_view_by_id(self,id: str) -> event_item_request_builder.EventItemRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: event_item_request_builder.EventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event%2Did"] = id
        return event_item_request_builder.EventItemRequestBuilder(self.request_adapter, url_tpl_params)

    def chats_by_id(self,id: str) -> chat_item_request_builder.ChatItemRequestBuilder:
        """
        Provides operations to manage the chats property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: chat_item_request_builder.ChatItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["chat%2Did"] = id
        return chat_item_request_builder.ChatItemRequestBuilder(self.request_adapter, url_tpl_params)

    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UserItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

    def contact_folders_by_id(self,id: str) -> contact_folder_item_request_builder.ContactFolderItemRequestBuilder:
        """
        Provides operations to manage the contactFolders property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: contact_folder_item_request_builder.ContactFolderItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["contactFolder%2Did"] = id
        return contact_folder_item_request_builder.ContactFolderItemRequestBuilder(self.request_adapter, url_tpl_params)

    def contacts_by_id(self,id: str) -> contact_item_request_builder.ContactItemRequestBuilder:
        """
        Provides operations to manage the contacts property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: contact_item_request_builder.ContactItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["contact%2Did"] = id
        return contact_item_request_builder.ContactItemRequestBuilder(self.request_adapter, url_tpl_params)

    def create_delete_request_information(self,request_configuration: Optional[UserItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete user.   When deleted, user resources are moved to a temporary container and can be restored within 30 days.  After that time, they are permanently deleted.  To learn more, see deletedItems.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info

    def created_objects_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the createdObjects property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)

    def create_get_request_information(self,request_configuration: Optional[UserItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of user object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info

    def create_patch_request_information(self,body: Optional[user.User] = None, request_configuration: Optional[UserItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a user object. Not all properties can be updated by Member or Guest users with their default permissions without Administrator roles. Compare member and guest default permissions to see properties they can manage.
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info

    async def delete(self,request_configuration: Optional[UserItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete user.   When deleted, user resources are moved to a temporary container and can be restored within 30 days.  After that time, they are permanently deleted.  To learn more, see deletedItems.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)

    def device_management_troubleshooting_events_by_id(self,id: str) -> device_management_troubleshooting_event_item_request_builder.DeviceManagementTroubleshootingEventItemRequestBuilder:
        """
        Provides operations to manage the deviceManagementTroubleshootingEvents property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_troubleshooting_event_item_request_builder.DeviceManagementTroubleshootingEventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementTroubleshootingEvent%2Did"] = id
        return device_management_troubleshooting_event_item_request_builder.DeviceManagementTroubleshootingEventItemRequestBuilder(self.request_adapter, url_tpl_params)

    def direct_reports_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the directReports property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)

    def drives_by_id(self,id: str) -> drive_item_request_builder.DriveItemRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_request_builder.DriveItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["drive%2Did"] = id
        return drive_item_request_builder.DriveItemRequestBuilder(self.request_adapter, url_tpl_params)

    def events_by_id(self,id: str) -> event_item_request_builder.EventItemRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: event_item_request_builder.EventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event%2Did"] = id
        return event_item_request_builder.EventItemRequestBuilder(self.request_adapter, url_tpl_params)

    def extensions_by_id(self,id: str) -> extension_item_request_builder.ExtensionItemRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: extension_item_request_builder.ExtensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["extension%2Did"] = id
        return extension_item_request_builder.ExtensionItemRequestBuilder(self.request_adapter, url_tpl_params)

    def followed_sites_by_id(self,id: str) -> site_item_request_builder.SiteItemRequestBuilder:
        """
        Provides operations to manage the followedSites property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: site_item_request_builder.SiteItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["site%2Did"] = id
        return site_item_request_builder.SiteItemRequestBuilder(self.request_adapter, url_tpl_params)

    async def get(self,request_configuration: Optional[UserItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[user.User]:
        """
        Retrieve the properties and relationships of user object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[user.User]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, user.User, response_handler, error_mapping)

    def get_managed_app_diagnostic_statuses(self,) -> get_managed_app_diagnostic_statuses_request_builder.GetManagedAppDiagnosticStatusesRequestBuilder:
        """
        Provides operations to call the getManagedAppDiagnosticStatuses method.
        Returns: get_managed_app_diagnostic_statuses_request_builder.GetManagedAppDiagnosticStatusesRequestBuilder
        """
        return get_managed_app_diagnostic_statuses_request_builder.GetManagedAppDiagnosticStatusesRequestBuilder(self.request_adapter, self.path_parameters)

    def get_managed_app_policies(self,) -> get_managed_app_policies_request_builder.GetManagedAppPoliciesRequestBuilder:
        """
        Provides operations to call the getManagedAppPolicies method.
        Returns: get_managed_app_policies_request_builder.GetManagedAppPoliciesRequestBuilder
        """
        return get_managed_app_policies_request_builder.GetManagedAppPoliciesRequestBuilder(self.request_adapter, self.path_parameters)

    def joined_teams_by_id(self,id: str) -> team_item_request_builder.TeamItemRequestBuilder:
        """
        Provides operations to manage the joinedTeams property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: team_item_request_builder.TeamItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["team%2Did"] = id
        return team_item_request_builder.TeamItemRequestBuilder(self.request_adapter, url_tpl_params)

    def license_details_by_id(self,id: str) -> license_details_item_request_builder.LicenseDetailsItemRequestBuilder:
        """
        Provides operations to manage the licenseDetails property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: license_details_item_request_builder.LicenseDetailsItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["licenseDetails%2Did"] = id
        return license_details_item_request_builder.LicenseDetailsItemRequestBuilder(self.request_adapter, url_tpl_params)

    def mail_folders_by_id(self,id: str) -> mail_folder_item_request_builder.MailFolderItemRequestBuilder:
        """
        Provides operations to manage the mailFolders property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: mail_folder_item_request_builder.MailFolderItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mailFolder%2Did"] = id
        return mail_folder_item_request_builder.MailFolderItemRequestBuilder(self.request_adapter, url_tpl_params)

    def managed_app_registrations_by_id(self,id: str) -> managed_app_registration_item_request_builder.ManagedAppRegistrationItemRequestBuilder:
        """
        Provides operations to manage the managedAppRegistrations property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_app_registration_item_request_builder.ManagedAppRegistrationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedAppRegistration%2Did"] = id
        return managed_app_registration_item_request_builder.ManagedAppRegistrationItemRequestBuilder(self.request_adapter, url_tpl_params)

    def managed_devices_by_id(self,id: str) -> managed_device_item_request_builder.ManagedDeviceItemRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_item_request_builder.ManagedDeviceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDevice%2Did"] = id
        return managed_device_item_request_builder.ManagedDeviceItemRequestBuilder(self.request_adapter, url_tpl_params)

    def member_of_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)

    def messages_by_id(self,id: str) -> message_item_request_builder.MessageItemRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: message_item_request_builder.MessageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["message%2Did"] = id
        return message_item_request_builder.MessageItemRequestBuilder(self.request_adapter, url_tpl_params)

    def oauth2_permission_grants_by_id(self,id: str) -> o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder:
        """
        Provides operations to manage the oauth2PermissionGrants property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["oAuth2PermissionGrant%2Did"] = id
        return o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder(self.request_adapter, url_tpl_params)

    def online_meetings_by_id(self,id: str) -> online_meeting_item_request_builder.OnlineMeetingItemRequestBuilder:
        """
        Provides operations to manage the onlineMeetings property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: online_meeting_item_request_builder.OnlineMeetingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onlineMeeting%2Did"] = id
        return online_meeting_item_request_builder.OnlineMeetingItemRequestBuilder(self.request_adapter, url_tpl_params)

    def owned_devices_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the ownedDevices property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)

    def owned_objects_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the ownedObjects property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)

    async def patch(self,body: Optional[user.User] = None, request_configuration: Optional[UserItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[user.User]:
        """
        Update the properties of a user object. Not all properties can be updated by Member or Guest users with their default permissions without Administrator roles. Compare member and guest default permissions to see properties they can manage.
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[user.User]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, user.User, response_handler, error_mapping)

    def people_by_id(self,id: str) -> person_item_request_builder.PersonItemRequestBuilder:
        """
        Provides operations to manage the people property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: person_item_request_builder.PersonItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["person%2Did"] = id
        return person_item_request_builder.PersonItemRequestBuilder(self.request_adapter, url_tpl_params)

    def photos_by_id(self,id: str) -> profile_photo_item_request_builder.ProfilePhotoItemRequestBuilder:
        """
        Provides operations to manage the photos property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: profile_photo_item_request_builder.ProfilePhotoItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["profilePhoto%2Did"] = id
        return profile_photo_item_request_builder.ProfilePhotoItemRequestBuilder(self.request_adapter, url_tpl_params)

    def registered_devices_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the registeredDevices property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)

    def reminder_view_with_start_date_time_with_end_date_time(self,end_date_time: Optional[str] = None, start_date_time: Optional[str] = None) -> reminder_view_with_start_date_time_with_end_date_time_request_builder.ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the reminderView method.
        Args:
            EndDateTime: Usage: EndDateTime='{EndDateTime}'
            StartDateTime: Usage: StartDateTime='{StartDateTime}'
        Returns: reminder_view_with_start_date_time_with_end_date_time_request_builder.ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise Exception("end_date_time cannot be undefined")
        if start_date_time is None:
            raise Exception("start_date_time cannot be undefined")
        return reminder_view_with_start_date_time_with_end_date_time_request_builder.ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, EndDateTime, StartDateTime)

    def scoped_role_member_of_by_id(self,id: str) -> scoped_role_membership_item_request_builder.ScopedRoleMembershipItemRequestBuilder:
        """
        Provides operations to manage the scopedRoleMemberOf property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: scoped_role_membership_item_request_builder.ScopedRoleMembershipItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["scopedRoleMembership%2Did"] = id
        return scoped_role_membership_item_request_builder.ScopedRoleMembershipItemRequestBuilder(self.request_adapter, url_tpl_params)

    def transitive_member_of_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.user entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)

    @dataclass
    class UserItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UserItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of user object.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name

    
    @dataclass
    class UserItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UserItemRequestBuilder.UserItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UserItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

