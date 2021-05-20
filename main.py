from ipaddress import IPv4Address
from ipaddress import IPv4Network
# https://realpython.com/python-ipaddress-module/

def get_ipaddress_integer(ip):
    ip_integer = 0
    ip_integer += ip[0] * (256 ** 3)
    ip_integer += ip[1] * (256 ** 2)
    ip_integer += ip[2] * (256 ** 1)
    ip_integer += ip[3] * (256 ** 0)
    print("Interger of IPv4 address: " + ip_integer)
    return ip_integer

def networkmethod():
    # ip address'
    ip_address = IPv4Address("220.24.9.37")

    print("Integer of IPv4 address: {ip}".format(ip = int(ip_address)))
    print("packed form of IPv4 address: {ip}".format(ip = ip_address.packed))
    print("IPv4 address: {ip}".format(ip = ip_address))
    print("")
    addrs = (
        IPv4Address("220.14.9.37"),
        IPv4Address("8.240.12.2"),
        IPv4Address("100.201.0.4"),
    )
    for a in sorted(addrs):
        print("IPv4 address: {addrs}".format(addrs = a))

    print("")
    # networks
    net = IPv4Network("192.4.2.0/24")
    print("Number of address: {net}".format(net = net.num_addresses))
    print("prefix length: {net}".format(net = net.prefixlen))
    print("Network mask: {net}".format(net = net.netmask))

if type(int) == type(int):
    networkmethod()