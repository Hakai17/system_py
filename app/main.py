from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import pika
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
from .rabbitmq import get_rabbitmq_connection

app = FastAPI()

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Configuração do SQLite e SQLAlchemy
DATABASE_URL = "sqlite:///./files.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

files_table = Table(
    'files', metadata,
    Column('id', Integer, primary_key=True),
    Column('filename', String),
    Column('status', String),
)

metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para atualizar o status do arquivo no banco
def update_file_status(filename, status):
    db = SessionLocal()
    file_record = db.query(files_table).filter(files_table.c.filename == filename).first()
    if file_record:
        db.execute(files_table.update().where(files_table.c.filename == filename).values(status=status))
    else:
        db.execute(files_table.insert().values(filename=filename, status=status))
    db.commit()
    db.close()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    # Salvando o arquivo temporariamente
    with open(file_location, "wb+") as f:
        f.write(file.file.read())

    # Atualiza o status no banco para "pendente"
    update_file_status(file.filename, "pendente")

    # Conectando ao RabbitMQ e enviando o caminho do arquivo para a fila
    channel = get_rabbitmq_connection()
    channel.basic_publish(
        exchange='',
        routing_key='file_queue',
        body=file_location,
        properties=pika.BasicProperties(
            delivery_mode=2,  # Torna a mensagem persistente
        )
    )

    return JSONResponse(content={"message": f"Arquivo '{file.filename}' enviado para a fila."})
