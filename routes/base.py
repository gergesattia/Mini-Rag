from fastapi import FastAPI,APIRouter
app = FastAPI()
router = APIRouter(
    prefix="/api",
    tags=["base"]
)

@router.get("/")

def welcome_message():
    return {
        "message": "Welcome to Mini-Rag API!"
        }