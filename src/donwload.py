import zipfile
import io
import httpx
import asyncio
from tqdm.asyncio import tqdm


async def unzip(client, zip_file_url, limit):
    async with limit:
        result = await client.get(zip_file_url)
        response = result.read()

    z = zipfile.ZipFile(io.BytesIO(response))
    return z.extractall(path="unzipped")


async def download(links):
    limit = asyncio.Semaphore(50)
    async with httpx.AsyncClient() as client:
        tasks = []
        for url in links:
            tasks.append(asyncio.ensure_future(unzip(client, url, limit)))
        await tqdm.gather(*tasks)
