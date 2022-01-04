import requests
import json 
from crayons import blue, green
from requests.models import HTTPError 
from requests.packages.urllib3.exceptions import InsecureRequestWarning


host='Your_IP'
username='admin'
password='Your_pass'
api_version='6'

headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

payload = {
        "grant_type": "password",
        "username": username,
        "password": password,
    }

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def fdm_login(): 

    """Login to FDM and return an access token that may be used for API calls.
    This login will give you an access token that is valid for ~30 minutes
    with no refresh. Using this token should be fine for short running scripts.
    Do not use for services that need to last longer than 30 minutes.
    """
    print(blue("\n==> Logging into FDM and requesting an access token"))

    response = requests.post(f'https://{host}/api/fdm/v{api_version}/fdm/token',
    headers=headers, json=payload, verify=False)  

    try:
        response.raise_for_status()
        access_token = response.json()['access_token']
    except HTTPError:
        if response.status_code == 400:
            raise HTTPError(f'Error logging into FDM: {response.text}')
        elif response.status_code == 401:
            raise HTTPError('Not authorized')
        else:
            raise

    except KeyError:
        raise KeyError("Error parsing the response from FDM")


    print(
         green("Login was successful!"),
         f'Access Token: {access_token}',
         sep="\n")

    return access_token

if __name__=="__main__": 
    fdm_login()