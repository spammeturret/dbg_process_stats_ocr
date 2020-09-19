# dbg_process_stats_ocr
Optical character recognition component for DBG_Automation
As a part of the DBG game automation project, we want to implement features to capture game statistics and collate it in a database structure.
This solution leverages off the Google Cloud Platform and its machine learning services as a part of its architecture, including:
* Google Function
* Google Vision
* Google Sheets

## Motivation
A short description of the motivation behind the creation and maintenance of the project. This should explain why the project exists.


## Pre-requisites
1. A google cloud account created
2. Enable API Functionalities for the following GCP services:
   * Google Sheets
   * Google Functions
   * Google Vision
3. Create a service account with the following permission:
   * roles/cloudfunctions.invoker
4. Download service account credentials as .json file and have it in your project directory or somewhere secured.

## Dependencies
* google-api-core
* google-api-python-client
* google-auth
* google-auth-httplib2
* google-cloud-core
* google-cloud-vision
* pytz

## Installation
**1. Pull the repository to your local machine in a project directory:**
```
git clone https://github.com/spammeturret/dbg_process_stats_ocr
```
**2. Update the configuration section of each script in the following:**
```
/root/project/dbg_process_stats_ocr/google functions/main.py (Line 13-21)
```
**3. Navigate to your project directory, where your main.py file is.**
```
cd /root/project/dbg_process_stats_ocr/google functions/main.py
```
**4. Run the following command to create a new Google Cloud Function**
```
gcloud functions deploy process_stats \
--runtime python37 --trigger-http
```

## Usage
Function is triggered via HTTP, you'll need the following in your request:
1. ID Token in the header to for authentication.
2. Image to be encoded in Base64 format

**1. Update id token script configurations**
Update the configuration with your GCP project id and service account credential path.
```
/root/project/dbg_process_stats_ocr/google functions/gcloud-id-token.py (Line 10-12)
```

**2. Run the python file to print out your ID Token.**
```
python /root/project/dbg_process_stats_ocr/google functions/gcloud-id-token.py
```

**3. Attach the ID Token string as a bearer token to your request**

**4. Convert your string in base64-decoded string in json format:**
```
{
  "combined_stat": <<base64-decoded string>>
}
```
**5. Send the request and if it is sucessful, it'll print "DONE"**

## API Reference
* [Google Vision API Documentation](https://cloud.google.com/vision/docs/ocr)
* [Google Functions API Documentation](https://cloud.google.com/functions/docs/reference/rest)
* [Google Sheets API Documentation](https://developers.google.com/sheets/api/quickstart/python)
