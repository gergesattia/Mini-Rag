from pathlib import Path
from fastapi import FastAPI
from dotenv import load_dotenv
from src.routes import base

load_dotenv(Path(__file__).resolve().parent / ".env")

app = FastAPI()
app.include_router(base.router)
