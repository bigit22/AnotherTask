import httpx
from fastapi import HTTPException

from core.config import settings


class ModerationService:
    headers = {
        'accept': 'application/json',
        'x-magicapi-key': settings.MODERATION_API_KEY,
        'Content-Type': 'application/json'
    }

    @staticmethod
    async def moderate_image(link: str) -> dict:
        data = {'image': link}
        try:
            async with httpx.AsyncClient(timeout=20) as client:
                response = await client.post(settings.MODERATION_API_URL, headers=ModerationService.headers, json=data)
                response.raise_for_status()
                return response.json()

        except httpx.TimeoutException:
            raise HTTPException(
                status_code=408,
                detail='Request timed out')

        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=response.status_code if response else 500,
                detail=str(e))