## Pacotes do Projeto:
- [Pandas](https://pypi.org/project/pandas/)
- [PySide6](https://pypi.org/project/PySide6/)
- [PyMySQL](https://pypi.org/project/pymysql/) 
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)
- [SQLAlchemy-seeder](https://sqlalchemy-seeder.readthedocs.io/en/latest/) 

> **Important**
> O [pipenv](https://pypi.org/project/pipenv/) foi utilizado para gerenciar as dependencias do projeto, mas caso necessário, utilize o método de instalação manual.

## Método de Instalação Manual de Dependências:

Para verificar se possui as dependências necessárias, use:
```
pip list
```

Para instalar rapidamente, use os seguintes comandos:
```
pip install pandas
pip install pyside6
pip install pymysql 
pip install sqlalchemy
pip install sqlalchemy-seeder
```

## Utilização:

> **Warning**
> Antes de tudo, é necessário criar o banco de dados 'eventos' ou apagá-lo caso o mesmo exista. Para isso, execute o arquivo: `reset.sql`
 
Para resetar manualmente o banco de dados:

```
DROP DATABASE IF EXISTS eventos
CREATE DATABASE IF NOT EXISTS eventos
USE eventos
```

> **Warning**
> Após o reset, execute os arquivos `conexao.py` e `seeder.py`

Para executar via terminal (prompt de comando):

```
cd [CAMINHO_PASTA_RAIZ]
python conexao.py
python seeder.py
```

> **Note**
> Após seguir os passos acima, execute o arquivo `main.py`

Para executar via terminal (prompt de comando):

```
cd [CAMINHO_PASTA_RAIZ]
python main.py
```


## Observações:

> **Note**
> - Não foi disponibilizado o ambiente virtual para evitar possíveis incompatibilidades por erro de versão (ao ativar o venv em uma versão SDK diferente, o ambiente virtual quebra e o projeto não funcionará corretamente).
>
> - Como já especificado, a base de dados "eventos" já deve estar criada corretamente (apenas o banco de dados de forma limpa, sem nehuma tabela).
> 
> - A lib Pandas foi utilizado para facilitar a visualização dos dados providos do banco.
>
> - Caso não seja a primeira utilização, não é necessário a execução de todos os passos descritos em 'Utilização', apenas execute o arquivo `main.py` da pasta raiz do projeto.
> 
> - Versão Python utilizada: 3.8.6
