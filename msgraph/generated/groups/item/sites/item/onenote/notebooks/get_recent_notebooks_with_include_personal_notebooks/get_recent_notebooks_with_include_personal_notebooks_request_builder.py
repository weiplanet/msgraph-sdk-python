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

from . import get_recent_notebooks_with_include_personal_notebooks_response
from ........models.o_data_errors import o_data_error

class GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilder():
    """
    Provides operations to call the getRecentNotebooks method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, include_personal_notebooks: Optional[bool] = None) -> None:
        """
        Instantiates a new GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilder and sets the default values.
        Args:
            includePersonalNotebooks: Usage: includePersonalNotebooks={includePersonalNotebooks}
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/onenote/notebooks/microsoft.graph.getRecentNotebooks(includePersonalNotebooks={includePersonalNotebooks}){?%24top,%24skip,%24search,%24filter,%24count}"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params[""] = includePersonalNotebooks
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

    def create_get_request_information(self,request_configuration: Optional[GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function getRecentNotebooks
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

    async def get(self,request_configuration: Optional[GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[get_recent_notebooks_with_include_personal_notebooks_response.GetRecentNotebooksWithIncludePersonalNotebooksResponse]:
        """
        Invoke function getRecentNotebooks
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[get_recent_notebooks_with_include_personal_notebooks_response.GetRecentNotebooksWithIncludePersonalNotebooksResponse]
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
        return await self.request_adapter.send_async(request_info, get_recent_notebooks_with_include_personal_notebooks_response.GetRecentNotebooksWithIncludePersonalNotebooksResponse, response_handler, error_mapping)

    @dataclass
    class GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilderGetQueryParameters():
        """
        Invoke function getRecentNotebooks
        """
        # Include count of items
        count: Optional[bool] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "count":
                return "%24count"
            if original_name == "filter":
                return "%24filter"
            if original_name == "search":
                return "%24search"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name

    
    @dataclass
    class GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilder.GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilderGetQueryParameters] = None

    

