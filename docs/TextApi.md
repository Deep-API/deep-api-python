# deep_api.TextApi

All URIs are relative to *https://api.deepapi.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_sentiment**](TextApi.md#analyze_sentiment) | **POST** /text/sentiment-analysis | Analyzes the sentiment of the input text.
[**chat**](TextApi.md#chat) | **POST** /text/chat | Generate chat-like responses using an LLM (Large Language Model) which can perform a wide variety of tasks.
[**detect_language**](TextApi.md#detect_language) | **POST** /text/language-detection | Detects the language of the input text.
[**translate_text**](TextApi.md#translate_text) | **POST** /text/translation | Translates the input text into the target language.


# **analyze_sentiment**
> List[AnalyzeSentiment200ResponseInner] analyze_sentiment(request_body)

Analyzes the sentiment of the input text.

Analyzes the sentiment of the input text.

### Example

* Api Key Authentication (api_key):

```python
import deep_api
from deep_api.models.analyze_sentiment200_response_inner import AnalyzeSentiment200ResponseInner
from deep_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deepapi.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = deep_api.Configuration(
    host = "https://api.deepapi.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with deep_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deep_api.TextApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Analyzes the sentiment of the input text.
        api_response = api_instance.analyze_sentiment(request_body)
        print("The response of TextApi->analyze_sentiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextApi->analyze_sentiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

[**List[AnalyzeSentiment200ResponseInner]**](AnalyzeSentiment200ResponseInner.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the sentiment analysis results. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat**
> Chat200Response chat(chat_request)

Generate chat-like responses using an LLM (Large Language Model) which can perform a wide variety of tasks.

Generate chat-like responses to input text. This API allows a large language model (LLM) to interpret and respond to various queries, simulating a natural conversation. It's beneficial for businesses in various ways. <br><br> For customer service, it can provide quick, automated responses to common inquiries, significantly reducing wait times and improving customer satisfaction. Content creation aids in generating ideas, drafting articles, composing emails, and streamlining the creative process. For data mining, an LLM can sift through vast amounts of text, summarising key points and offering insights by answering specific questions, thereby aiding decision-making. Furthermore, educational platforms can be used to create interactive learning experiences, answering student queries in real time. <br><br> The versatility of this API makes it a valuable tool across numerous sectors, enhancing efficiency, engagement and workflow automation. 

### Example

* Api Key Authentication (api_key):

```python
import deep_api
from deep_api.models.chat200_response import Chat200Response
from deep_api.models.chat_request import ChatRequest
from deep_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deepapi.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = deep_api.Configuration(
    host = "https://api.deepapi.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with deep_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deep_api.TextApi(api_client)
    chat_request = {"model":"llama-2-7b-chat","chats":[[{"role":"user","content":"How many megapixels is the camera in this description? The camera is 12MP and is the same as the one in the iPhone 12 Pro."},{"role":"assistant","content":"The camera has a 12MP camera."},{"role":"user","content":"Just tell me the number of MP"},{"role":"assistant","content":"12"},{"role":"user","content":"What is the make if the phone?"}],[{"role":"user","content":"Write me a letter to my boss asking for a pay rise."}],[{"role":"user","content":"Complete this sentence: One way to end all wars and human suffering is..."}]]} # ChatRequest | 

    try:
        # Generate chat-like responses using an LLM (Large Language Model) which can perform a wide variety of tasks.
        api_response = api_instance.chat(chat_request)
        print("The response of TextApi->chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextApi->chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_request** | [**ChatRequest**](ChatRequest.md)|  | 

### Return type

[**Chat200Response**](Chat200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeepAPI chat API is designed to generate chat-style responses, which can be accessed through a link. This link remains active for 24 hours, after which it expires, and you won&#39;t be able to access the responses anymore. The responses are delivered in a JSON array containing all the necessary details, such as the speaker&#39;s role and message content. Usually, these responses are generated within seconds after you make a request. However, it may take longer to generate the responses during peak hours. Therefore, it is recommended that you check the link after a few seconds to see if the response has been generated. You can do this by polling the URL and checking the response&#39;s status. It is important to note that the link cannot be accessed after 24 hours, so it&#39;s best to download or save the responses as soon as possible. This method allows for better scalability; you may batch many chat generations and then poll each for the result 🚀 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_language**
> List[str] detect_language(request_body)

Detects the language of the input text.

Detects the language of the input text.

### Example

* Api Key Authentication (api_key):

```python
import deep_api
from deep_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deepapi.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = deep_api.Configuration(
    host = "https://api.deepapi.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with deep_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deep_api.TextApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Detects the language of the input text.
        api_response = api_instance.detect_language(request_body)
        print("The response of TextApi->detect_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextApi->detect_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the detected language. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_text**
> List[str] translate_text(translate_text_request_inner)

Translates the input text into the target language.

Translates the input text into the target language.

### Example

* Api Key Authentication (api_key):

```python
import deep_api
from deep_api.models.translate_text_request_inner import TranslateTextRequestInner
from deep_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deepapi.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = deep_api.Configuration(
    host = "https://api.deepapi.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with deep_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deep_api.TextApi(api_client)
    translate_text_request_inner = [deep_api.TranslateTextRequestInner()] # List[TranslateTextRequestInner] | 

    try:
        # Translates the input text into the target language.
        api_response = api_instance.translate_text(translate_text_request_inner)
        print("The response of TextApi->translate_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextApi->translate_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_text_request_inner** | [**List[TranslateTextRequestInner]**](TranslateTextRequestInner.md)|  | 

### Return type

**List[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the translated text. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

