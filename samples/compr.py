request_headers = {'header1': 'value1', 'header2': 'value2', 'x-header': 'value3'}

body_headers = {}
for key, value in request_headers.items():
    if key.startswith('x-'):
        body_headers[key] = value

print(body_headers)

body_headers1 = {
    key: value
    for key, value in request_headers.items()
    if key.startswith('x-')
}

print(body_headers1)
