from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/model_download")
async def model():
    return FileResponse("model.pkl", filename="model.pkl", media_type="application/octet-stream")
