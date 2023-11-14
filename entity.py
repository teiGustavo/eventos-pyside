from sqlalchemy import Column, Date, String, Integer, ForeignKey, Double
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Estado(Base):
    __tablename__ = 'estados'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    abreviacao = Column(String(2), nullable=False)


class Cidade(Base):
    __tablename__ = 'cidades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(300), nullable=False)
    estado_id = Column(Integer, ForeignKey('estados.id'), nullable=False)


class Genero(Base):
    __tablename__ = 'generos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)


class Artista(Base):
    __tablename__ = 'artistas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    pagina_web = Column(String(100), default='Não Informada', nullable=True)
    genero_id = Column(Integer, ForeignKey('generos.id'), nullable=False)


class TipoEvento(Base):
    __tablename__ = 'tipo_eventos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)


class Evento(Base):
    __tablename__ = 'eventos'
    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    localizacao = Column(String(100), nullable=False)
    tipo_evento_id = Column(Integer, ForeignKey('tipo_eventos.id'), nullable=False)
    cidade_id = Column(Integer, ForeignKey('cidades.id'), nullable=False)


class Preco(Base):
    __tablename__ = 'precos'
    id = Column(Integer, primary_key=True)
    cache = Column(Double, nullable=False)
    artista_id = Column(Integer, ForeignKey('artistas.id'), nullable=False)
    evento_id = Column(Integer, ForeignKey('eventos.id'), nullable=False)


class Apresentacao(Base):
    __tablename__ = 'apresentacoes'
    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    valor_ingresso = Column(Double, nullable=False)
    publico_maximo = Column(Integer, nullable=False)
    publico_presente = Column(Integer, default=publico_maximo, nullable=True)
    artista_id = Column(Integer, ForeignKey('artistas.id'), nullable=False)
    evento_id = Column(Integer, ForeignKey('eventos.id'), nullable=False)


class TipoDespesa(Base):
    __tablename__ = 'tipo_despesas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)


class Despesa(Base):
    __tablename__ = 'despesas'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(300), nullable=False)
    valor = Column(Double, nullable=False)
    data = Column(Date, nullable=False)
    tipo_despesa_id = Column(Integer, ForeignKey('tipo_despesas.id'), nullable=False)
    evento_id = Column(Integer, ForeignKey('eventos.id'), nullable=False)


class Receita(Base):
    __tablename__ = 'receitas'
    id = Column(Integer, primary_key=True)
    valor = Column(Double, nullable=False)
    evento_id = Column(Integer, ForeignKey('eventos.id'), nullable=False)
