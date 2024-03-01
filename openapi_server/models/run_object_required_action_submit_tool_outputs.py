# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.run_tool_call_object import RunToolCallObject


class RunObjectRequiredActionSubmitToolOutputs(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RunObjectRequiredActionSubmitToolOutputs - a model defined in OpenAPI

        tool_calls: The tool_calls of this RunObjectRequiredActionSubmitToolOutputs.
    """

    tool_calls: List[RunToolCallObject] = Field(alias="tool_calls")

RunObjectRequiredActionSubmitToolOutputs.update_forward_refs()