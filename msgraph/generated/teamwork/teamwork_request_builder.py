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

from ..models import teamwork
from ..models.o_data_errors import o_data_error
from .send_activity_notification_to_recipients import send_activity_notification_to_recipients_request_builder
from .workforce_integrations import workforce_integrations_request_builder
from .workforce_integrations.item import workforce_integration_item_request_builder

class TeamworkRequestBuilder():
    """
    Provides operations to manage the teamwork singleton.
    """
    def send_activity_notification_to_recipients(self) -> send_activity_notification_to_recipients_request_builder.SendActivityNotificationToRecipientsRequestBuilder:
        """
        Provides operations to call the sendActivityNotificationToRecipients method.
        """
        return send_activity_notification_to_recipients_request_builder.SendActivityNotificationToRecipientsRequestBuilder(self.request_adapter, self.path_parameters)

    def workforce_integrations(self) -> workforce_integrations_request_builder.WorkforceIntegrationsRequestBuilder:
        """
        Provides operations to manage the workforceIntegrations property of the microsoft.graph.teamwork entity.
        """
        return workforce_integrations_request_builder.WorkforceIntegrationsRequestBuilder(self.request_adapter, self.path_parameters)

    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TeamworkRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/teamwork{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

    def create_get_request_information(self,request_configuration: Optional[TeamworkRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get teamwork
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

    def create_patch_request_information(self,body: Optional[teamwork.Teamwork] = None, request_configuration: Optional[TeamworkRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update teamwork
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

    async def get(self,request_configuration: Optional[TeamworkRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[teamwork.Teamwork]:
        """
        Get teamwork
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[teamwork.Teamwork]
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
        return await self.request_adapter.send_async(request_info, teamwork.Teamwork, response_handler, error_mapping)

    async def patch(self,body: Optional[teamwork.Teamwork] = None, request_configuration: Optional[TeamworkRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[teamwork.Teamwork]:
        """
        Update teamwork
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[teamwork.Teamwork]
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
        return await self.request_adapter.send_async(request_info, teamwork.Teamwork, response_handler, error_mapping)

    def workforce_integrations_by_id(self,id: str) -> workforce_integration_item_request_builder.WorkforceIntegrationItemRequestBuilder:
        """
        Provides operations to manage the workforceIntegrations property of the microsoft.graph.teamwork entity.
        Args:
            id: Unique identifier of the item
        Returns: workforce_integration_item_request_builder.WorkforceIntegrationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workforceIntegration%2Did"] = id
        return workforce_integration_item_request_builder.WorkforceIntegrationItemRequestBuilder(self.request_adapter, url_tpl_params)

    @dataclass
    class TeamworkRequestBuilderGetQueryParameters():
        """
        Get teamwork
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
    class TeamworkRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TeamworkRequestBuilder.TeamworkRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TeamworkRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

