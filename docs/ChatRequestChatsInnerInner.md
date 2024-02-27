# ChatRequestChatsInnerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role of the speaker, either \&quot;user\&quot; or \&quot;assistant\&quot;. | 
**content** | **str** | The text content of the message. To simulate a conversation, the input should alternate between the user and the assistant. | 

## Example

```python
from deep_api.models.chat_request_chats_inner_inner import ChatRequestChatsInnerInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChatRequestChatsInnerInner from a JSON string
chat_request_chats_inner_inner_instance = ChatRequestChatsInnerInner.from_json(json)
# print the JSON string representation of the object
print ChatRequestChatsInnerInner.to_json()

# convert the object into a dict
chat_request_chats_inner_inner_dict = chat_request_chats_inner_inner_instance.to_dict()
# create an instance of ChatRequestChatsInnerInner from a dict
chat_request_chats_inner_inner_form_dict = chat_request_chats_inner_inner.from_dict(chat_request_chats_inner_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


