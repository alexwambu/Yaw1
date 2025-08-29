from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from video_pipeline import generate_video
import os

app = FastAPI()

# Serve React frontend
app.mount("/static", StaticFiles(directory="frontend/dist/static"), name="static")

@app.get("/")
async def serve_root():
    return FileResponse("frontend/dist/index.html")

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    script = data.get("script", "")
    output = generate_video(script)
    return {"status": "done", "file": output}
