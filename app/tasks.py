import pika
import time

def callback(ch, method, properties, body):
    file_location = body.decode()
    print(f"Processando o arquivo: {file_location}")

    # Simulação de processamento (ex: redimensionar uma imagem)
    time.sleep(5)

    print(f"Arquivo {file_location} processado com sucesso!")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar a fila para garantir que ela exista
    channel.queue_declare(queue='file_queue', durable=True)

    # Consome as mensagens da fila
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='file_queue', on_message_callback=callback)

    print("Aguardando mensagens para processamento...")
    channel.start_consuming()

if __name__ == "__main__":
    start_consumer()
