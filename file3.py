import requests, asyncio

async def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

async def main():
    urls = ["https://jsonplaceholder.typicode.com/todos/1", "https://jsonplaceholder.typicode.com/todos/2"]
    data = []
    for u in urls:
        d = await fetch_data(u)
        data.append(d)
    print(data)

asyncio.run(main())
