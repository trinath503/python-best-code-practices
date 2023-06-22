# https://stackoverflow.com/questions/472000/usage-of-slots
"""
    - __enter__ (runs before the nested code block is executed) & __exit__ (runs after the nested code block is done)
    - By default open is context manager in python
    - Automatically deallocated memory even on error in resource manager. (acquire and release resources)
    - 
"""


# Exampl-1 
import psycopg2


class DataBaseConnection:

    def __init__(self, connection_params: dict) -> None:
        self.connection_params = connection_params
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connection(**self.connection_params)
        return self.connection

    def __exit__(self, exec_type, exec_val, exec_tab):
        self.connection.close()


connection_params = {
    'host' : 'localhost',
    "database": "mydb",
    "user": "myuser",
    "password": "password"
}


with DataBaseConnection(connection_params) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * from users")
    rows = cursor.fetchall()


# Example: 2
from contextlib import contextmanager

@contextmanager
def example_cm(string_input):

    string_input = string_input.swapcase()

    try:
        yield string_input
    except ValueError as e:
        print("An error occured")
    finally:
        print("Teardown logic")

    print("end of context manager")

with example_cm("trinath") as cm:
    print(cm)
