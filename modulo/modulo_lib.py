

def gcd(a,b):
    x = b%a
    while(x != 0):
        # x = remainder,  a 
        # b <<--a
        # a <<-- x
        b = a
        a = x
        x = b%a
    return a
