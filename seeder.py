from conexao import *
from sqlalchemyseeder import ResolvingSeeder


seeder = ResolvingSeeder(session)
estados = seeder.load_entities_from_json_file("seeder/estados.json")
cidades = seeder.load_entities_from_json_file("seeder/cidades.json")
generos = seeder.load_entities_from_json_file("seeder/generos.json")
artistas = seeder.load_entities_from_json_file("seeder/artistas.json")
tipo_eventos = seeder.load_entities_from_json_file("seeder/tipo_eventos.json")
eventos = seeder.load_entities_from_json_file("seeder/eventos.json")
precos = seeder.load_entities_from_json_file("seeder/precos.json")
apresentacoes = seeder.load_entities_from_json_file("seeder/apresentacoes.json")
tipo_despesas = seeder.load_entities_from_json_file("seeder/tipo_despesas.json")
despesas = seeder.load_entities_from_json_file("seeder/despesas.json")
receitas = seeder.load_entities_from_json_file("seeder/receitas.json")
session.commit()

print('Banco de dados povoado com sucesso!')

