from typing import Optional

from fastapi import APIRouter, UploadFile, HTTPException

from models.schemas import ModerationResponse
from services.file_uploading import UploadService
from services.nsfw_moderation import ModerationService

nsfw_r = APIRouter()

@nsfw_r.post('/moderate',
             response_model=ModerationResponse,
             response_model_exclude_none=True)
async def moderate_image(file: Optional[UploadFile] = None):
    if not file:
        raise HTTPException(status_code=400, detail='No image provided')

    image_bytes = await file.read()
    upload_link = await UploadService.upload_file_to_0x0(image_bytes, file.filename)
    moderation_result = await ModerationService.moderate_image(upload_link)

    if moderation_result.get('result') == 'normal':
        return {'status': 'OK'}
    else:
        return {'status': 'REJECTED', 'reason': 'NSFW content'}
