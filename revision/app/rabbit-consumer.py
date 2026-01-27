import config
import time
import ssl
import pika
import json

ssl_context = ssl.create_default_context()
connection_params = pika.ConnectionParameters(
    host = config.RMQ_HOST,
    port = config.RMQ_PORT,
    virtual_host = config.RMQ_VIRTUAL_HOST,
    credentials=pika.PlainCredentials(username=config.RMQ_USER, password=config.RMQ_PASSWORD),
    ssl_options = pika.SSLOptions(context=ssl_context) 
)

def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)


def process_message(channel: pika.adapters.blocking_connection.BlockingChannel, method, properties, body):
    print(f" [v] Processing: {body.decode()}", flush=True)
    time.sleep(1)
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print(f" [x] Done with {method.delivery_tag}", flush=True)

def consume_message(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'logs'
    channel.queue_declare(queue=QUEUE)
    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=process_message,
        auto_ack=False
    )
    channel.start_consuming()

def main():
    print("Connecting to RabbitMQ...")
    with get_connection() as connection:
        print("Connection established!") 
        with connection.channel() as channel:
            consume_message(channel)

if __name__ == "__main__":
    main()