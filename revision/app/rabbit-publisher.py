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
print(config.RMQ_HOST)
def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)

def produce_logs(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'logs'
    channel.queue_declare(queue=QUEUE)
    
    for i in range(100):
        message_dict = {
        "event":"event_name",
        "id" : i
        }
        json_message = json.dumps(message_dict)

        channel.basic_publish(
            exchange = '',
            routing_key = QUEUE,
            body = json_message,
            properties= pika.BasicProperties(content_type="application/json")
        )
    print('100 logs sent')

def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            produce_logs(channel)

if __name__ == "__main__":
    main()