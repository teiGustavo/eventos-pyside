from conexao import *
from entity import *


def format_date_to_sql(data):
    data = data.split('/')
    return f"{data[2]}-{data[1]}-{data[0]}"


def unformat_sql_date(data):
    data = f"{data}"
    data = data.split('-')
    return f"{data[2]}/{data[1]}/{data[0]}"


def get_date_array(data):
    if '-' in data:
        return data.split('-')

    data = data.split('/')
    return data[::-1]



def get_estado_by_id(estado_id):
    estado = session.query(Estado).filter(Estado.id == estado_id).first()
    return estado.nome


def get_estado_by_name(nome_estado):
    estado = session.query(Estado).filter(Estado.nome.contains(nome_estado)).first()
    return estado.id


def get_cidade_by_id(cidade_id):
    cidade = session.query(Cidade).filter(Cidade.id == cidade_id).first()
    return cidade.nome


def get_cidade_by_name(nome_cidade):
    cidade = session.query(Cidade).filter(Cidade.nome.contains(nome_cidade)).first()
    return cidade.id


def get_genero_by_id(genero_id):
    genero = session.query(Genero).filter(Genero.id == genero_id).first()
    return genero.nome


def get_genero_by_name(nome_genero):
    genero = session.query(Genero).filter(Genero.nome.contains(nome_genero)).first()
    return genero.id


def get_artista_by_id(artista_id):
    artista = session.query(Artista).filter(Artista.id == artista_id).first()
    return artista.nome


def get_artista_by_name(nome_artista):
    artista = session.query(Artista).filter(Artista.nome.contains(nome_artista)).first()
    return artista.id


def get_tipo_evento_by_id(tipo_evento_id):
    tipo_evento = session.query(TipoEvento).filter(TipoEvento.id == tipo_evento_id).first()
    return tipo_evento.nome


def get_tipo_evento_by_name(nome_tipo_evento):
    tipo_evento = session.query(TipoEvento).filter(TipoEvento.nome.contains(nome_tipo_evento)).first()
    return tipo_evento.id


def format_evento(evento: Evento):
    data = evento.data
    data = f"{data}".split('-')

    return f"{data[2]}/{data[1]}/{data[0]} | {evento.localizacao} | {get_cidade_by_id(evento.cidade_id)}"


def get_evento_by_id(evento_id):
    evento = session.query(Evento).filter(Evento.id == evento_id).first()

    return format_evento(evento)


def get_evento_by_format(evento_formatado):
    evento_formatado = evento_formatado.split(" | ")

    data = evento_formatado[0].split('/')

    evento = session.query(Evento).filter(
        Evento.data.contains(f'{data[2]}-{data[1]}-{data[0]}'), Evento.localizacao.contains(evento_formatado[1]),
        Evento.cidade_id == get_cidade_by_name(evento_formatado[2])
    ).first()

    return evento.id
