# openapi_client.model.event_input.EventInput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**customerAlias** | str,  | str,  | A pseudonymous or otherwise obfuscated identifier uniquely assigned to each customer. | 
**name** | str,  | str,  | The distinctive label assigned to an event, serving as a critical identifier for categorizing and pricing events within the system&#x27;s backend infrastructure. | 
**timestamp** | str, datetime,  | str,  | The temporal marker denoting the exact moment of event occurrence. | value must conform to RFC-3339 date-time
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A schema-less JSON object encapsulating miscellaneous attributes and metrics associated with the event. | [optional] 
**ref** | str,  | str,  | A universally unique identifier (UUID) or other form of high-entropy string serving as an immutable reference for each event entry. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

A schema-less JSON object encapsulating miscellaneous attributes and metrics associated with the event.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A schema-less JSON object encapsulating miscellaneous attributes and metrics associated with the event. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

