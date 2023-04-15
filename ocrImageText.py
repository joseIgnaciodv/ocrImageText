import easyocr
from PIL import Image
import re
import datetime

def readText(image):
    text = ""
    reader = easyocr.Reader(['es'])
    res = reader.readtext(image, detail=0)
    for word in res:
        text = text + word + " "
    return text

def getImageExtension(filePath: str):
    extension = ""
    indexDot = filePath.rfind('.')
    extension = filePath[indexDot:]
    return extension

def saveRotatedImage(image: Image, filename: str):
    image.save(filename)

def getTextFromImage(imgPath: str):
    text = ""
    results = []
    # ext = getImageExtension(imgPath)
    # date = str(datetime.datetime.now().date())
    # date = re.sub('-', '_', date)
    # filename = date + "_img" + ext
    
    image = Image.open(imgPath)
    exif = image.getexif()
    if 256 in exif.keys() and 257 in exif.keys():
        imgWidth = exif[256]
        imgLength = exif[257]
        if ((imgWidth > imgLength) and exif[274] == 1):
            rotated = image.rotate(-90)
            saveRotatedImage(rotated, imgPath)
            img = Image.open(imgPath)
            text = readText(img)
            results = re.findall(r'([0-9]{8,18})', text)
    else:
        text = readText(image)
        results = re.findall(r'([0-9]{8,18})', text)
    print(text)


getTextFromImage('images/ticket_Leroy.jpg')

# getTextFromImage('images/eci_factura_2.jpg')
# getTextFromImage('images/ejemplo1.jpg')
# getTextFromImage('images/eci_factura_3.jpeg')
print("\n\n")
# getTextFromImage('images/lm_factura_3.jpg')
# getTextFromImage('images/zara_factura.jpg')