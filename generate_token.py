import jwt

SECRET_KEY = "mysecretkey123"
payload = {"user": "test_user"}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("Bearer", token)
