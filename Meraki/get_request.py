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

print(network)