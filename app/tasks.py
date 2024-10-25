from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
import os
from datetime import time
import logging

logger = logging.getLogger(__name__)

DATABASE_URL = "sqlite:///./files.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
files_table = Table('files', metadata, autoload_with=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def update_file_status(filename, status):
    db = SessionLocal()
    file_record = db.query(files_table).filter(files_table.c.filename == filename).first()
    if file_record:
        db.execute(files_table.update().where(files_table.c.filename == filename).values(status=status))
    db.commit()
    db.close()

def process_file(file_location):
    try:
        if os.path.exists(file_location):
            print(f"Processando o arquivo: {file_location}")
            time.sleep(5)
            if file_location.endswith(".fail"):
                raise Exception("Erro no processamento do arquivo.")
            print(f"Arquivo {file_location} processado com sucesso!")
            update_file_status(os.path.basename(file_location), "processado")
        else:
            raise FileNotFoundError(f"Arquivo {file_location} não encontrado.")
    except Exception as e:
        logging.error(f"Erro ao processar {file_location}: {str(e)}")
