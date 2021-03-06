import bcrypt

from helpers.password.exception import GeneratePasswordHashException, CheckPasswordHashException


def generate_hash(pwd: str) -> bytes:
    try:
        return bcrypt.hashpw(
            password=pwd.encode(),
            salt=bcrypt.gensalt(),
        )
    except (TypeError, ValueError) as e:
        raise GeneratePasswordHashException(str(e))


def check_hash(pwd: str, hsh: bytes) -> bool:
    try:
        result = bcrypt.checkpw(
            password=pwd.encode(),
            hashed_password=hsh,
        )
    except (TypeError, ValueError) as e:
        raise CheckPasswordHashException(str(e))
    return result


if __name__ == '__main__':
    password = 'qwerty'
    for _ in range(3):
        hsh_ = generate_hash(password)
        print(f'{password}: {hsh_}')
