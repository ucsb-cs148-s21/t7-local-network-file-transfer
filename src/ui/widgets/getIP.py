import netifaces
import socket

def get_ip_thru_gateway():
    '''
    Opens a socket to the user's router (gateway) that allows the broadcast ip
    to be determined.
    Returns ip as a string.
    '''

    gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]	# https://pypi.org/project/netifaces/

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gateway, 80))					# Connect to gateway (router) to get local facing ipaddress
    address = s.getsockname()[0]
    s.close()
    return address+':2402'   # TODO REMOVE HARD CODE
