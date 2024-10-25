import pika

def get_rabbitmq_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declara a fila, garantindo que ela exista
    channel.queue_declare(queue='file_queue', durable=True)

    return channel
