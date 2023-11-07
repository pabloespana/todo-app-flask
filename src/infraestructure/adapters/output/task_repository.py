from typing import List, Optional, Any
import logging
from src import get_env_var
from src.domain.task import (
    Task,
    TaskCreate,
    TaskCreateOut,
    TaskUpdate,
    TaskUpdateOut,
)
from dataclasses import asdict
from sqlalchemy import create_engine, insert, update, delete, func
from sqlalchemy.orm import Session
from src.domain.ports.output.task_repository import TaskRepository
from src.infraestructure.entities.task_entity import TaskEntity


class TaskPostgresRepository(TaskRepository):
    def __init__(self) -> None:
        self.engine = create_engine(get_env_var("DATABASE_URL")).connect()

    def list(self) -> List[Task]:
        with Session(self.engine) as session:
            tasks: List[TaskEntity] = session.query(TaskEntity).all()
            return [
                Task(
                    id=int(task.id),
                    title=str(task.title),
                    description=str(task.description),
                    due_date=str(task.due_date),
                    status=str(task.status),  # type: ignore
                )
                for task in tasks
            ]

    def find(self, task_id: int) -> Task:
        with Session(self.engine) as session:
            task: TaskEntity | None = (
                session.query(TaskEntity).filter_by(id=task_id).first()
            )
            if task is None:
                raise Exception("Task not found")
            return Task(
                id=int(task.id),
                title=str(task.title),
                description=str(task.description),
                due_date=str(task.due_date),
                status=str(task.status),  # type: ignore
            )

    def create(self, task: TaskCreate) -> TaskCreateOut:
        with Session(self.engine) as session:
            stmt = (
                insert(TaskEntity)
                .values(
                    title=task.title,
                    description=task.description,
                    due_date=task.due_date,
                    status=task.status,
                )
                .returning(TaskEntity.id)
            )
            result: Any = session.execute(statement=stmt)
            session.commit()
            return TaskCreateOut(
                id=result.fetchone()[0],
                title=task.title,
                description=task.description,
                due_date=task.due_date,
                status=task.status,
            )

    def update(self, task_id: int, task: TaskUpdate) -> TaskUpdateOut:
        task_updated = TaskUpdate(**asdict(task))
        with Session(bind=self.engine) as session:
            stmt = (
                update(TaskEntity)
                .where(TaskEntity.id == task_id)
                .values(
                    title=task.title,
                    description=task.description,
                    due_date=task.due_date,
                    status=task.status,
                )
                .returning(TaskEntity.id)
            )
            result: Any | None = session.execute(statement=stmt)
            if result is None:
                raise Exception("Task not found")

            session.commit()

            return TaskUpdateOut(
                id=result.fetchone()[0],
                title=task.title,
                description=task.description,
                due_date=task.due_date,
                status=task.status,
            )

    def delete(self, task_id: int) -> None:
        with Session(bind=self.engine) as session:
            stmt = delete(TaskEntity).where(TaskEntity.id == task_id)
            session.execute(statement=stmt)
            session.commit()
