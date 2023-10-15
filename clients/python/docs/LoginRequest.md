# LoginRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** | The refresh token issued previously during the authentication process. It is required to obtain a new access token. | 

## Example

```python
from openapi_client.models.login_request import LoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoginRequest from a JSON string
login_request_instance = LoginRequest.from_json(json)
# print the JSON string representation of the object
print LoginRequest.to_json()

# convert the object into a dict
login_request_dict = login_request_instance.to_dict()
# create an instance of LoginRequest from a dict
login_request_form_dict = login_request.from_dict(login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


