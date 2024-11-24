import time
import asyncio
import aiohttp
import sys

# Para realizar una solicitud asíncrona
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

# Para probar la API
async def test_api(base_url, num_requests):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, f"{base_url}/get_value") for _ in range(num_requests)]
        results = await asyncio.gather(*tasks)
    return results

# Test
async def main():
    num_requests = int(sys.argv[1])

    # Prueba para Flask
    flask_start = time.time()
    await test_api("http://127.0.0.1:5000", num_requests)
    flask_end = time.time()
    print(f"Tiempo de ejecución Flask: {flask_end - flask_start:.2f} segundos.")

    # Prueba para FastAPI
    fastapi_start = time.time()
    await test_api("http://127.0.0.1:8000", num_requests)
    fastapi_end = time.time()
    print(f"Tiempo de ejecución FastAPI: {fastapi_end - fastapi_start:.2f} segundos.")

asyncio.run(main())

