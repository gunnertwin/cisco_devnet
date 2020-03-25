import requests
import json
from router_info import router
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {"Accept": "application/yang-data+json",
          "Content-Type": "application/yang-data+json"}

for host in router["host"]:

        url = f"https://{host}:{router['port']}/restconf/data/Cisco-IOS-XE-cdp-oper:cdp-neighbor-details"
        url2 = f"https://{host}:{router['port']}/restconf/data/ietf-interfaces:interfaces"

        response = requests.get(url, headers=headers, 
                auth=(router['username'], router['password']), verify=False)

        api_data = response.json()

        interfaces = api_data["Cisco-IOS-XE-cdp-oper:cdp-neighbor-details"]["cdp-neighbor-detail"]
        #print(json.dumps(api_data, indent=4))
        for device in interfaces:
                payload = {
                "ietf-interfaces:interfaces": {
                "interface": [
                {
                "name": f"{device['local-intf-name']}",
                "description": f"Connected to {device['device-name']} {device['port-id']} ",
                "type": "iana-if-type:ethernetCsmacd",
                "enabled": True
                }
                ]
                }
                }

                response = requests.patch(url2, headers=headers, auth=(router['username'], router['password']), data=json.dumps(payload), verify=False)
                print(response)