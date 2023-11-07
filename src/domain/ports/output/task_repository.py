from typing import List
from abc import ABC, abstractmethod
from src.domain.task import (
    Task,
    TaskCreate,
    TaskCreateOut,
    TaskUpdate,
    TaskUpdateOut,
)


class TaskRepository(ABC):
    @abstractmethod
    def list(self) -> List[Task]:
        ...

    @abstractmethod
    def find(self, task_id: int) -> Task:
        ...

    @abstractmethod
    def create(self, task: TaskCreate) -> TaskCreateOut:
        ...

    @abstractmethod
    def update(self, task_id: int, task: TaskUpdate) -> TaskUpdateOut:
        ...

    @abstractmethod
    def delete(self, task_id: int) -> None:
        ...
