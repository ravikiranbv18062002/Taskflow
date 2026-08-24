from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    project_id: UUID
    assignee_id: UUID | None = None
    status: TaskStatus = TaskStatus.TODO
    due_date: datetime | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    assignee_id: UUID | None = None
    status: TaskStatus | None = None
    due_date: datetime | None = None


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str | None
    project_id: UUID
    assignee_id: UUID | None
    status: TaskStatus
    due_date: datetime | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True