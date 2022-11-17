import socket
from binascii import hexlify

# get mac address
def get_mac(interface, p=0):

    # create dummy socket
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)

    # bind it with interface name
    s.bind((interface,p))

    # extract mac address
    mac =  hexlify(s.getsockname()[4])

    # close socket
    s.close()

    #return value
    print(mac)