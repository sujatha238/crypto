

## lHash:
#da 39 a3 ee 5e 6b 4b 0d 32 55 bf ef 95 60 18 90
#af d8 07 09
#
## DB:
#
#da 39 a3 ee 5e 6b 4b 0d 32 55 bf ef 95 60 18 90
#af d8 07 09 00 00 00 00 00 00 00 00 00 00 00 00
#00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
#00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
#00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
#00 00 00 00 00 00 00 00 00 00 01 d4 36 e9 95 69
#fd 32 a7 c8 a0 5b bc 90 d3 2c 49
#
## seed:
#aa fd 12 f6 59 ca e6 34 89 b4 79 e5 07 6d de c2
#f0 6c b5 8f
#
## dbMask:
#06 e1 de b2 36 9a a5 a5 c7 07 d8 2c 8e 4e 93 24
#8a c7 83 de e0 b2 c0 46 26 f5 af f9 3e dc fb 25
#c9 c2 b3 ff 8a e1 0e 83 9a 2d db 4c dc fe 4f f4
#77 28 b4 a1 b7 c1 36 2b aa d2 9a b4 8d 28 69 d5
#02 41 21 43 58 11 59 1b e3 92 f9 82 fb 3e 87 d0
#95 ae b4 04 48 db 97 2f 3a c1 4e af f4 9c 8c 3b
#7c fc 95 1a 51 ec d1 dd e6 12 64

import hashlib
from binascii import hexlify

def i2osp(integer, size):
  for i in range(size):
      ''.join([chr((integer >> (8 * i)) & 0xFF)]) 

  #return ''.join([chr((integer >> (8 * i)) & 0xFF) for i in (range(size))])

def mgf1(input_data, length, hash=hashlib.sha1):
  counter = 0
  output = ''
  print("input_data = ", input_data)

  while (len(output) < length):
    print("counter = ",counter)
    C = int(input_data,16)
    print(" C = ",hex(C))
    C =  C + 1
    print(" C = C + 1 = ",hex(C))
    tmp = str(C)
    print("hash input ", tmp)
    output += (hash(bytes.fromhex(tmp)).hexdigest())
    print("output = ",output)
    counter += 1
    print("\n\n\n")
  return output[:length]





seed= 'aafd12f659cae63489b479e5076ddec2f06cb58f00000000'

b =  bytes(seed, 'utf-8')
print(" b = ", b)
print(" hash  = ", hashlib.sha1(b).hexdigest())

b =  bytes(seed, 'ascii')
print(" b = ", b)
print(" hash  = ", hashlib.sha1(b).hexdigest())


print(" hash  = ", hashlib.sha1(bytes.fromhex(seed)).hexdigest())
dmMask = mgf1(seed,107,hashlib.sha1)
#print(type(dmMask))
print(dmMask)


