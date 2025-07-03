import httpx

class UploadService:
    url = "https://0x0.st"

    @staticmethod
    async def upload_file_to_0x0(file_bytes: bytes, filename: str) -> str:
        async with httpx.AsyncClient(verify=False, timeout=20) as client:
            response = await client.post(
                UploadService.url,
                files={'file': (filename, file_bytes)}
            )
        response.raise_for_status()
        return response.text.strip()

