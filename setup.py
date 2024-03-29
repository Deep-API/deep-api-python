# coding: utf-8

"""
    DeepAPI

    Our AI API service offers a seamless and efficient solution for businesses and individuals seeking to leverage the power of artificial intelligence without the complexity and cost of managing their infrastructure. By choosing DeepAPI, you eliminate the need to invest in and maintain expensive servers and GPUs, as we provide a robust, scalable, cloud-based platform operating out of multiple data centers that ensures high performance, low latency and reliability. Our on-demand service allows you to pay only for what you use, ensuring a cost-effective approach to accessing cutting-edge AI capabilities. Get your API key today at https://deepapi.ai

    The version of the OpenAPI document: 1.0.0
    Contact: contact@deepapi.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "deep-api-client"
VERSION = "2.17.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="DeepAPI",
    author="DeepAPI Support",
    author_email="contact@deepapi.ai",
    url="https://github.com/Deep-API/deep-api-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "DeepAPI"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type='text/markdown',
    long_description="""\
    Our AI API service offers a seamless and efficient solution for businesses and individuals seeking to leverage the power of artificial intelligence without the complexity and cost of managing their infrastructure. By choosing DeepAPI, you eliminate the need to invest in and maintain expensive servers and GPUs, as we provide a robust, scalable, cloud-based platform operating out of multiple data centers that ensures high performance, low latency and reliability. Our on-demand service allows you to pay only for what you use, ensuring a cost-effective approach to accessing cutting-edge AI capabilities. Get your API key today at https://deepapi.ai
    """,  # noqa: E501
    package_data={"deep_api": ["py.typed"]},
)
