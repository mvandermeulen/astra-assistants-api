# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.thread_object import ThreadObject


class ListThreadsResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ListThreadsResponse - a model defined in OpenAPI

        object: The object of this ListThreadsResponse.
        data: The data of this ListThreadsResponse.
        first_id: The first_id of this ListThreadsResponse.
        last_id: The last_id of this ListThreadsResponse.
        has_more: The has_more of this ListThreadsResponse.
    """

    object: str = Field(alias="object")
    data: List[ThreadObject] = Field(alias="data")
    first_id: str = Field(alias="first_id")
    last_id: str = Field(alias="last_id")
    has_more: bool = Field(alias="has_more")

ListThreadsResponse.update_forward_refs()