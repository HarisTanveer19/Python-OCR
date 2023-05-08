from typing import Union
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import pathlib
import uuid

app = FastAPI()

# BASE_DIR = pathlib.Path(__file__).parent
IMG_DIR =  "images/"

@app.post('/')
async def Upload_img(file: UploadFile = File(...)):
    # file.filename = f"{uuid.uuid1().jpg}"
    file.filename = f"{uuid.uuid1()}.png"
    file.filename = f"{uuid.uuid4()}.jpg"
    content = await file.read()

    with open(f"{IMG_DIR}{file.filename}", "wb") as f:
        f.write(content)
    return {"filename": file.filename} 