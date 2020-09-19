import google.oauth2.credentials
from google.oauth2 import id_token
from google.oauth2 import service_account
import google.auth
import google.auth.transport.requests
from google.auth.transport.requests import AuthorizedSession
import requests

#CONFIGURATION
project_id = '<<project ID>>'
target_audience = 'https://australia-southeast1-'+project_id+'.cloudfunctions.net/test-auth-1'
svcAccountFile = '<<Service Account Path>>'

#Use this function to refresh your ID Token for Google Cloud Functions call
def GetIDTokenFromServiceAccount(svcAccountFile, target_audience):
  """
  Input: Service Account Path, Target Audience Endpoint
  Output: ID Token String
  """
  creds = service_account.IDTokenCredentials.from_service_account_file(
        svcAccountFile,
        target_audience= target_audience)
  request = google.auth.transport.requests.Request()
  creds.refresh(request)
  return creds.token

#Use this function to check if your ID token is still valid or if it's expired.
def VerifyIDToken(token, audience=None):
  """
  Input: ID Token String, Target Audience Endpoint
  Output: True if token is still valid, False if invalid
  """
  certs_url='https://www.googleapis.com/oauth2/v1/certs'
  request = google.auth.transport.requests.Request()
  result = id_token.verify_token(token,request,certs_url=certs_url)
  if audience in result['aud']:
    return True
  return False

#Execute this script just to test out ID token generation
if __name__ == "__main__":
  print("New Token ID is: \n \n"+GetIDTokenFromServiceAccount(svcAccountFile, target_audience))