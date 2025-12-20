"""Basic connection example.
"""
from dotenv import load_dotenv
import redis
from revision.app import config
import datetime

load_dotenv()


r = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USERNAME,
    password=config.REDIS_PASSWORD,
)


r.set('car', 'dodge durango')
r.set('pet', 'rat')

car = r.get('car')
print(car)
pet = r.get('pet')
print(pet)

exptime = datetime.datetime(year=2025, month=12, day=27)

# r.rpush('food_list', 'ham')
# r.rpush('food_list', 'sour milk')
# r.rpush('food_list', 'cheese')
# r.expireat('food_list', exptime)

foodlist = r.lrange('food_list', 0, 2)
print(foodlist)

# r.hset('food_cart',  mapping={"flour": 250, "milk": 500})
# r.hset('food_cart', mapping = {'sugar':300})
# r.hset('food_cart', mapping = {'sugar':500})
print(r.hgetall('food_cart'))
