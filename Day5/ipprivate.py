import ipaddress

def validate_ip_address(ip_string):
    """
    Check if private IP
    """
    try:
        ip_object = ipaddress.ip_address(ip_string)
        return ip_object.is_private
    except ValueError as e:
        return False, str(e)

print(validate_ip_address('192.168.1.1'))