#! /usr/bin/python



import sys
from modulo_lib import*
lineno = 0
a=0
p=0
#m=0
result=0

print("\n\n Usage: python3.7  inverse.py < inverse.input \n")
while True:
    line = sys.stdin.readline()
    #print("typeof(line)) = ", type(line))
    #print("line =",line)
    if not line:
        break
    lineno = lineno + 1
    #print(lineno)
    if(line[0] == " "):
        continue

    if(line[0] == "\n"):
        continue

    if(line[0] == "#"):
        continue

    fields = line.split(":")
    print(" fields : ", fields)
    print("typeof(fields[0]) = ", type(fields[0]))
    print("typeof(fields[1]) = ", type(fields[1]))
    print(line[0:4])
    a = int(fields[0],16)
    p = int(fields[1],16)
  #  m = int(fields[2],16)
    print("typeof(a) = ", type(a))
    print("typeof(p) = ", type(p))
   # print("typeof(m) = ", type(m))
    print(" a = ", hex(a))
    print(" a = ", (a))
    print(" p = ", hex(p))
    #e = e >> 1
    #print(" e >> 1 = ", hex(e))
    #print(" m = ", hex(m))
    
  #  import modulo_lib.py
    result = binary_inversion(a,p)
    print(" Result = ",hex(result))
    result =pow(a,(p-2),p)
    print(" Result 2 = ",hex(result))
    print("a*a^-1 mod p =",(a*result)%p)
    print(" -------------------------------------------------------------------------------------------")
print()




