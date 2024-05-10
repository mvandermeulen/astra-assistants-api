# coding: utf-8

"""
    OpenAI API

    The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server_v2.models.message_object_attachments_inner_tools_inner import MessageObjectAttachmentsInnerToolsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MessageObjectAttachmentsInner(BaseModel):
    """
    MessageObjectAttachmentsInner
    """ # noqa: E501
    file_id: Optional[StrictStr] = Field(default=None, description="The ID of the file to attach to the message.")
    tools: Optional[List[MessageObjectAttachmentsInnerToolsInner]] = Field(default=None, description="The tools to add this file to.")
    __properties: ClassVar[List[str]] = ["file_id", "tools"]

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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MessageObjectAttachmentsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tools (list)
        _items = []
        if self.tools:
            for _item in self.tools:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tools'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MessageObjectAttachmentsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "file_id": obj.get("file_id"),
            "tools": [MessageObjectAttachmentsInnerToolsInner.from_dict(_item) for _item in obj.get("tools")] if obj.get("tools") is not None else None
        })
        return _obj


