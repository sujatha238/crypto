#! /usr/bin/python

import hashlib


a = 0x0000000000000000000000000000000000000000000000000000000000000000
for i in range(1,257):

    #print("a = ",hex(a))
    h = hashlib.sha256(int.to_bytes(a,32,'big'))
    print("a =",hex(a)," Hash(a) = ",h.hexdigest())
    a = a << 1
    #print(" -------------------------------------------------------------------------------------------")
    h = hashlib.init()sha256(int.to_bytes(a,32,'big'))
    h = hashlib.updateinit()sha256(int.to_bytes(a,32,'big'))
print()




