from typing import List
import inject
from src.domain.ports.input.task_service import TaskService
from src.domain.ports.output.task_repository import TaskRepository
from src.domain.task import (
    Task,
    TaskCreate,
    TaskCreateOut,
    TaskUpdate,
    TaskUpdateOut,
)


class TaskServiceImpl(TaskService):
    @inject.autoparams()
    def __init__(self, task_repository: TaskRepository) -> None:
        self._task_repository = task_repository

    def list(self) -> List[Task]:
        return self._task_repository.list()

    def find(self, task_id: int) -> Task:
        return self._task_repository.find(task_id)

    def create(self, task: TaskCreate) -> TaskCreateOut:
        return self._task_repository.create(task)

    def update(self, task_id: int, task: TaskUpdate) -> TaskUpdateOut:
        return self._task_repository.update(task_id, task)

    def delete(self, task_id: int) -> None:
        return self._task_repository.delete(task_id)
