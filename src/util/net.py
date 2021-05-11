import netifaces
import socket


def get_ip_thru_gateway() -> str:
    '''
    Opens a socket to the user's router (gateway) that allows the broadcast ip
    to be determined.
    Returns ip as a string.
    '''

    # https://pypi.org/project/netifaces/
    gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Connect to gateway (router) to get local facing ipaddress
    s.connect((gateway, 80))
    address = s.getsockname()[0]
    s.close()
    return address
