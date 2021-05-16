FROM python:3.9-slim

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt-get update && apt-get install make
RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false
RUN poetry install
COPY ./src /app/
RUN poetry install

CMD ["python", "-m", "is_alive.interface.cli.perform_check"]