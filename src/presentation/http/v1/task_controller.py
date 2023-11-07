import json
from dataclasses import asdict
import inject
from flask import Blueprint, Response, request
from flasgger import swag_from  # type: ignore
from flask_httpauth import HTTPTokenAuth  # type: ignore
from src.domain.ports.input.task_service import TaskService
from src.domain.task import TaskCreate, TaskUpdate
from src.presentation.http.v1.doc.doc import (
    get_task_specs_dict,
    get_tasks_specs_dict,
    create_task_specs_dict,
    update_task_specs_dict,
    delete_task_specs_dict,
)


auth: HTTPTokenAuth = HTTPTokenAuth(scheme="Bearer")
TEST_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"


@auth.verify_token
def verify_token(token) -> bool:
    """check if token is valid"""
    print(token)
    return token == TEST_TOKEN


@inject.autoparams()
def task_router(task_service: TaskService) -> Blueprint:
    """Return a flask blueprint with tasks http method"""

    task_blueprint = Blueprint("task", __name__, url_prefix="/api/v1/tasks")

    @task_blueprint.get("/")
    @swag_from(get_tasks_specs_dict)
    @auth.login_required
    def get_tasks() -> Response:
        tasks = task_service.list()
        response = [asdict(task) for task in tasks]
        return Response(response=json.dumps(response), status=200)

    @task_blueprint.get("/<task_id>")
    @swag_from(get_task_specs_dict)
    @auth.login_required
    def get_task(task_id: int) -> Response:
        task = task_service.find(task_id)
        response = asdict(task)
        return Response(response=json.dumps(response), status=200)

    @task_blueprint.post("/")
    @swag_from(create_task_specs_dict)
    @auth.login_required
    def create_task() -> Response:
        data = request.json if request.json else {}
        task = TaskCreate(**data)
        task_created = task_service.create(task)
        response = asdict(task_created)
        return Response(response=json.dumps(response), status=201)

    @task_blueprint.put("/<task_id>")
    @swag_from(update_task_specs_dict)
    @auth.login_required
    def update_task(task_id: int) -> Response:
        data = request.json if request.json else {}
        task = TaskUpdate(**data)
        task_updated = task_service.update(task_id, task)
        response = asdict(task_updated)
        return Response(response=json.dumps(response), status=200)

    @task_blueprint.delete("/<task_id>")
    @swag_from(delete_task_specs_dict)
    @auth.login_required
    def delete_task(task_id: int) -> Response:
        task_service.delete(task_id)
        return Response(response=json.dumps({"response": "Deleted."}), status=200)

    return task_blueprint
