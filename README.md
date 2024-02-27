# deep-api-client
Our AI API service offers a seamless and efficient solution for businesses and individuals seeking to leverage the power of artificial intelligence without the complexity and cost of managing their infrastructure. By choosing DeepAPI, you eliminate the need to invest in and maintain expensive servers and GPUs, as we provide a robust, scalable, cloud-based platform operating out of multiple data centers that ensures high performance, low latency and reliability. Our on-demand service allows you to pay only for what you use, ensuring a cost-effective approach to accessing cutting-edge AI capabilities. Get your API key today at https://deepapi.ai

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Deep-API/deep-api-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Deep-API/deep-api-python.git`)

Then import the package:
```python
import deep_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import deep_api
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
        # Analyzes the sentiment of the input text.
        api_response = api_instance.analyze_sentiment(request_body)
        print("The response of TextApi->analyze_sentiment:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TextApi->analyze_sentiment: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.deepapi.ai/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TextApi* | [**analyze_sentiment**](docs/TextApi.md#analyze_sentiment) | **POST** /text/sentiment-analysis | Analyzes the sentiment of the input text.
*TextApi* | [**chat**](docs/TextApi.md#chat) | **POST** /text/chat | Generate chat-like responses using an LLM (Large Language Model) which can perform a wide variety of tasks.
*TextApi* | [**detect_language**](docs/TextApi.md#detect_language) | **POST** /text/language-detection | Detects the language of the input text.
*TextApi* | [**translate_text**](docs/TextApi.md#translate_text) | **POST** /text/translation | Translates the input text into the target language.


## Documentation For Models

 - [AnalyzeSentiment200ResponseInner](docs/AnalyzeSentiment200ResponseInner.md)
 - [Chat200Response](docs/Chat200Response.md)
 - [ChatRequest](docs/ChatRequest.md)
 - [ChatRequestChatsInnerInner](docs/ChatRequestChatsInnerInner.md)
 - [Error](docs/Error.md)
 - [TranslateTextRequestInner](docs/TranslateTextRequestInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="api_key"></a>
### api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header


## Author

contact@deepapi.ai

