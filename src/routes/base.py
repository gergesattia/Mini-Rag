from fastapi import APIRouter, Depends

from src.helpers import Settings, get_settings

router = APIRouter()

@router.get("/")
async def welcome_message(app_settings: Settings = Depends(get_settings)):
    return {
        "message": app_settings.APP_NAME,
        "version": app_settings.APP_VERSION,
    }