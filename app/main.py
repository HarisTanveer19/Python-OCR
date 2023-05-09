from typing import Union
from fastapi import FastAPI, File, UploadFile
import pytesseract
from PIL import Image
import pathlib
import uuid

app = FastAPI()


IMG_DIR = "images/"
# img_path = "/home/haris/Desktop/FastAPI_OCR/app/images/test2.png"
img_path = "./images/test2.png"
text_path = "/home/haris/Desktop/FastAPI_OCR/app/Text"

@app.post('/')
async def Upload_img(file: UploadFile = File(...)):
    # Reading FIle Content
    content = await file.read()
    # Creating File in Image Directory
    with open(f"{IMG_DIR}{file.filename}", "wb") as f:
        f.write(content)
    # Opening image and converting into text
    img = Image.open(img_path)
    result = pytesseract.image_to_string(img)
    # Creating text file and saving
    f = open("./Text/result.txt", "w")
    f.write(result)
    f.close


    return {"filename": file.filename} 