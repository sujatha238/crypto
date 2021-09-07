

from ecc_lib import *




p = 2**255  - 19
#L = 2^252+27742317777372353535851937790883648493
L = 2**252 + 0x14def9dea2f79cd65812631a5cf5d3ed

x1 = 0xe0eb7a7c3b41b8ae1656e3faf19fc46ada098deb9c32b1fd866205165f49b880
scalar = 0xc8d74acde5934e64b9895d5ff7afbffd7f704f7dfccff7ac28fa62a1e6410347
A24 = 0x01DB41


byte_scalar = scalar.to_bytes(32,byteorder='little')
byte_x1= x1.to_bytes(32,byteorder='little')

int_scalar = int.from_bytes(byte_scalar, byteorder='big')
int_x1= int.from_bytes(byte_x1, byteorder='big')

int_x1 = int_x1&p
int_scalar = int_scalar&p
print("\n Prime                : ", hex(p))
print("\n Base Point           : ", hex(x1))
print("\n Base Point           : ", hex(int_x1))
print("\n scalar               : ", hex(scalar))
print("\n scalar after big_num : ",hex(int_scalar))


rx,rz = RFC_7748_ecc_mul_x25519(int_x1,int_scalar,A24,p)
print(" rx = ", hex(rx))
print(" rz = ", hex(rz))
inv_rz = pow(rz,(p-2),p)
rx = (rx * inv_rz)%p
rz = (rz * inv_rz)%p


byte_rx  = rx.to_bytes(32,byteorder='big')
int_rx  = int.from_bytes(byte_rx,byteorder='little')

byte_rz  = rz.to_bytes(32,byteorder='big')
int_rz  = int.from_bytes(byte_rz,byteorder='little')
print("\n x25519 result       : ")
print(" rx = ", hex(rx))
print(" int_x = ", hex(int_rx))
print(" z = ", hex((int_rz)))
print()


