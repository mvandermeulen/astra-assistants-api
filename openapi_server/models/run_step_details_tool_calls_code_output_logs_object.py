# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class RunStepDetailsToolCallsCodeOutputLogsObject(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RunStepDetailsToolCallsCodeOutputLogsObject - a model defined in OpenAPI

        type: The type of this RunStepDetailsToolCallsCodeOutputLogsObject.
        logs: The logs of this RunStepDetailsToolCallsCodeOutputLogsObject.
    """

    type: str = Field(alias="type")
    logs: str = Field(alias="logs")

RunStepDetailsToolCallsCodeOutputLogsObject.update_forward_refs()