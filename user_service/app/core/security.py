import bcrypt


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_hash_password(password: str, user_password: str) -> bool:
    return bcrypt.checkpw(password.encode(), user_password.encode())
