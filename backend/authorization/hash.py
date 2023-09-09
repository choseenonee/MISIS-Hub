import bcrypt


def get_password_hash(password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password


def compare_password(password, password_hash):
    return bcrypt.checkpw(password.encode(), password_hash)
