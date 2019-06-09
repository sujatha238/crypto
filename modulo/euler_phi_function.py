
from modulo_lib import *


n =9
count = 0


for x in range(1,n):
    if(gcd(x,n) == 1):
       count = count +1
       print(x)

print(" Euler phi(",n,") = ",count)



for x in range(1,n):
    if(gcd(x,n) == 1):
        print(x,"^phi(",n,") = ",x,"^",count," = ",pow(x,count,n))




for x in range(1,n):
    if(gcd(x,n) == 1):
       print("inverse(",x,") = ",pow(x,count-1,n))
 #       print(x,"^phi(",(n-1),"),mod",x,",=", pow(x,count-1,n))


