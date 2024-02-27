# Chat200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to the generated chat-like responses. | [optional] 

## Example

```python
from deep_api.models.chat200_response import Chat200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Chat200Response from a JSON string
chat200_response_instance = Chat200Response.from_json(json)
# print the JSON string representation of the object
print Chat200Response.to_json()

# convert the object into a dict
chat200_response_dict = chat200_response_instance.to_dict()
# create an instance of Chat200Response from a dict
chat200_response_form_dict = chat200_response.from_dict(chat200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


