# coding: utf-8

"""
    DeepAPI

    Our AI API service offers a seamless and efficient solution for businesses and individuals seeking to leverage the power of artificial intelligence without the complexity and cost of managing their infrastructure. By choosing DeepAPI, you eliminate the need to invest in and maintain expensive servers and GPUs, as we provide a robust, scalable, cloud-based platform operating out of multiple data centers that ensures high performance, low latency and reliability. Our on-demand service allows you to pay only for what you use, ensuring a cost-effective approach to accessing cutting-edge AI capabilities. Get your API key today at https://deepapi.ai

    The version of the OpenAPI document: 1.0.0
    Contact: contact@deepapi.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from deep_api.models.translate_text_request_inner import TranslateTextRequestInner

class TestTranslateTextRequestInner(unittest.TestCase):
    """TranslateTextRequestInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TranslateTextRequestInner:
        """Test TranslateTextRequestInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TranslateTextRequestInner`
        """
        model = TranslateTextRequestInner()
        if include_optional:
            return TranslateTextRequestInner(
                text = 'Hello, how are you?',
                source_language = 'en',
                target_language = 'es'
            )
        else:
            return TranslateTextRequestInner(
                text = 'Hello, how are you?',
                target_language = 'es',
        )
        """

    def testTranslateTextRequestInner(self):
        """Test TranslateTextRequestInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
