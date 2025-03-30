import os
import json
import jwt
import requests
from flask import request
from dotenv import load_dotenv

load_dotenv()

SUPABASE_PROJECT_ID = os.getenv("SUPABASE_PROJECT_ID")
JWKS_URL = f"https://{SUPABASE_PROJECT_ID}.supabase.co/auth/v1/.well-known/jwks.json"
JWKS = requests.get(JWKS_URL).json()

def get_public_key(kid):
    for key in JWKS['keys']:
        if key['kid'] == kid:
            return jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key))
    return None

def verify_user_token():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None, "Missing Authorization header"

    try:
        token = auth_header.split(" ")[1]
        header = jwt.get_unverified_header(token)
        key = get_public_key(header["kid"])
        payload = jwt.decode(
            token,
            key=key,
            algorithms=["RS256"],
            issuer=f"https://{SUPABASE_PROJECT_ID}.supabase.co/auth/v1"
        )
        return payload, token
    except Exception as e:
        return None, str(e)
