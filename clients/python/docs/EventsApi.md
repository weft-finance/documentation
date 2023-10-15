# openapi_client.EventsApi

All URIs are relative to *https://events.goweft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_events**](EventsApi.md#send_events) | **POST** /events | Submit a batch of events for ingestion


# **send_events**
> send_events(send_events_request)

Submit a batch of events for ingestion

Use this endpoint to send an array of events for processing and storage. Make sure to comply with the request schema for each event.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.send_events_request import SendEventsRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://events.goweft.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://events.goweft.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EventsApi(api_client)
    send_events_request = openapi_client.SendEventsRequest() # SendEventsRequest | An array of events following the EventInput schema. This request body should be included in the PUT request to '/events' Up to 1000 events or a total payload max size of 256KB 

    try:
        # Submit a batch of events for ingestion
        api_instance.send_events(send_events_request)
    except Exception as e:
        print("Exception when calling EventsApi->send_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_events_request** | [**SendEventsRequest**](SendEventsRequest.md)| An array of events following the EventInput schema. This request body should be included in the PUT request to &#39;/events&#39; Up to 1000 events or a total payload max size of 256KB  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

