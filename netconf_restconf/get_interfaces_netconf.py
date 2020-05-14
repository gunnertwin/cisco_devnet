from ncclient import manager
import xml.dom.minidom
import xmltodict

router = {"host":"192.168.1.201", 
        "port":"830", 
        "username":"cisco", 
        "password":"cisco"}

netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces-state>
</filter>
"""



with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
        interface_netconf = m.get(netconf_filter)
        print(interface_netconf)
        interface_python = xmltodict.parse(interface_netconf.xml)[
            "rpc-reply"]["data"]
        name = interface_python["interfaces"]["interface"]["name"]["#text"]
        config = interface_python["interfaces"]["interface"]
        op_state = interface_python["interfaces-state"]["interface"]
        
        print("Start")
        print(f"Name: {config['name']['#text']}")
        print(f"Description: {config['description']}")
        print(f"Packets in: {op_state['statistics']['in-unicast-pkts']}")