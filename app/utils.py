# The 'passlib' import below is correct. If you are seeing an "unresolved import" error,
# please make sure that you have installed the dependencies from requirements.txt
# into your virtual environment using a command like:
# pip install -r requirements.txt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
