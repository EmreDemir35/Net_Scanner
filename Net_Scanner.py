import scapy.all as scapy
import optparse

def user_inputs():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress",dest="ip_address",help="Enter Ip Address")
    (user_input,argument)=parse_object.parse_args()

    if not user_input.ip_address:
        print("Error!! Enter Ip Address")
    return  user_input
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    boardcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packed=boardcast_packet/arp_request
    (answer_list,unanswered_list)=scapy.srp(combined_packed,timeout=1)
    answer_list.summary()

user_ip_address=user_inputs()
scan(user_ip_address.ip_address)