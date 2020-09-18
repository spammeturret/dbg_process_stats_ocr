import base64
import json
from google.cloud import vision
import PIL.Image
import requests
from google.oauth2 import service_account
from oauth2client import client
import jwt
import time
import httplib2
from google.cloud.vision_v1 import ImageAnnotatorClient
from google.cloud import vision
from google.cloud.vision import types
import binascii
from python_imagesearch.imagesearch import region_grabber
from datetime import datetime
import pytz

from googleapiclient.discovery import build
import google.auth
import gspread

import io

def encode_base64(var):
    """
    Input: PIL img
    Output: base64 string
    """
    message_bytes = str(var).encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('ascii')

def get_access_token():

    #CONFIGURATIONS
    SERVICE_ACCOUNT_FILE = '<<Path to service account>>'
    with open(SERVICE_ACCOUNT_FILE) as f:
        private = json.load(f)

    #iat and exp are time variables to dictate token creation time and expiration time/date
    iat = int(time.time())
    exp = iat + 3600
    
    #Create header
    additional_headers = {
		"kid": private["private_key_id"],
        "alg": "RS256",
        "typ": "JWT"
        }

    #Create JWT payload
    jwt_payload = {
    "iss": "<<Service account email>>",
    "aud": "https://oauth2.googleapis.com/token",
    "scope": "https://www.googleapis.com/auth/cloudfunctions https://www.googleapis.com/auth/cloud-platform",
    "exp": exp,
    "iat": iat
    }

    #Base64 encoded request token
    request_token = jwt.encode(
        jwt_payload,
        private["private_key"],
        algorithm='RS256',
        headers=additional_headers
    )

    #Decode Request Token to string using UFT-8 Encoding
    decoded_request_token = request_token.decode("utf-8")

    #Construct Request Payload
    request_payload = {
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": decoded_request_token
    }

    access_token = requests.post(private["token_uri"], data = request_payload)
    return (access_token.text)

def gcloud_vision_test():
    #CREATE VISION CLIENT
    client = vision.ImageAnnotatorClient()

    #CONFIGURATION
    path = 'C:\\projects\\ocr-component\\temp.png'
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    #CONSTRUCT REQUEST
    request = {
        'image':{
            'content': content
        },
        'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}]
    }
    #PRINT OUT RESPONSE
    response = client.annotate_image(request)
    print (response)
    for annotation in response.text_annotations:
        print(annotation.description.rstrip("\n"))

def img_to_base64(x1, y1, x2, y2):
    """
    Input: input the co-ordinates
    output: capture of x & y co-ordinates in base64 form (string)
    """
    save_dir = "temp.png"
    screenshot = region_grabber(region=(x1,y1,x2,y2))
    screenshot.save(save_dir, "PNG")
    with open(save_dir, "rb") as image_file:
        encoded_base64 = base64.b64encode(image_file.read())
    return encoded_base64

#gcloud_vision_test()