# EventInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The distinctive label assigned to an event, serving as a critical identifier for categorizing and pricing events within the system&#39;s backend infrastructure. | 
**timestamp** | **datetime** | The temporal marker denoting the exact moment of event occurrence. | 
**customer_alias** | **str** | A pseudonymous or otherwise obfuscated identifier uniquely assigned to each customer. | 
**data** | **object** | A schema-less JSON object encapsulating miscellaneous attributes and metrics associated with the event. | [optional] 
**ref** | **str** | A universally unique identifier (UUID) or other form of high-entropy string serving as an immutable reference for each event entry. | [optional] 

## Example

```python
from openapi_client.models.event_input import EventInput

# TODO update the JSON string below
json = "{}"
# create an instance of EventInput from a JSON string
event_input_instance = EventInput.from_json(json)
# print the JSON string representation of the object
print EventInput.to_json()

# convert the object into a dict
event_input_dict = event_input_instance.to_dict()
# create an instance of EventInput from a dict
event_input_form_dict = event_input.from_dict(event_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


