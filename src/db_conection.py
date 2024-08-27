from sqlalchemy import create_engine
from decouple import config

engine = create_engine(f'postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}/{config('DB_DB')}')

def conn():
    return engine