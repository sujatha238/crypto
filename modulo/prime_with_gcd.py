
from modulo_lib import *

num = int(input("enter any positive number to check whether it is prime or not ;"))
if num>1:
    for i in range(2,num):
        if(gcd(i,num) != 1):
            print("i",i)
            break
# for in loop range means last num not taken num-1 taken after end of the loop  we use i = i+1 that way it take give to the if condition to check for prime or not
    i= i+1
    print("i",i)
    if (i == num):
        print(num, "is a prime number")
    else:
       # print("i",i)
        print(num, "num is no t a prime number")

else:
    print(num, "is less than 1")

