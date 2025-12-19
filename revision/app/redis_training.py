"""Basic connection example.
"""
from dotenv import load_dotenv
import redis
from revision.app import config

load_dotenv()


r = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    username=config.REDIS_USERNAME,
    password=config.REDIS_PASSWORD,
)


r.set('car', 'dodge durango')
r.set('pet', 'rat', 6200)

car = r.get('car')
print(car)
pet = r.get('pet')
print(pet)

# >>> bar

