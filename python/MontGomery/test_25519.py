

from ecc_lib import *




p = 2**255  - 19
#L = 2^252+27742317777372353535851937790883648493
L = 2**252 + 0x14def9dea2f79cd65812631a5cf5d3ed

x1 = 0xe0eb7a7c3b41b8ae1656e3faf19fc46ada098deb9c32b1fd866205165f49b800
#x1 = 0xe0eb7a7c3b41b8ae1656e3faf19fc46ada098deb9c32b1fd866205165f49b880
#scalar = 0x0000000000000000000000000000000000000000000000000000000000000040
scalar = 0xc8d74acde5934e64b9895d5ff7afbffd7f704f7dfccff7ac28fa62a1e6410347
#scalar = 0x302e020100300506032b656e04220420c8fe0df92ae68a03023fc0c9adb9557d31be7feed0d3ab36c558143daf4dbb40
#scalar = 0xc8d74acde5934e64b9895d5ff7afbffd7f704f7dfccff7ac28fa62a1e6410347
#scalar = 0x70076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a
#scalar = 0x6ebd9ed75882d52815a97585caf4790a7f6c6b3b7f821c5e259a24b02e502e11
#scalar = 0x0200000000000000000000000000000000000000000000000000000000000000
#scalar = 0x05dab087e624a8a4b79e17f8b83800ee66f3bb1292618b6fd1c2f8b27ff88e0eb
#scalar =  0x689faee7d21893c0b2e6bc17f5cef7a600000000000000000000000000000040
#scalar =  0x80000000000000000000000000000000a6f7cef517bce6b2c09318d2e7ae9f68
#scalar = 0xe8e0717b91fbb284195a5610fdc15712215eb6417f8f2759fa87668ca7eaeb56
#scalar = 0x18f7cd39d5619ed93bc4aed5d615472642290f9ab90af8af9c85411bb16b3446
#x1 = 0x6f0377d6430d4f431a5918153cc57f0982f8e8e7b4f719cdfa1c89050d33ae65
#x1 = 0x2245c5cad56b135a7eace39b2b859953d1a1fa13c564f18783fd9f737149b379
#order = 2**252 + 0x14def9dea2f79cd65812631a5cf5d3ed

#scalar = 0xedd3f55c1a631258d69cf7a2de14000000000000000000000000000000000010

#print("\n Order                : ", hex(L))
#print("\n Base Point           : ", hex(x1))
#print("\n scalar               : ", hex(scalar))
A24 = 0x01DB42


byte_scalar = scalar.to_bytes(32,byteorder='little')
byte_x1= x1.to_bytes(32,byteorder='little')

int_scalar = int.from_bytes(byte_scalar, byteorder='big')
int_x1= int.from_bytes(byte_x1, byteorder='big')
print("\n Prime                : ", hex(p))
print("\n Base Point           : ", hex(x1))
print("\n Base Point           : ", hex(int_x1))
print("\n scalar               : ", hex(scalar))
print("\n scalar after big_num : ",hex(int_scalar))


rx,rz = ecc_mul_x25519(int_x1,int_scalar,A24,p)
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


