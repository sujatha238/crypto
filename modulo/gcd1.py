a=int(input("enter the number:"))
b=int(input("enter the number:"))
print("a =",a,"b =",b)
x=b%a
print("x =",x)
while(x !=0):
    print("a =",a,"b =",b," x =",x)
    b=a
    print("b after swap =",b)
    a=x
    print("a after swap =",a)
    x=b%a
    print(" after swap x =b%a =",x)
print("gcd =",a)


