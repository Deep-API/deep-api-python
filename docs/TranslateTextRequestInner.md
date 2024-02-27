# TranslateTextRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text to translate. | 
**source_language** | **str** | The source language code of the text using the two letter ISO 639-1 language code. If not provided, the language will be automatically detected. | [optional] 
**target_language** | **str** | The target language code using the two letter ISO 639-1 language code to translate the text into. | 

## Example

```python
from deep_api.models.translate_text_request_inner import TranslateTextRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateTextRequestInner from a JSON string
translate_text_request_inner_instance = TranslateTextRequestInner.from_json(json)
# print the JSON string representation of the object
print TranslateTextRequestInner.to_json()

# convert the object into a dict
translate_text_request_inner_dict = translate_text_request_inner_instance.to_dict()
# create an instance of TranslateTextRequestInner from a dict
translate_text_request_inner_form_dict = translate_text_request_inner.from_dict(translate_text_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


