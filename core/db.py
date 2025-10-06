import psycopg2
# from psycopg2 import pool
# from contextlib import contextmanager
#
# from core import settings
#
# # from app.core.config import settings
#
# db_pool = pool.SimpleConnectionPool(
#     1, 10,
#     host=settings.DB_HOST,
#     database=settings.DB_NAME,
#     user=settings.DB_USER,
#     password=settings.DB_PASSWORD,
#     port=settings.DB_PORT,
# )
#
# @contextmanager
# def get_conn():
#     conn = db_pool.getconn()
#     try:
#         yield conn
#     finally:
#         db_pool.putconn(conn)


import psycopg2

from core import settings


class DataBase:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=settings.DB_HOST,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            port=settings.DB_PORT
        )

    def _get_conn(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="your_database",
            user="your_user",
            password="your_password",
            port="5432"
        )

    def execute(self, sql, many=True):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall() if many else cursor.fetchone()
        self.conn.close()
        cursor.close()
        return result

    def commit(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        result = cursor.fetchone()
        self.conn.close()
        cursor.close()
        return result

