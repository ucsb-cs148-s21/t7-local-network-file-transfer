import netifaces
import socket


def get_ip_thru_gateway():
    '''
    Opens a socket to the user's router (gateway) that allows the broadcast ip
    to be determined.
    Returns ip as a string.
    '''
    # Get the user's router ip address https://pypi.org/project/netifaces/
    ​gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
    
    # Connect socket to the router
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gateway, 80))					# Connect to gateway (router) to get local facing ipaddress
    
    ipaddress = s.getsockname()[0])
    return ipaddress
