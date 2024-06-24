import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from settings import logger


@contextmanager
def pg_conn_context(dsn: dict):
    """Контекстный менеджер для создания подключения к базам данных SQLite и Postgres"""
    try:
        pg_conn = psycopg2.connect(**dsn, cursor_factory=RealDictCursor)
        yield pg_conn
    except psycopg2.OperationalError as err:
        logger.error(f'Postgres connection context manager caught an error: {err}')
    finally:
        pg_conn.close()