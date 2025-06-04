from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import clear_mappers
from infrastructure.database import connection as conn
from src.adapters.orm import metadata, start_mappers

def test_conexao_com_postgre_via_docker():
    # Iniciando mapeamento e criação de bases de dado
    start_mappers()

    try:
        metadata.create_all(conn.engine)
        
        # Realizando query qualquer de teste
        with conn.session_maker() as session:
            query = session.execute(text(
                "SELECT 1"
            ))
            assert query.fetchall() == [(1,)]

        # Fechando a sessão
        clear_mappers()    
    except Exception as e:
        assert type(e) == OperationalError
        