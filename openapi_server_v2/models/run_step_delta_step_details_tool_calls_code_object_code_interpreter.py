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
from openapi_server_v2.models.run_step_delta_step_details_tool_calls_code_object_code_interpreter_outputs_inner import RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreter(BaseModel):
    """
    The Code Interpreter tool call definition.
    """ # noqa: E501
    input: Optional[StrictStr] = Field(default=None, description="The input to the Code Interpreter tool call.")
    outputs: Optional[List[RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner]] = Field(default=None, description="The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.")
    __properties: ClassVar[List[str]] = ["input", "outputs"]

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
        """Create an instance of RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreter from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in outputs (list)
        _items = []
        if self.outputs:
            for _item in self.outputs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['outputs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "input": obj.get("input"),
            "outputs": [RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.from_dict(_item) for _item in obj.get("outputs")] if obj.get("outputs") is not None else None
        })
        return _obj

