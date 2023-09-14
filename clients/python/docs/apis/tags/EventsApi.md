<a name="__pageTop"></a>
# openapi_client.apis.tags.events_api.EventsApi

All URIs are relative to *https://api.goweft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refresh_user**](#refresh_user) | **post** /refreshToken | Refreshes the user&#x27;s access token
[**send_events**](#send_events) | **put** /events | Submit a batch of events for ingestion

# **refresh_user**
<a name="refresh_user"></a>
> RefreshTokenResponse refresh_user(refresh_token_input)

Refreshes the user's access token

This endpoint is designed to refresh an expired or expiring JWT access token. Submit the refresh token in the request body to obtain a new access token. Use this new token for subsequent API calls. Token is set to expire every hour. 

### Example

```python
import openapi_client
from openapi_client.apis.tags import events_api
from openapi_client.model.refresh_token_input import RefreshTokenInput
from openapi_client.model.refresh_token_response import RefreshTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.goweft.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.goweft.com"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)

    # example passing only required values which don't have defaults set
    body = RefreshTokenInput(
        refresh_token="refresh_token_example",
    )
    try:
        # Refreshes the user's access token
        api_response = api_instance.refresh_user(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventsApi->refresh_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RefreshTokenInput**](../../models/RefreshTokenInput.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#refresh_user.ApiResponseFor200) | response contains a new access token

#### refresh_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RefreshTokenResponse**](../../models/RefreshTokenResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **send_events**
<a name="send_events"></a>
> send_events(event_input)

Submit a batch of events for ingestion

Use this endpoint to send an array of events for processing and storage. Make sure to comply with the request schema for each event.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import openapi_client
from openapi_client.apis.tags import events_api
from openapi_client.model.event_input import EventInput
from pprint import pprint
# Defining the host is optional and defaults to https://api.goweft.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.goweft.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)

    # example passing only required values which don't have defaults set
    body = [{"name":"UserSignup","timestamp":"2023-09-13T18:25:43.511Z","customerAlias":"customer_12345","data":{"key1":"api_processing_in_milliseconds","key2":"api_url"},"ref":"4f6cf35x-2c4y-483z-a0a9-158621f77a21"}]
    try:
        # Submit a batch of events for ingestion
        api_response = api_instance.send_events(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling EventsApi->send_events: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EventInput**]({{complexTypePrefix}}EventInput.md) | [**EventInput**]({{complexTypePrefix}}EventInput.md) | [**EventInput**]({{complexTypePrefix}}EventInput.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#send_events.ApiResponseFor200) | OK

#### send_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

