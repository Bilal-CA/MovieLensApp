import os
import jwt
import datetime
import json


# Access environment variables
supabase_jwt_secret = str(os.getenv('SUPABASE_JWT_SECRET'))
supabase_url = os.getenv('SUPABASE_URL')


# Payload data for the JWT token
payload = {
    'sub': 'USER_ID',
    'aud': 'authenticated',
    'iss': supabase_url,
    'email': 'EMAIL',
}


# Generate the JWT token
token = jwt.encode(payload, supabase_jwt_secret, algorithm='HS256')


print("Generated JWT Token:", token)

try:
    # Decode the JWT token
    decoded_token = jwt.decode(token, supabase_jwt_secret, algorithms=['HS256'], audience='authenticated')

    print("Decoded Token:", json.dumps(decoded_token, indent=3))  # Pretty-print the decoded token

except jwt.ExpiredSignatureError:
    print("Token has expired.")

except jwt.InvalidTokenError as e:
    print("Invalid token:", str(e))
