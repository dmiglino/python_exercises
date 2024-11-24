import time
import requests
import sys

call_num = sys.argv[1]

start_time = time.time()
for i in range(1, int(call_num)):
    try:
        print(requests.get('http://127.0.0.1:5000/get_value').text, end=', ')
    except requests.exceptions.ConnectionError as e:
        print(f'Conexion Rechazada: {str(e)}', end=', ')

print()
print("Tiempo de ejecucion Flask: %s segundos." % (time.time() - start_time))

start_time = time.time()
for i in range(1, int(call_num)):
    try:
        print(requests.get('http://127.0.0.1:8000/get_value').text, end=', ')
    except requests.exceptions.ConnectionError as e:
        print(f'Conexion Rechazada: {str(e)}', end=', ')

print()
print("Tiempo de ejecucion FastAPI: %s segundos." % (time.time() - start_time))


