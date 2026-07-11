from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from rag.chatbot import ask

app = FastAPI(title="Horizon AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = Path(__file__).resolve().parent



app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)

templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


class ChatRequest(BaseModel):
    question: str


@app.get("/")
async def home():
    return {
        "version": "68cc553",
        "status": "NEW CODE"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    answer, pages = ask(request.question)

    return {
        "answer": answer,
        "pages": pages
    }