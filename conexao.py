from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.sql import text
from entity import *

user = 'root'
password = 'root'
host = 'localhost'
port = '3306'
database = 'eventos'

# URL for Database Connection
url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'

# Database Connection
engine = create_engine(url, echo=False)
session = None

# Active sessions
try:
    connection = engine.connect()
    print('Conexão estabelecida com sucesso!\n')
    connection.close()

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

except Exception as e:
    print('Erro de conexão: ', e)
