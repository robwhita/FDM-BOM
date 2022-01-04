import requests
from crayons import blue, green, white 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pformat 
from fdm_auth import fdm_login

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

host='your_IP'
api_version='6'
username='admin'
password='your_pass'

NETWORK_OBJECT = {
    "name": "PUT_NAME_HERE",
    "description": "DevNet Security",
    "subType": "HOST",
    "value": "5.5.5.5",
    "type": "networkobject"
}


def fdm_create_network(network_object, access_token): 
    print(blue('\n==> Creating a new network in FDM'))

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    payload = network_object

    response = requests.post(f"https://{host}:{port}/api/fdm/v{api_version}/object/networks",
        headers=headers,
        json=payload,
        verify=False,
    )

    response.raise_for_status()

    print(green("Successfully created the new network!"))
    return response.json()


if __name__ == '__main__': 
    token = fdm_login
    new_network = dm_create_network(NETWORK_OBJECT, token)
    print(white('Network Details:', bold=True),
    pformat(new_network)
    sep="\n") 