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




from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_server_v2.models.assistants_api_response_format_option import AssistantsApiResponseFormatOption
from openapi_server_v2.models.assistants_api_tool_choice_option import AssistantsApiToolChoiceOption
from openapi_server_v2.models.create_run_request_model import CreateRunRequestModel
from openapi_server_v2.models.create_thread_and_run_request_tool_resources import CreateThreadAndRunRequestToolResources
from openapi_server_v2.models.create_thread_and_run_request_tools_inner import CreateThreadAndRunRequestToolsInner
from openapi_server_v2.models.create_thread_request import CreateThreadRequest
from openapi_server_v2.models.truncation_object import TruncationObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateThreadAndRunRequest(BaseModel):
    """
    CreateThreadAndRunRequest
    """ # noqa: E501
    assistant_id: StrictStr = Field(description="The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run.")
    thread: Optional[CreateThreadRequest] = None
    model: Optional[CreateRunRequestModel] = None
    instructions: Optional[StrictStr] = Field(default=None, description="Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis.")
    tools: Optional[Annotated[List[CreateThreadAndRunRequestToolsInner], Field(max_length=20)]] = Field(default=None, description="Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.")
    tool_resources: Optional[CreateThreadAndRunRequestToolResources] = None
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long. ")
    temperature: Optional[Union[Annotated[float, Field(le=2, strict=True, ge=0)], Annotated[int, Field(le=2, strict=True, ge=0)]]] = Field(default=1, description="What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. ")
    top_p: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=1, description="An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or temperature but not both. ")
    stream: Optional[StrictBool] = Field(default=None, description="If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message. ")
    max_prompt_tokens: Optional[Annotated[int, Field(strict=True, ge=256)]] = Field(default=None, description="The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info. ")
    max_completion_tokens: Optional[Annotated[int, Field(strict=True, ge=256)]] = Field(default=None, description="The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info. ")
    truncation_strategy: Optional[TruncationObject] = None
    tool_choice: Optional[AssistantsApiToolChoiceOption] = None
    response_format: Optional[AssistantsApiResponseFormatOption] = None
    __properties: ClassVar[List[str]] = ["assistant_id", "thread", "model", "instructions", "tools", "tool_resources", "metadata", "temperature", "top_p", "stream", "max_prompt_tokens", "max_completion_tokens", "truncation_strategy", "tool_choice", "response_format"]

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
        """Create an instance of CreateThreadAndRunRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of thread
        if self.thread:
            _dict['thread'] = self.thread.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tools (list)
        _items = []
        if self.tools:
            for _item in self.tools:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tools'] = _items
        # override the default output from pydantic by calling `to_dict()` of tool_resources
        if self.tool_resources:
            _dict['tool_resources'] = self.tool_resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of truncation_strategy
        if self.truncation_strategy:
            _dict['truncation_strategy'] = self.truncation_strategy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tool_choice
        if self.tool_choice:
            _dict['tool_choice'] = self.tool_choice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of response_format
        if self.response_format:
            _dict['response_format'] = self.response_format.to_dict()
        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if instructions (nullable) is None
        # and model_fields_set contains the field
        if self.instructions is None and "instructions" in self.model_fields_set:
            _dict['instructions'] = None

        # set to None if tools (nullable) is None
        # and model_fields_set contains the field
        if self.tools is None and "tools" in self.model_fields_set:
            _dict['tools'] = None

        # set to None if tool_resources (nullable) is None
        # and model_fields_set contains the field
        if self.tool_resources is None and "tool_resources" in self.model_fields_set:
            _dict['tool_resources'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if temperature (nullable) is None
        # and model_fields_set contains the field
        if self.temperature is None and "temperature" in self.model_fields_set:
            _dict['temperature'] = None

        # set to None if top_p (nullable) is None
        # and model_fields_set contains the field
        if self.top_p is None and "top_p" in self.model_fields_set:
            _dict['top_p'] = None

        # set to None if stream (nullable) is None
        # and model_fields_set contains the field
        if self.stream is None and "stream" in self.model_fields_set:
            _dict['stream'] = None

        # set to None if max_prompt_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.max_prompt_tokens is None and "max_prompt_tokens" in self.model_fields_set:
            _dict['max_prompt_tokens'] = None

        # set to None if max_completion_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.max_completion_tokens is None and "max_completion_tokens" in self.model_fields_set:
            _dict['max_completion_tokens'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateThreadAndRunRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assistant_id": obj.get("assistant_id"),
            "thread": CreateThreadRequest.from_dict(obj.get("thread")) if obj.get("thread") is not None else None,
            "model": CreateRunRequestModel.from_dict(obj.get("model")) if obj.get("model") is not None else None,
            "instructions": obj.get("instructions"),
            "tools": [CreateThreadAndRunRequestToolsInner.from_dict(_item) for _item in obj.get("tools")] if obj.get("tools") is not None else None,
            "tool_resources": CreateThreadAndRunRequestToolResources.from_dict(obj.get("tool_resources")) if obj.get("tool_resources") is not None else None,
            "metadata": obj.get("metadata"),
            "temperature": obj.get("temperature") if obj.get("temperature") is not None else 1,
            "top_p": obj.get("top_p") if obj.get("top_p") is not None else 1,
            "stream": obj.get("stream"),
            "max_prompt_tokens": obj.get("max_prompt_tokens"),
            "max_completion_tokens": obj.get("max_completion_tokens"),
            "truncation_strategy": TruncationObject.from_dict(obj.get("truncation_strategy")) if obj.get("truncation_strategy") is not None else None,
            "tool_choice": AssistantsApiToolChoiceOption.from_dict(obj.get("tool_choice")) if obj.get("tool_choice") is not None else None,
            "response_format": AssistantsApiResponseFormatOption.from_dict(obj.get("response_format")) if obj.get("response_format") is not None else None
        })
        return _obj


