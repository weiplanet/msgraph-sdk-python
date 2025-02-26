from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, Union

from ...models.call_records import call_record, call_record_collection_response
from ...models.o_data_errors import o_data_error
from .count import count_request_builder
from .get_direct_routing_calls_with_from_date_time_with_to_date_time import get_direct_routing_calls_with_from_date_time_with_to_date_time_request_builder
from .get_pstn_calls_with_from_date_time_with_to_date_time import get_pstn_calls_with_from_date_time_with_to_date_time_request_builder

class CallRecordsRequestBuilder():
    """
    Provides operations to manage the callRecords property of the microsoft.graph.cloudCommunications entity.
    """
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)

    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CallRecordsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/communications/callRecords{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

    def create_get_request_information(self,request_configuration: Optional[CallRecordsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get callRecords from communications
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

    def create_post_request_information(self,body: Optional[call_record.CallRecord] = None, request_configuration: Optional[CallRecordsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to callRecords for communications
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
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info

    async def get(self,request_configuration: Optional[CallRecordsRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[call_record_collection_response.CallRecordCollectionResponse]:
        """
        Get callRecords from communications
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[call_record_collection_response.CallRecordCollectionResponse]
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
        return await self.request_adapter.send_async(request_info, call_record_collection_response.CallRecordCollectionResponse, response_handler, error_mapping)

    def get_direct_routing_calls_with_from_date_time_with_to_date_time(self,from_date_time: Optional[datetime] = None, to_date_time: Optional[datetime] = None) -> get_direct_routing_calls_with_from_date_time_with_to_date_time_request_builder.GetDirectRoutingCallsWithFromDateTimeWithToDateTimeRequestBuilder:
        """
        Provides operations to call the getDirectRoutingCalls method.
        Args:
            fromDateTime: Usage: fromDateTime={fromDateTime}
            toDateTime: Usage: toDateTime={toDateTime}
        Returns: get_direct_routing_calls_with_from_date_time_with_to_date_time_request_builder.GetDirectRoutingCallsWithFromDateTimeWithToDateTimeRequestBuilder
        """
        if from_date_time is None:
            raise Exception("from_date_time cannot be undefined")
        if to_date_time is None:
            raise Exception("to_date_time cannot be undefined")
        return get_direct_routing_calls_with_from_date_time_with_to_date_time_request_builder.GetDirectRoutingCallsWithFromDateTimeWithToDateTimeRequestBuilder(self.request_adapter, self.path_parameters, fromDateTime, toDateTime)

    def get_pstn_calls_with_from_date_time_with_to_date_time(self,from_date_time: Optional[datetime] = None, to_date_time: Optional[datetime] = None) -> get_pstn_calls_with_from_date_time_with_to_date_time_request_builder.GetPstnCallsWithFromDateTimeWithToDateTimeRequestBuilder:
        """
        Provides operations to call the getPstnCalls method.
        Args:
            fromDateTime: Usage: fromDateTime={fromDateTime}
            toDateTime: Usage: toDateTime={toDateTime}
        Returns: get_pstn_calls_with_from_date_time_with_to_date_time_request_builder.GetPstnCallsWithFromDateTimeWithToDateTimeRequestBuilder
        """
        if from_date_time is None:
            raise Exception("from_date_time cannot be undefined")
        if to_date_time is None:
            raise Exception("to_date_time cannot be undefined")
        return get_pstn_calls_with_from_date_time_with_to_date_time_request_builder.GetPstnCallsWithFromDateTimeWithToDateTimeRequestBuilder(self.request_adapter, self.path_parameters, fromDateTime, toDateTime)

    async def post(self,body: Optional[call_record.CallRecord] = None, request_configuration: Optional[CallRecordsRequestBuilderPostRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[call_record.CallRecord]:
        """
        Create new navigation property to callRecords for communications
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[call_record.CallRecord]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_post_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, call_record.CallRecord, response_handler, error_mapping)

    @dataclass
    class CallRecordsRequestBuilderGetQueryParameters():
        """
        Get callRecords from communications
        """
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name

    
    @dataclass
    class CallRecordsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CallRecordsRequestBuilder.CallRecordsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class CallRecordsRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

