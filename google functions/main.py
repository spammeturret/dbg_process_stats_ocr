import binascii
import json
from google.cloud import vision
from google.cloud.vision import types
from google.cloud.vision_v1 import ImageAnnotatorClient
from datetime import datetime
import pytz

from googleapiclient.discovery import build
import google.auth

def insert_gsheets(val_array):
    #CONFIG VARIABLES
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SPREADSHEET_ID = '<<SPREADSHEET ID>>'
    RANGE_NAME = '<<RANGE_NAME>>'
    values_range_body = {
        "range": RANGE_NAME,
        "majorDimension": "ROWS",
        "values": [val_array]
    }
    #SETUP SERVICE
    credentials, project = google.auth.default(scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    #INSERT OPERATION
    result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME,valueInputOption= "USER_ENTERED", body = values_range_body).execute()
    test = result.get('values', [])
    print(test)

def clean_array(array):
    """
    Input: Array
    Output: Array
    """
    dict_array = {
        "Ч": "4",
        "ч": "4",
        ":": ".",
        "К": "K",
        "-": "",
        "א": "K",
        "з": "a",
        "B": "8",
        "]": ""
    }
    new_arr=[]
    for item in array:
        for key, value in dict_array.items():
            item = item.replace(key, value)
        new_arr.append(item)
    return new_arr

def process_dbg_stat(request):
    request_json = request.get_json()
    client = vision.ImageAnnotatorClient()
    combined_stat = binascii.a2b_base64(request_json['combined_stat'])
    request = {
        'image':{
            'content': combined_stat
        },
        'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}]
    }

    response = client.annotate_image(request)
    arr = []

    melb = pytz.timezone('Australia/Melbourne')
    current_time = datetime.now(melb)

    for annotation in response.text_annotations:
        arr.append(annotation.description.rstrip("\n"))
    arr = clean_array(arr)
    arr.insert(0, current_time.strftime("%H:%M:%S"))
    arr.insert(0, current_time.strftime("%d/%m/%Y"))
    arr.pop(2)
    insert_gsheets(arr)

    return "DONE"