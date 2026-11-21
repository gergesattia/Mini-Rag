from fastapi import FastAPI,APIRouter
import os


app = FastAPI()
router = APIRouter(
    prefix="",
)

@router.get("/")

async def welcome_message():
    app_name = os.getenv('APP_NAME')
    return {
        "message": app_name
        }