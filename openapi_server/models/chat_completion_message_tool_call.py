# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.chat_completion_message_tool_call_function import ChatCompletionMessageToolCallFunction


class ChatCompletionMessageToolCall(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ChatCompletionMessageToolCall - a model defined in OpenAPI

        id: The id of this ChatCompletionMessageToolCall.
        type: The type of this ChatCompletionMessageToolCall.
        function: The function of this ChatCompletionMessageToolCall.
    """

    id: str = Field(alias="id")
    type: str = Field(alias="type")
    function: ChatCompletionMessageToolCallFunction = Field(alias="function")

ChatCompletionMessageToolCall.update_forward_refs()