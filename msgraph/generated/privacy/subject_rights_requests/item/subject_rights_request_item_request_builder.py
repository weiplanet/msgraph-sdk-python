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

from ....models import subject_rights_request
from ....models.o_data_errors import o_data_error
from .get_final_attachment import get_final_attachment_request_builder
from .get_final_report import get_final_report_request_builder
from .notes import notes_request_builder
from .notes.item import authored_note_item_request_builder
from .team import team_request_builder

class SubjectRightsRequestItemRequestBuilder():
    """
    Provides operations to manage the subjectRightsRequests property of the microsoft.graph.privacy entity.
    """
    def notes(self) -> notes_request_builder.NotesRequestBuilder:
        """
        Provides operations to manage the notes property of the microsoft.graph.subjectRightsRequest entity.
        """
        return notes_request_builder.NotesRequestBuilder(self.request_adapter, self.path_parameters)

    def team(self) -> team_request_builder.TeamRequestBuilder:
        """
        Provides operations to manage the team property of the microsoft.graph.subjectRightsRequest entity.
        """
        return team_request_builder.TeamRequestBuilder(self.request_adapter, self.path_parameters)

    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SubjectRightsRequestItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/privacy/subjectRightsRequests/{subjectRightsRequest%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

    def create_delete_request_information(self,request_configuration: Optional[SubjectRightsRequestItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property subjectRightsRequests for privacy
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

    def create_get_request_information(self,request_configuration: Optional[SubjectRightsRequestItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get subjectRightsRequests from privacy
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

    def create_patch_request_information(self,body: Optional[subject_rights_request.SubjectRightsRequest] = None, request_configuration: Optional[SubjectRightsRequestItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property subjectRightsRequests in privacy
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

    async def delete(self,request_configuration: Optional[SubjectRightsRequestItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property subjectRightsRequests for privacy
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

    async def get(self,request_configuration: Optional[SubjectRightsRequestItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[subject_rights_request.SubjectRightsRequest]:
        """
        Get subjectRightsRequests from privacy
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[subject_rights_request.SubjectRightsRequest]
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
        return await self.request_adapter.send_async(request_info, subject_rights_request.SubjectRightsRequest, response_handler, error_mapping)

    def get_final_attachment(self,) -> get_final_attachment_request_builder.GetFinalAttachmentRequestBuilder:
        """
        Provides operations to call the getFinalAttachment method.
        Returns: get_final_attachment_request_builder.GetFinalAttachmentRequestBuilder
        """
        return get_final_attachment_request_builder.GetFinalAttachmentRequestBuilder(self.request_adapter, self.path_parameters)

    def get_final_report(self,) -> get_final_report_request_builder.GetFinalReportRequestBuilder:
        """
        Provides operations to call the getFinalReport method.
        Returns: get_final_report_request_builder.GetFinalReportRequestBuilder
        """
        return get_final_report_request_builder.GetFinalReportRequestBuilder(self.request_adapter, self.path_parameters)

    def notes_by_id(self,id: str) -> authored_note_item_request_builder.AuthoredNoteItemRequestBuilder:
        """
        Provides operations to manage the notes property of the microsoft.graph.subjectRightsRequest entity.
        Args:
            id: Unique identifier of the item
        Returns: authored_note_item_request_builder.AuthoredNoteItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["authoredNote%2Did"] = id
        return authored_note_item_request_builder.AuthoredNoteItemRequestBuilder(self.request_adapter, url_tpl_params)

    async def patch(self,body: Optional[subject_rights_request.SubjectRightsRequest] = None, request_configuration: Optional[SubjectRightsRequestItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[subject_rights_request.SubjectRightsRequest]:
        """
        Update the navigation property subjectRightsRequests in privacy
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[subject_rights_request.SubjectRightsRequest]
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
        return await self.request_adapter.send_async(request_info, subject_rights_request.SubjectRightsRequest, response_handler, error_mapping)

    @dataclass
    class SubjectRightsRequestItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SubjectRightsRequestItemRequestBuilderGetQueryParameters():
        """
        Get subjectRightsRequests from privacy
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
    class SubjectRightsRequestItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SubjectRightsRequestItemRequestBuilder.SubjectRightsRequestItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SubjectRightsRequestItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

