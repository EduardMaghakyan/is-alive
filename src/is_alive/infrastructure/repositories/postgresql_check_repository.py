from psycopg2._psycopg import connection

from is_alive.application.repositories.check_repository import CheckRepository
from is_alive.domain.model import Check


class PostgresqlCheckRepository(CheckRepository):
    def __init__(self, session: connection):
        self.session = session
        self.cursor = self.session.cursor()

    def add(self, check: Check) -> int:
        query = f"INSERT INTO check_result (status) VALUES (%s) RETURNING id"
        self.cursor.execute(query, [check.to_tuple()])
        return self.cursor.fetchone()[0]
