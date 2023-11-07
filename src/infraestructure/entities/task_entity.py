from sqlalchemy import Column, Integer, VARCHAR, Float
from src.infraestructure.entities import Base


class TaskEntity(Base):
    __tablename__ = "tasks"
    id = Column(Integer(), primary_key=True)
    title = Column(VARCHAR(length=25), nullable=False)
    description = Column(VARCHAR(length=100), nullable=False)
    due_date = Column(VARCHAR(), nullable=False)
    status = Column(VARCHAR(), nullable=False)
