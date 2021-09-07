

from ecc_lib import *




p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = p - 3
x1 = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
y1 = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5

#x1 = 0xde2444bebc8d36e682edd27e0f271508617519b3221a8fa0b77cab3989da97c9
#y1 = 0xc093ae7ff36e5380fc01a5aad1e66659702de80f53cec576b6350b243042a256

z1 = 0x0000000000000000000000000000000000000000000000000000000000000001


#rx,ry,rz = ecc_double_jacobian(x1,y1,z1,a,p)
#
#inv_rz = pow(rz,(p-2),p)
#rx = (rx * inv_rz*inv_rz)%p
#ry = (ry * inv_rz*inv_rz*inv_rz)%p
#print("\n double result :")
#print(" x = ", hex(rx))
#print(" y = ", hex(ry))
#print(" z = ", hex((rz*inv_rz) % p))
#print()
#
#x2 =  0x7669e6901606ee3ba1a8eef1e0024c33df6c22f3b17481b82a860ffcdb6127b0
#y2 =  0xfa878162187a54f6c39f6ee0072f33de389ef3eecd03023de10ca2c1db61d0c7
#z2 = 0x0000000000000000000000000000000000000000000000000000000000000001

#
#rx,ry,rz = ecc_add_jacobian(x1,y1,z1,x2,y2,z2,a,p)
#
#inv_rz = pow(rz,(p-2),p)
#rx = (rx * inv_rz*inv_rz)%p
#ry = (ry * inv_rz*inv_rz*inv_rz)%p
#print("\n add result :")
#print(" x = ", hex(rx))
#print(" y = ", hex(ry))
#print(" z = ", hex((rz*inv_rz) % p))
#print()

scalar = 0xc51e4753afdec1e6b6c6a5b992f43f8dd0c7a8933072708b6522468b2ffb06fd
#scalar = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551
#scalar = 0x3


print(" b4 ecc_mul \n x1 : ", hex(x1))
print(" y1 : ", hex(y1))
print(" z1 : ", hex(z1))
print("scalar : ",hex(scalar))

rx,ry,rz = ecc_mul_jacobian(x1,y1,z1,scalar,a,p)

print("after ecc_mul : X,Y,Z")
print(" x = ", hex(rx))
print(" y = ", hex(ry))
print(" z = ", hex(rz))

inv_rz = pow(rz,(p-2),p)
rx = (rx * inv_rz*inv_rz)%p
ry = (ry * inv_rz*inv_rz*inv_rz)%p
print("\n mul result :")
print(" x = ", hex(rx))
print(" y = ", hex(ry))
print(" z = ", hex((rz*inv_rz) % p))
print()



