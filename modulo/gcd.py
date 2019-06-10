#! /usr/bin/python



import sys
from modulo_lib import*
lineno = 0
b=0
e=0
m=0
result=0

print("\n\n Usage: python3.7  gcd.py < gcd.\n")
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
    b = int(fields[0],16)
    e = int(fields[1],16)
  #  m = int(fields[2],16)
    print("typeof(b) = ", type(b))
    print("typeof(e) = ", type(e))
   # print("typeof(m) = ", type(m))
    print(" b = ", hex(b))
    print(" e = ", hex(e))
    #e = e >> 1
    #print(" e >> 1 = ", hex(e))
    #print(" m = ", hex(m))
    
  #  import modulo_lib.py
    result = gcd(b,e)

    print(" Result = ",hex(result))
    print(" -------------------------------------------------------------------------------------------")
print()




