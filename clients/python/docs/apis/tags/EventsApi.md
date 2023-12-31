<a name="__pageTop"></a>
# openapi_client.apis.tags.events_api.EventsApi

All URIs are relative to *https://events.goweft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_events**](#send_events) | **post** /events | Submit a batch of events for ingestion

# **send_events**
<a name="send_events"></a>
> send_events(send_events_request_schema)

Submit a batch of events for ingestion

Use this endpoint to send an array of events for processing and storage. Make sure to comply with the request schema for each event.

### Example

```python
import openapi_client
from openapi_client.apis.tags import events_api
from openapi_client.model.send_events_request_schema import SendEventsRequestSchema
from pprint import pprint
# Defining the host is optional and defaults to https://events.goweft.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://events.goweft.com"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SendEventsRequestSchema(
        events=[{"name":"UserSignup","timestamp":"2023-09-13T18:25:43.511Z","customerAlias":"customer_12345","data":{"key1":"api_processing_in_milliseconds","key2":"api_url"},"ref":"4f6cf35x-2c4y-483z-a0a9-158621f77a21"}],
    )
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
Type | Description  | Notes
------------- | ------------- | -------------
[**SendEventsRequestSchema**](../../models/SendEventsRequestSchema.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#send_events.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#send_events.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#send_events.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#send_events.ApiResponseFor500) | Internal Server Error

#### send_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### send_events.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### send_events.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### send_events.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

