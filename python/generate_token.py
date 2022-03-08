from datetime import datetime
from datetime import timedelta
import base64
import hmac
import hashlib
import jwt
import os

api_key = os.getenv('API_KEY')
key_id = os.getenv('KEY_ID')
aud_url = os.getenv('AUD_URL')

def generate_jwt():

        curr_time = datetime.utcnow()
        payload = {
            "aud": aud_url,
            "iat": curr_time,
            "exp": curr_time + timedelta(seconds=10),
            "iss": key_id,
            "metadata": {
                "reason": "fetch usages",
                "requesterip": "127.0.0.1",
                "date-time": curr_time.strftime("%m/%d/%Y, %H:%M:%S"),
                "user-agent": "datamart"
            }
        }
        signature = base64.b64encode(hmac.new(bytes(api_key, 'UTF-8'), bytes(key_id, 'UTF-8'), digestmod=hashlib.sha512).digest())
        token = jwt.encode(payload, signature, algorithm='HS512',
                     headers={"kid": key_id})
        print("Token: {}" .format(token))

generate_jwt()
