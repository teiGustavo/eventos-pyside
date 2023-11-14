from conexao import *
from entity import *

cidades = session.query(Cidade).join(Estado).all()

for cidade in cidades:
    print(f"Cidade: {cidade}")