#!/usr/bin/env python
# coding: utf-8
"""
Performs Optical Character Recognition (OCR) on the cropped images
=====================================
"""
import cv2
import requests
import io
import json
import re
import numpy as np 

API_KEY = '8ae022ceff88957'
URL_API = 'https://api.ocr.space/parse/image'
LANGUAGE = "swe"
LICENSE_PLATE_FORMAT = r'\b([A-Z0-9]+){3}\s([A-Z0-9]+){3}\b'

def parse_text(text):
    return re.search(LICENSE_PLATE_FORMAT, text).group()

def character_recognition(*argv, showImg = False):
    licenseNumbers = []
    print("Performing OCR...")
    for i in argv:
        _, compressedImage = cv2.imencode(".jpg", np.array(i), [1, 90])
        file_bytes = io.BytesIO(compressedImage)

        result = requests.post(URL_API, 
            files={"test.jpg": file_bytes},
            data={"apikey": API_KEY,
                  "language": LANGUAGE})

        result = result.content.decode()
        result = json.loads(result)

        text = result.get('ParsedResults')[0].get("ParsedText")
        parsedText = parse_text(text)
        print(parsedText)
        licenseNumbers.append(parsedText)
        if(showImg):
            cv2.imshow('License Plate ' + parsedText, i)
            cv2.waitKey(0)

    return parsedText


if __name__ == "__main__":
    test = cv2.imread("crop_test.jpg")
    character_recognition(test)