from fastapi import FastAPI
from dotenv import load_dotenv
from source.routes import base

load_dotenv("\.env")  # Load environment variables from .env file

app = FastAPI()
app.include_router(base.router)
