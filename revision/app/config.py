from dotenv import load_dotenv
import os
load_dotenv()

RMQ_PORT = os.getenv("RMQ_PORT")
RMQ_USER = os.getenv("RMQ_USER")
RMQ_VIRTUAL_HOST = os.getenv("RMQ_VIRTUAL_HOST")
RMQ_HOST = os.getenv("RMQ_HOST")
RMQ_PASSWORD = os.getenv("RMQ_PASSWORD")