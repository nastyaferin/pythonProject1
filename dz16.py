import requests

pyth = 'https://www.python.org/'

try:
    resp = requests.request('GET', pyth)
    print(resp.status_code)
except Exception as e:
    print(f'Error: {e}')
else:
    print(f'Response: {resp}')
    data = resp.content
    con = resp.headers['Content-Type']
    print(con)
    if 200 <= resp.status_code < 300 and resp.headers['Content-Type'] == 'text/html':
        with open('index.html', 'wb') as f:
            f.write(data)

    else:
        print('Unecspected result')
        with open('index.html', 'wb') as f:
            f.write(data)

