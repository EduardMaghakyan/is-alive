import uuid

import psycopg2  # type: ignore
import pytest
from psycopg2 import OperationalError

from is_alive.domain.model import Check
from is_alive.domain.model.check import CheckStatus
from is_alive.infrastructure.repositories.postgresql_check_repository import (
    PostgresqlCheckRepository,
)


def create_connection(db_name):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user="is_alive_user",
            password="example",
            host="db",
        )
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        exit()

    return connection


def create_test_db() -> str:
    conn = create_connection("postgres")
    cursor = conn.cursor()

    dbname = f"is_alive_{uuid.uuid1().hex}"
    conn.autocommit = True
    cursor.execute(f"CREATE DATABASE {dbname};")
    conn.close()
    return dbname


def drop_test_db(dbname):
    conn = create_connection("postgres")
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"DROP DATABASE {dbname};")
    conn.close()


@pytest.fixture
def test_postgres_session():
    dbname = create_test_db()

    conn = create_connection(dbname)
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS "check_result" (
      "id" serial NOT NULL,
      "status" text NOT NULL,
      PRIMARY KEY ("id")
    );"""
    )

    yield conn

    conn.close()
    drop_test_db(dbname)


def test_check_repo_add(test_postgres_session):
    check = Check(status=CheckStatus.SUCCESS)

    repo = PostgresqlCheckRepository(test_postgres_session)
    last_insert_id = repo.add(check)
    cursor = test_postgres_session.cursor()
    cursor.execute(f"SELECT status FROM check_result WHERE id={last_insert_id}")
    result = cursor.fetchone()
    assert CheckStatus.SUCCESS.value == result[0]
