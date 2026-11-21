from fastapi import FastAPI,APIRouter
import os


app = FastAPI()
router = APIRouter(
    prefix="/api",
)

@router.get("/")

def welcome_message():
    app_name = os.getenv('APP_NAME')
    return {
        "message": f"Welcome to {app_name} API!"
        }