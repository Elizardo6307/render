import psycopg2
from decouple import config

def conexion2023():
    try:
        conex = psycopg2.connect(
            host=config('BD_HOST'),
            user=config('BD_USER'),
            password=config('BD_PASSWORD'),
            database=config('BD_DB'),
            port=5432
        )
        return conex
    except psycopg2.Error as e:
        print("Error al conectarse a Postgresql:", e)
        return None
