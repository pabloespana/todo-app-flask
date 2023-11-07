from enum import Enum
from dataclasses import dataclass


class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    """Task Model"""

    id: int
    title: str
    description: str
    due_date: str
    status: TaskStatus


@dataclass
class TaskCreate:
    title: str
    description: str
    due_date: str
    status: TaskStatus


@dataclass
class TaskCreateOut(Task):
    ...


@dataclass
class TaskUpdate(TaskCreate):
    ...


@dataclass
class TaskUpdateOut(Task):
    ...
