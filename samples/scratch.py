container = [num for num in range(11) if not num % 2]

print(container)


def func(x, y, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs) # dict - 'key': 'value'


# после * если переменные указываеются, то обязательно именованные
def func(request, *, body=None, config=None):
    pass


if __name__ == '__main__':
    # func(1, 2, 3, 4, user_id=10, tasks=[''])
    params = (2, 3, 4)
    body = dict(user_id=10, tasks=['t1', 't2'])
    func(1, 2, params, body)
    func(1, 2, *params, body)
    func(1, 2, *params, **body)

