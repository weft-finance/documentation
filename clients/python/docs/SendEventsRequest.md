# SendEventsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[EventInput]**](EventInput.md) |  | 

## Example

```python
from openapi_client.models.send_events_request import SendEventsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendEventsRequest from a JSON string
send_events_request_instance = SendEventsRequest.from_json(json)
# print the JSON string representation of the object
print SendEventsRequest.to_json()

# convert the object into a dict
send_events_request_dict = send_events_request_instance.to_dict()
# create an instance of SendEventsRequest from a dict
send_events_request_form_dict = send_events_request.from_dict(send_events_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


