import json
from flask import Flask, Response
from flasgger import Swagger  # type: ignore
from src.presentation.http.v1.task_controller import task_router
from src.config import configure_inject

configure_inject()

app = Flask(__name__)
app.config["DEBUG"] = True


@app.errorhandler(Exception)
def internal_server_error(e):
    """Error handler"""
    return json.dumps({"error": str(e)}), 500


@app.get("/")
def home() -> Response:
    """Home"""
    return Response(response=json.dumps({"response": "Task App"}), status=200)


template = {
    "swagger": "2.0",
    "info": {
        "title": "Tasks App",
        "description": "This API was developed using Python Flask",
        "version": "1.0",
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": '\
            JWT Authorization header using the Bearer scheme. Example: "Authorization: Bearer {token}"',
        }
    },
    "security": [{"Bearer": []}],
}

app.config["SWAGGER"] = {
    "title": "Flask API",
    "uiversion": 2,
    "template": "./resources/flasgger/swagger_ui.html",
}

Swagger(app, template=template)

app.register_blueprint(task_router())  # pylint: disable=E1120
