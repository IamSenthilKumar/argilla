#  coding=utf-8
#  Copyright 2021-present, the Recognai S.L. team.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class FeedbackDatasetModel(BaseModel):
    id: UUID
    name: str = Field(regex="^(?!-|_)[a-zA-Z0-9-_ ]+$")
    guidelines: str = None
    status: str = None
    workspace_id: str = None
    created_at: datetime = None
    last_updated: datetime = None


class FeedbackResponseModel(BaseModel):
    id: UUID
    values: Dict[str, Any]
    status: Literal["submitted", "missing", "discarded"]
    user_id: UUID
    inserted_at: datetime
    updated_at: datetime


class FeedbackItemModel(BaseModel):
    id: UUID
    fields: Dict[str, Any]
    external_id: Optional[str] = None
    responses: List[FeedbackResponseModel] = []
    inserted_at: datetime
    updated_at: datetime


class FeedbackRecordsModel(BaseModel):
    items: List[FeedbackItemModel]
    total: Optional[int] = None

    class Config:
        fields = {"total": {"exclude": True}}
