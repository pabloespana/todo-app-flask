get_tasks_specs_dict = {
    "parameters": [],
    "definitions": {
        "Tasks": {"type": "array", "items": {"$ref": "#/definitions/Task"}},
        "Task": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                },
                "title": {
                    "type": "string",
                },
                "description": {
                    "type": "string",
                },
                "due_date": {
                    "type": "string",
                },
                "status": {
                    "type": "string",
                    "enum": ["pending", "in_progress", "done"],
                },
            },
        },
    },
    "responses": {
        "200": {
            "description": "Successful response",
            "schema": {"$ref": "#/definitions/Tasks"},
        }
    },
}

get_task_specs_dict = {
    "parameters": [
        {"name": "task_id", "in": "path", "type": "integer", "required": "true"}
    ],
    "definitions": {
        "Task": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                },
                "title": {
                    "type": "string",
                },
                "description": {
                    "type": "string",
                },
                "due_date": {
                    "type": "string",
                },
                "status": {
                    "type": "string",
                    "enum": ["pending", "in_progress", "done"],
                },
            },
        }
    },
    "responses": {
        "200": {
            "description": "Successful response",
            "schema": {"$ref": "#/definitions/Task"},
        }
    },
    "example": {"due_date": "2023-12-20"},
}

create_task_specs_dict = {
    "parameters": [
        {
            "in": "body",
            "name": "body",
            "required": "true",
            "schema": {
                "id": "Task",
                "$ref": "#definitions/TaskCreate",
            },
        }
    ],
    "definitions": {
        "TaskCreate": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                },
                "description": {
                    "type": "string",
                },
                "due_date": {
                    "type": "string",
                },
                "status": {
                    "type": "string",
                    "enum": ["pending", "in_progress", "done"],
                },
            },
        },
        "TaskCreateOut": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                },
                "title": {
                    "type": "string",
                },
                "description": {
                    "type": "string",
                },
                "due_date": {
                    "type": "string",
                },
                "status": {
                    "type": "string",
                    "enum": ["pending", "in_progress", "done"],
                },
            },
        },
    },
    "responses": {
        "201": {
            "description": "Successful response",
            "schema": {"$ref": "#/definitions/TaskCreateOut"},
        }
    },
}

update_task_specs_dict = {
    "parameters": [
        {"name": "task_id", "in": "path", "type": "integer", "required": "true"},
        {
            "in": "body",
            "name": "body",
            "required": "true",
            "schema": {
                "id": "Task",
                "$ref": "#definitions/TaskUpdate",
            },
        },
    ],
    "definitions": {
        "TaskUpdate": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                },
                "description": {
                    "type": "string",
                },
                "due_date": {
                    "type": "string",
                },
                "status": {
                    "type": "string",
                    "enum": ["pending", "in_progress", "done"],
                },
            },
        },
        "TaskUpdateOut": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                },
                "title": {
                    "type": "string",
                },
                "description": {
                    "type": "string",
                },
                "due_date": {
                    "type": "string",
                },
                "status": {
                    "type": "string",
                    "enum": ["pending", "in_progress", "done"],
                },
            },
        },
    },
    "responses": {
        "200": {
            "description": "Successful response",
            "schema": {"$ref": "#/definitions/TaskUpdateOut"},
        }
    },
}

delete_task_specs_dict = {
    "parameters": [
        {"name": "task_id", "in": "path", "type": "integer", "required": "true"},
    ],
    "responses": {
        "200": {
            "description": "Successful response",
        }
    },
}
