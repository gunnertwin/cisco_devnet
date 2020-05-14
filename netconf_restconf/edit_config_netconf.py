from ncclient import manager
import xml.dom.minidom
import xmltodict
from router_info import router

config_template = open(
      'netconf_config.xml').read()

netconf_config = config_template.format(
  interface="GigabitEthernet1", description="DEVNET_TRAINING"
)

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
        interface_netconf = m.edit_config(netconf_config, target="running")        
        print(interface_netconf)

