import inject
from src.domain.ports.input.task_service import TaskService
from src.domain.ports.output.task_repository import TaskRepository
from src.domain.task_service_impl import TaskServiceImpl
from src.infraestructure.adapters.output.task_repository import (
    TaskPostgresRepository,
)


def configure_inject() -> None:
    """Method to configure dependency injections"""

    def config_repositories(binder: inject.Binder) -> None:
        binder.bind_to_provider(TaskRepository, TaskPostgresRepository)

    def config_services(binder: inject.Binder) -> None:
        binder.bind_to_provider(TaskService, TaskServiceImpl)

    def config(binder: inject.Binder) -> None:
        config_repositories(binder)
        config_services(binder)

    inject.configure(config)
