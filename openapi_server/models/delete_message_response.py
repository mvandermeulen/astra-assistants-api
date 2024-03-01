# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class DeleteMessageResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DeleteMessageResponse - a model defined in OpenAPI

        id: The id of this DeleteMessageResponse.
        deleted: The deleted of this DeleteMessageResponse.
        object: The object of this DeleteMessageResponse.
    """

    id: str = Field(alias="id")
    deleted: bool = Field(alias="deleted")
    object: str = Field(alias="object")

DeleteMessageResponse.update_forward_refs()