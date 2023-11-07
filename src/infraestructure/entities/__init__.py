from typing import Any
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy.orm import DeclarativeMeta

Base: Any = declarative_base()

from src.infraestructure.entities.task_entity import TaskEntity  # noqa: F401 E402
