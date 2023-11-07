FROM python:3.11.3-slim as base

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.2.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv

# Install poetry
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry

ENV PATH="$POETRY_VENV/bin:$PATH"

WORKDIR /code
COPY . .

RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["gunicorn", "-b", ":5000", "src.app:app"]
