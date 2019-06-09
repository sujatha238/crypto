num = int(input("enter any positive number to check whether it is prime or not ;"))
if num>1:
    for i in range(2,num):
        if(num % i) == 0:
            print("i = ",i)
            break
    i= i+1
    if (i == num):
        print(num, "is a prime number")
    else:
        print(num, "num is no t a prime number")

#else:
#    print(num, "is less than 1")
