from os import getenv

POSTGRES_DB = getenv('POSTGRES_DB', 'altar_db')
POSTGRES_HOST = getenv('POSTGRES_HOST', '127.0.0.1')
POSTGRES_PORT = getenv('POSTGRES_PORT', 5432)
POSTGRES_USER = getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD', 'qwerty')

POSTGRES_ENGINE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@" \
                      f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
