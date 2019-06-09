mod = int(input("enter the any number;"))
for x in range(1,mod):
    print(x)
    for i in range(1,mod): 
        print(x,"*","*",i,"%",mod,"=",(x**i)%mod)
