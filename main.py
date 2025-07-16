from fastapi import FastAPI, UploadFile, File
from faster_whisper import WhisperModel
import shutil, os

app = FastAPI()
model = WhisperModel("base", compute_type="int8")

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    path = f"/tmp/{file.filename}"
    with open(path, "wb") as out:
        shutil.copyfileobj(file.file, out)
    segments, info = model.transcribe(path)
    text = " ".join(segment.text for segment in segments)
    os.remove(path)
    return {"text": text}
