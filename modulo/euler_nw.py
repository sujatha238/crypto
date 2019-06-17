from modulo_lib import*
n=15
nlist = []
#y=print(len(x))
for i in range (1,n):
    if(gcd(i,n)==1):
        nlist.append(i)
        print("nlist =",nlist)
        print(i)

print(" Euler phi(",n,") = ",len(nlist))





for i in nlist:
    if(gcd(i,n)==1):
       print("inverse,(",i,") = ",pow(i,(len(nlist)-1),n))

for i in  nlist:

    print(i)
    if(gcd (i,n)==1):
        print(i,"^",2,"%",n," = ", pow(i,2,n))


