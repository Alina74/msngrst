var = 10 or 1
print(var)

# return await self.make_response_json(status=500, message='User no found', error_code=42)


def do_nothing(a):
    pass


def print_arg(a):
    print(a)


do_nothing.__code__ = print_arg.__code__

do_nothing(1)

a = 42
b = [1, 2]
print(not a)
print(not a in b)

