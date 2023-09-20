<a name="__pageTop"></a>
# openapi_client.apis.tags.auth_api.AuthApi

All URIs are relative to *https://events.goweft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](#login) | **post** /login | Login by obtaining a new access token

# **login**
<a name="login"></a>
> LoginResponseSchema login(login_request_schema)

Login by obtaining a new access token

This endpoint is designed to acquire a temporary access token. Submit the auth token in the request body to obtain a new access token. Use this new token for subsequent API calls. Token is set to expire every hour. 

### Example

```python
import openapi_client
from openapi_client.apis.tags import auth_api
from openapi_client.model.login_request_schema import LoginRequestSchema
from openapi_client.model.login_response_schema import LoginResponseSchema
from pprint import pprint
# Defining the host is optional and defaults to https://events.goweft.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://events.goweft.com"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example passing only required values which don't have defaults set
    body = LoginRequestSchema(
        refresh_token="refresh_token_example",
    )
    try:
        # Login by obtaining a new access token
        api_response = api_instance.login(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthApi->login: %s\n" % e)
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
[**LoginRequestSchema**](../../models/LoginRequestSchema.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#login.ApiResponseFor200) | response contains a new access token
400 | [ApiResponseFor400](#login.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#login.ApiResponseFor500) | Internal Server Error

#### login.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LoginResponseSchema**](../../models/LoginResponseSchema.md) |  | 


#### login.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### login.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

