# coding: utf-8

# flake8: noqa

"""
    DeepAPI

    Our AI API service offers a seamless and efficient solution for businesses and individuals seeking to leverage the power of artificial intelligence without the complexity and cost of managing their infrastructure. By choosing DeepAPI, you eliminate the need to invest in and maintain expensive servers and GPUs, as we provide a robust, scalable, cloud-based platform operating out of multiple data centers that ensures high performance, low latency and reliability. Our on-demand service allows you to pay only for what you use, ensuring a cost-effective approach to accessing cutting-edge AI capabilities. Get your API key today at https://deepapi.ai

    The version of the OpenAPI document: 1.0.0
    Contact: contact@deepapi.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "2.17.0"

# import apis into sdk package
from deep_api.api.text_api import TextApi

# import ApiClient
from deep_api.api_response import ApiResponse
from deep_api.api_client import ApiClient
from deep_api.configuration import Configuration
from deep_api.exceptions import OpenApiException
from deep_api.exceptions import ApiTypeError
from deep_api.exceptions import ApiValueError
from deep_api.exceptions import ApiKeyError
from deep_api.exceptions import ApiAttributeError
from deep_api.exceptions import ApiException

# import models into sdk package
from deep_api.models.analyze_sentiment200_response_inner import AnalyzeSentiment200ResponseInner
from deep_api.models.chat200_response import Chat200Response
from deep_api.models.chat_request import ChatRequest
from deep_api.models.chat_request_chats_inner_inner import ChatRequestChatsInnerInner
from deep_api.models.error import Error
from deep_api.models.translate_text_request_inner import TranslateTextRequestInner
