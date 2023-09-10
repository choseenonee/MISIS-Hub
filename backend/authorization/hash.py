import bcrypt


def get_password_hash(password: str):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password.decode()


def compare_password(password: str, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())
