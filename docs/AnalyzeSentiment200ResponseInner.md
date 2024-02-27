# AnalyzeSentiment200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sentiment** | **str** | The sentiment of the text, either POSITIVE or NEGATIVE. | [optional] 
**score** | **float** | The confidence score of the sentiment analysis. | [optional] 

## Example

```python
from deep_api.models.analyze_sentiment200_response_inner import AnalyzeSentiment200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyzeSentiment200ResponseInner from a JSON string
analyze_sentiment200_response_inner_instance = AnalyzeSentiment200ResponseInner.from_json(json)
# print the JSON string representation of the object
print AnalyzeSentiment200ResponseInner.to_json()

# convert the object into a dict
analyze_sentiment200_response_inner_dict = analyze_sentiment200_response_inner_instance.to_dict()
# create an instance of AnalyzeSentiment200ResponseInner from a dict
analyze_sentiment200_response_inner_form_dict = analyze_sentiment200_response_inner.from_dict(analyze_sentiment200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


