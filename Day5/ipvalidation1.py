import ipaddress

def validate_ip_address(ip_string):
    """
    Validates an IP address string using the ipaddress module.

    Args:
        ip_string (str): The IP address string to validate.

    Returns:
        tuple: A tuple containing (True, ip_object) if valid,
               or (False, error_message) if invalid.
    """
    try:
        ip_object = ipaddress.ip_address(ip_string)
        return True, ip_object
    except ValueError as e:
        return False, str(e)
    
iplist=['172.1.1.1', '172.2.2.2', '192.6.6.6', '274.35.2.1', '258.3.666.2', '125.3.5.1']
validlist=[]
invalidlist=[]

for ip in iplist:
    isvalid,result=validate_ip_address(ip)
    if isvalid:
        validlist.append(ip)
    else:
        invalidlist.append(ip)

print(f"Valid Ip List: {validlist}")
print(f"Invalid Ip List: {invalidlist}")