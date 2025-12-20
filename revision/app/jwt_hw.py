import jwt
import datetime
import time
from revision.app import config

current_time = datetime.datetime.now(datetime.timezone.utc)

payload = {
    'name':'Hlib',
    'age': 16,
    'city':'shanghai',
    "exp": current_time + datetime.timedelta(seconds=1000)
}

encoded_jwt = jwt.encode(
    payload=payload,
    key = config.jwt_secret,
    algorithm='HS256'
)

payload3 = {
    'name':'bib',
    'age': 1900,
    "exp": current_time + datetime.timedelta(seconds=500)
}

encoded_jwt3 = jwt.encode(
    payload=payload3,
    key = config.jwt_secret,
    algorithm='HS256'
)

print(encoded_jwt3)


jwt.decode(
    jwt=encoded_jwt3,
    key = 'wrong key',
    algorithms=['HS256']

)
