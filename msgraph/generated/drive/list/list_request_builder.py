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

from ...models import list
from ...models.o_data_errors import o_data_error
from .columns import columns_request_builder
from .columns.item import column_definition_item_request_builder
from .content_types import content_types_request_builder
from .content_types.item import content_type_item_request_builder
from .drive import drive_request_builder
from .items import items_request_builder
from .items.item import list_item_item_request_builder
from .operations import operations_request_builder
from .operations.item import rich_long_running_operation_item_request_builder
from .subscriptions import subscriptions_request_builder
from .subscriptions.item import subscription_item_request_builder

class ListRequestBuilder():
    """
    Provides operations to manage the list property of the microsoft.graph.drive entity.
    """
    def columns(self) -> columns_request_builder.ColumnsRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.list entity.
        """
        return columns_request_builder.ColumnsRequestBuilder(self.request_adapter, self.path_parameters)

    def content_types(self) -> content_types_request_builder.ContentTypesRequestBuilder:
        """
        Provides operations to manage the contentTypes property of the microsoft.graph.list entity.
        """
        return content_types_request_builder.ContentTypesRequestBuilder(self.request_adapter, self.path_parameters)

    def drive(self) -> drive_request_builder.DriveRequestBuilder:
        """
        Provides operations to manage the drive property of the microsoft.graph.list entity.
        """
        return drive_request_builder.DriveRequestBuilder(self.request_adapter, self.path_parameters)

    def items(self) -> items_request_builder.ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.list entity.
        """
        return items_request_builder.ItemsRequestBuilder(self.request_adapter, self.path_parameters)

    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.list entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)

    def subscriptions(self) -> subscriptions_request_builder.SubscriptionsRequestBuilder:
        """
        Provides operations to manage the subscriptions property of the microsoft.graph.list entity.
        """
        return subscriptions_request_builder.SubscriptionsRequestBuilder(self.request_adapter, self.path_parameters)

    def columns_by_id(self,id: str) -> column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.list entity.
        Args:
            id: Unique identifier of the item
        Returns: column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["columnDefinition%2Did"] = id
        return column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)

    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ListRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drive/list{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

    def content_types_by_id(self,id: str) -> content_type_item_request_builder.ContentTypeItemRequestBuilder:
        """
        Provides operations to manage the contentTypes property of the microsoft.graph.list entity.
        Args:
            id: Unique identifier of the item
        Returns: content_type_item_request_builder.ContentTypeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["contentType%2Did"] = id
        return content_type_item_request_builder.ContentTypeItemRequestBuilder(self.request_adapter, url_tpl_params)

    def create_delete_request_information(self,request_configuration: Optional[ListRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property list for drive
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

    def create_get_request_information(self,request_configuration: Optional[ListRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        For drives in SharePoint, the underlying document library list. Read-only. Nullable.
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

    def create_patch_request_information(self,body: Optional[list.List] = None, request_configuration: Optional[ListRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property list in drive
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

    async def delete(self,request_configuration: Optional[ListRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property list for drive
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

    async def get(self,request_configuration: Optional[ListRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[list.List]:
        """
        For drives in SharePoint, the underlying document library list. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[list.List]
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
        return await self.request_adapter.send_async(request_info, list.List, response_handler, error_mapping)

    def items_by_id(self,id: str) -> list_item_item_request_builder.ListItemItemRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.list entity.
        Args:
            id: Unique identifier of the item
        Returns: list_item_item_request_builder.ListItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["listItem%2Did"] = id
        return list_item_item_request_builder.ListItemItemRequestBuilder(self.request_adapter, url_tpl_params)

    def operations_by_id(self,id: str) -> rich_long_running_operation_item_request_builder.RichLongRunningOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.list entity.
        Args:
            id: Unique identifier of the item
        Returns: rich_long_running_operation_item_request_builder.RichLongRunningOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["richLongRunningOperation%2Did"] = id
        return rich_long_running_operation_item_request_builder.RichLongRunningOperationItemRequestBuilder(self.request_adapter, url_tpl_params)

    async def patch(self,body: Optional[list.List] = None, request_configuration: Optional[ListRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[list.List]:
        """
        Update the navigation property list in drive
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[list.List]
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
        return await self.request_adapter.send_async(request_info, list.List, response_handler, error_mapping)

    def subscriptions_by_id(self,id: str) -> subscription_item_request_builder.SubscriptionItemRequestBuilder:
        """
        Provides operations to manage the subscriptions property of the microsoft.graph.list entity.
        Args:
            id: Unique identifier of the item
        Returns: subscription_item_request_builder.SubscriptionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["subscription%2Did"] = id
        return subscription_item_request_builder.SubscriptionItemRequestBuilder(self.request_adapter, url_tpl_params)

    @dataclass
    class ListRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ListRequestBuilderGetQueryParameters():
        """
        For drives in SharePoint, the underlying document library list. Read-only. Nullable.
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
    class ListRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ListRequestBuilder.ListRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ListRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

