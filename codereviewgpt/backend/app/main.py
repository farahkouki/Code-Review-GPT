from fastapi import FastAPI
from app.api import routes
from dotenv import load_dotenv
load_dotenv()


app = FastAPI(title="CodeReviewGPT", version="0.1.0")
app.include_router(routes.router, prefix="/api")

@app.get("/")
async def root():
    return {"msg": "CodeReviewGPT backend is running. See /api/docs"}
