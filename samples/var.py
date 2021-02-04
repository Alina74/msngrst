import os


os.environ.update(var='localhost')

var = os.getenv('var')
print(var)
print(os.environ.get('var'))

os.environ.pop('var')

var = os.getenv('var')
print(var)

# print(os.environ.values())


def get_env(key: str, type_: str, default: str = None):

    var = os.getenv(key)

    if var is None:
        return default

    elif type_ == str:
        return key

    elif type_ == int:
        try:
            return int(var)
        except:
            return default

    elif type_ == bool:

        if var in ['False', 'No', 'n', '0']:
            return False
        return False


