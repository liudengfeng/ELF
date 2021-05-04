import socket


def get_ip():
    """本机IP地址
    """
    hostname = socket.getfqdn(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    return s.getsockname()[0]
