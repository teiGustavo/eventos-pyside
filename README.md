# Eventos - PySide6

Pacotes usados no projeto:
SQLAlchemy, PyMySQL, SQLAlchemy-seeder, Pandas

Para verificar se possui as dependências necessárias, use:
pip list

Para instalar rapidamente, use os seguintes comandos:
pip install sqlalchemy
pip install pymysql 
pip install sqlalchemy-seeder
pip install pandas

- Obs 1: Não foi disponibilizado o ambiente virtual para evitar possíveis incompatibilidades por erro de versão (ao ativar o venv em uma versão SDK diferente, o ambiente virtual quebra e o projeto não funcionará corretamente).

Para iniciar, execute o arquivo "reset.sql" contido na pasta "sql"
- Obs 2: Esse arquivo foi criado para facilitar pois por motivos do SQLAlchemy, a base de dados "eventos" já deve estar criada corretamente

Para testar o código, execute o arquivo main, no qual está contido todas as funções responsáveis por retornar e exibir as tabelas devidamente cadastradas pelo python (como o arquivo main importa o arquivo de conexão, mesmo que seja a primeira vez executando o script, ele mesmo se encarregará de mapear o banco de dados)

Para povoar o banco de dados:
Rode o seeder.py (é necessário que se rode o script manualmente a fim de evitar falhas devido às limitações do SQLAlchemy-Seeder)

- Obs 3: A lib Pandas foi utilizado para facilitar a visualização dos dados providos do banco de dados
- Obs 4: Para a exibição de dados nos dataframes pandas no arquivo main.py, execute os passos descritos para povoar o banco de dados

A conexão com o banco de dados está no arquivo "conexao.py" e as tabelas que serão criadas estão no arquivo "entity.py"

O arquivo com o modelo relacional está contido na pasta "sql"




------------------------------------------------------------------------------------------------------------------------


VERSÃO UTILIZADA PARA O DESENVOLVIMENTO DO PROJETO: PYTHON 3.8


------------------------------------------------------------------------------------------------------------------------
