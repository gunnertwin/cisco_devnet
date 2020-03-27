import requests
import json
from f5_info import f5
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def as3_declaration():

    with open('as3_config.json', 'r') as f:
        body = json.load(f)
    
    headers = {"Accept": "application/json",
          "Content-Type": "application/json"}

    url = f"https://{f5['host']}/mgmt/shared/appsvcs/declare"

    result = requests.get(url, headers=headers, auth=(f5["username"], f5["password"]), verify=False)

    if result.status_code == 200 or result.status_code == 204 :
        result = requests.post(url, headers=headers, auth=(f5["username"], f5["password"]), verify=False, data=json.dumps(body)).json()
        if result["results"][0]["code"] == 200:
            print("JSON config was uploaded to the F5 successfully")
            print(json.dumps(result, indent=4))
        else:
            print("There was a problem uploading the JSON config, please double check the formatting.")
            exit(0)
    else:
        print("Could not connect to the F5s AS3 api, please check that AS3 is installed.")

if __name__ == "__main__":
  as3_declaration()

