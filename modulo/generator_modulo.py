

p = 11 
for a in range(1,p):
    #print(a,"^2 mod",p," = ",(pow(a,2,p)))

    for x in range(1,p):
        print(a,"^",x,"mod",p," = ", pow(a,x,p))
    print();

#https://crypto.stanford.edu/pbc/notes/numbertheory/


