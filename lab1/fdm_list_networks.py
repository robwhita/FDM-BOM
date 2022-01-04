import requests
from crayons import blue, green, white 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pformat 
from fdm_auth import fdm_login


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

host='your_IP'
api_version='6'
username='admin'
password='Your_Pass'


def fdm_get_networks(access_token): 

    print(blue("\n==>Getting a list of all Networks in FDM"))

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(
    f"https://{host}/api/fdm/v{api_version}/object/networks",
    headers=headers,
    verify=False,)

    response.raise_for_status()

    print(green("Successfully retrieved the list of Networks"))
  
    return response.json()


if __name__ == '__main__': 
    token = fdm_login()
    networks = fdm_get_networks(token)

    print(white('Network(s):', bold=True),
    pformat(networks),
    sep="\n",) 

