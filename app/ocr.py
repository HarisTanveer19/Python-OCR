import pytesseract
import pathlib
from PIL import Image

BASE_DIR = pathlib.Path(__file__).parent
IMG_DIR = BASE_DIR / "images/"
img_path =  IMG_DIR / "img2.jpg" 

img = Image.open(img_path)

result = pytesseract.image_to_string(img)

print(result)