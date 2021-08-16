from transformers import MarianTokenizer, MarianMTModel

src='bn'
dst='en'

model_name = f'Helsinki-NLP/opus-mt-{src}-{dst}'
model = MarianMTModel.from_pretrained(model_name)

print(f"Model loaded {model_name}")
tokenizer = MarianTokenizer.from_pretrained(model_name)

import cv2
import numpy as np 
import pytesseract
from unidecode import unidecode

# img = cv2.imread('big_text.png')
# img = cv2.imread('arabic.png')
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def dilate(image):
    kernel = np.ones((5,5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)

def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations=1)

def opening(image):
    kernel = np.ones((5,5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

def canny(image):
    return cv2.Canny(image, 100,200)

def deskew(image):
    coords = np.column_stack(np.where(image>0))
    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else :
        angle = -angle
    
    (h,w) = image.shape[:2]
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w,h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def match_template(image,template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOFF_NORMED)


def recog_image(imagename='./img/test_bangla.png'):

    print(imagename)
    # imagename = 'static/bengali_text.png'
    img = cv2.imread(imagename)

    img = cv2.transpose(img)
    img = cv2.flip(img,flipCode=0)

    grey = get_grayscale(img)
    grey = deskew(grey)
    grey = thresholding(grey)
    # canny = canny(grey) # edge detection

    screen_res = 1280, 720
    scale_width = screen_res[0] / grey.shape[1]
    scale_height = screen_res[1] / grey.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(grey.shape[1] * scale)
    window_height = int(grey.shape[0] * scale)
    
    
    # to show the preprocess
    cv2.imshow('dst_rt', grey)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Adding custom options
    # custom_config = r'--oem 3 --psm 6 -l ben --tessdata-dir Z:\\Installs\\tesseract\\tessdata'
    custom_config = r'--oem 3 --psm 6 -l ben'

    # custom_config = r'-l ara'
    result = pytesseract.image_to_string(grey, config=custom_config)
    strs = unidecode(result)
    
    print("Raw pytesseract: " , result)
    print("The string: " , strs)

    # with open("image_result.txt", "w",encoding='utf-8') as file:
    #     file.write( result )

    batch = tokenizer([result], return_tensors="pt")
    gen = model.generate(**batch)
    result = tokenizer.batch_decode(gen,skip_special_tokens=True)

    with open("image_result.txt", "a",encoding='utf-8') as file:
        file.write( str(result ))


    print("Final transform: ", result)

    return result

# print(recog_image())