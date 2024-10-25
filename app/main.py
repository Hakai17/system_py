from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import pika
from .rabbitmq import get_rabbitmq_connection

app = FastAPI()

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    # Salvando o arquivo temporariamente
    with open(file_location, "wb+") as f:
        f.write(file.file.read())

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
