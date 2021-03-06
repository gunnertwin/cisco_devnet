# import requests
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# headers = {"Authorization": "Basic bGVhcm5pbmc6bGVhcm5pbmc"}
# url = "https://devnetapi.cisco.com/sandbox/mse/api/location/v2/clients"

# response = requests.get(url, headers=headers, verify=False)

# print(response.text)

from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json


token = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
meraki = MerakiSdkClient(token)
orgs = meraki.organizations.get_organizations()

for org in orgs:
    if org["name"] == "DevNet Sandbox":
        orgID = org["id"]
        print(f"The org ID of {org['name']} is {orgID}.")

#networkid = meraki.networks()
#vlans = meraki.vlans.get_network_vlans()
#print(vlans)

network = meraki.networks.get_network("L_566327653141843049")


#json = json.dumps(network, indent=4)

#import ipdb; ipdb.set_trace()
products = network["productTypes"]

for product in products:
    print(f"I love owning a {product}!")
