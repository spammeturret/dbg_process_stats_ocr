# ocr-component
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

**1. To create the ID token, do the following**
Update the configuration section of each script in the following
```
/root/project/dbg_process_stats_ocr/google functions/gcloud-id-token.py (Line 10-12)
```

Run the python file to print out your ID Token.
'''
'''
You can use Postman or Python to invoke the Google Cloud Function.
###Postman




## Build status
Build status of continus integration i.e. travis, appveyor etc. Ex. -

Build Status Windows Build Status

Code style
If you're using any code style like xo, standard etc. That will help others while contributing to your project. Ex. -

js-standard-style

Screenshots
Include logo/demo screenshot etc.

Tech/framework used
Ex. -

Built with

Electron
Features
What makes your project stand out?

Code Example
Show what the library does as concisely as possible, developers should be able to figure out how your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

Installation
Provide step by step series of examples and explanations about how to get a development env running.

API Reference
Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.
* google vision
* google function
* google sheets


Tests
Describe and show how to run the tests with code examples.

How to use?
If people like your project they’ll want to learn how they can use it. To do so include step by step guide to use your project.

Contribute
Let people know how they can contribute into your project. A contributing guideline will be a big plus.

Credits
Give proper credits. This could be a link to any repo which inspired you to build this project, any blogposts or links to people who contrbuted in this project.

Anything else that seems useful
