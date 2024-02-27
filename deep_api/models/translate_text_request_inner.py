# coding: utf-8

"""
    DeepAPI

    Our AI API service offers a seamless and efficient solution for businesses and individuals seeking to leverage the power of artificial intelligence without the complexity and cost of managing their infrastructure. By choosing DeepAPI, you eliminate the need to invest in and maintain expensive servers and GPUs, as we provide a robust, scalable, cloud-based platform operating out of multiple data centers that ensures high performance, low latency and reliability. Our on-demand service allows you to pay only for what you use, ensuring a cost-effective approach to accessing cutting-edge AI capabilities. Get your API key today at https://deepapi.ai

    The version of the OpenAPI document: 1.0.0
    Contact: contact@deepapi.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TranslateTextRequestInner(BaseModel):
    """
    TranslateTextRequestInner
    """ # noqa: E501
    text: StrictStr = Field(description="The text to translate.")
    source_language: Optional[StrictStr] = Field(default=None, description="The source language code of the text using the two letter ISO 639-1 language code. If not provided, the language will be automatically detected.")
    target_language: StrictStr = Field(description="The target language code using the two letter ISO 639-1 language code to translate the text into.")
    __properties: ClassVar[List[str]] = ["text", "source_language", "target_language"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TranslateTextRequestInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TranslateTextRequestInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "text": obj.get("text"),
            "source_language": obj.get("source_language"),
            "target_language": obj.get("target_language")
        })
        return _obj

