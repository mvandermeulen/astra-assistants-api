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
from typing_extensions import Annotated
from openapi_server_v2.models.create_assistant_request_tool_resources_file_search_vector_stores_inner import CreateAssistantRequestToolResourcesFileSearchVectorStoresInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateThreadRequestToolResourcesFileSearch(BaseModel):
    """
    CreateThreadRequestToolResourcesFileSearch
    """ # noqa: E501
    vector_store_ids: Optional[Annotated[List[StrictStr], Field(max_length=1)]] = Field(default=None, description="The [vector store](/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread. ")
    vector_stores: Optional[Annotated[List[CreateAssistantRequestToolResourcesFileSearchVectorStoresInner], Field(max_length=1)]] = Field(default=None, description="A helper to create a [vector store](/docs/api-reference/vector-stores/object) with file_ids and attach it to this thread. There can be a maximum of 1 vector store attached to the thread. ")
    __properties: ClassVar[List[str]] = ["vector_store_ids", "vector_stores"]

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
        """Create an instance of CreateThreadRequestToolResourcesFileSearch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in vector_stores (list)
        _items = []
        if self.vector_stores:
            for _item in self.vector_stores:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vector_stores'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateThreadRequestToolResourcesFileSearch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "vector_store_ids": obj.get("vector_store_ids"),
            "vector_stores": [CreateAssistantRequestToolResourcesFileSearchVectorStoresInner.from_dict(_item) for _item in obj.get("vector_stores")] if obj.get("vector_stores") is not None else None
        })
        return _obj


