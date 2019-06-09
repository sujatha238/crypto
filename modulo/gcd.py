a = 104729
b = 27000
print("a = ", a, ",b = ",b)
p = b%a
print("x = ", x)
while(x != 0):
    # x = remainder,  a 
    # b <<--a
    # a <<-- x
    print("x = ", x, ",a = ", a, ",b = ",b)
    b = a
    a = x
    print("after swap a = ", a, ",b = ",b)
    x = b%a
    print("after x = b%a = ",x)
print("gcd = ",a)



