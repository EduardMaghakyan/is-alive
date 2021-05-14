FROM python:3.9-slim

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry install
COPY ./src /app/

ENTRYPOINT ["poetry", "run"]
