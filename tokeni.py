# from jose import JWTError, jwt
# import os
# from pydantic import BaseModel
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from dotenv import load_dotenv




# def generate_token(data=None):
#     load_dotenv()
#     SECRET_KEY = os.environ.get("SECRET_KEY")
#     ALGORITHM = "HS256"
#     if data is None:
#         data = {}
#     encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt
# # Données à encoder dans le token (facultatif)
# token_data = {"custom_key": "custom_value"}

# # Générez le jeton
# token = generate_token(token_data)
# print(token)