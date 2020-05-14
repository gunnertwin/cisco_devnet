import requests
import json

router = {"host":"192.168.1.201", 
        "port":"8443", 
        "username":"cisco", 
        "password":"cisco"}

headers = {"Accept": "application/yang-data+json",
          "Content-Type": "application/yang-data+json"}

url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces"


response = requests.get(url, headers=headers, 
          auth=(router['username'], router['password']), verify=False)

api_data = response.json()

print(api_data["ietf-interfaces:interfaces"]["interface"][0])