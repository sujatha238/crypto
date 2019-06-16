
#debug=1

def gcd(a,b):
    x = b%a
    while(x != 0):
        # x = remainder,  a 
        # b <<--a
        # a <<-- x
        b = a
        a = x
        x = b%a
    return a



def binary_gcd(a,b):
    u = a
    v = b
    e = 1
    while (((u&1)==0) and ((v&1)==0)):
        u = u>>1
        v = v>>1
        e = e<<1
    
    while (u!=0):
        while((u&1)==0):
            u = u>>1
        while((v&1)==0):
            v = v>>1
        if (u>=v):
            u = u-v
        else:
            v = v-u
    return(e*v)


#def inversion_extended_Euclidean(a,p):
#    u = a
#    v = p
#    x1= 1
#    x2= 0
#    if(debug==1):
#        print("u = ",hex(u))
#        print("v = ",hex(v))
#        print("x1 = ",hex(x1))
#        print("x2 = ",hex(x2))
#        print("----------------------------")
#    while(u!=1):
#        q = u//v
#        if(debug == 1):
#            print("q = ", hex(q))
#
#        r = v-((q*u)%p)
#        if(debug == 1):
#            print("r = ", hex(r))
#
#        x = x2-((q*x1)%p)
#        if(debug == 1):
#            print("x = ", hex(x))
#
#        v = u
#        u = r
#        x2= x1
#        x1= x
#        if(debug==1):
#            print("u = ",hex(u))
#            print("v = ",hex(v))
#            print("x1 = ",hex(x1))
#            print("x2 = ",hex(x2))
#            print("---------------------------------------------------------------------------")
#
#    return(x1%p)
#











def binary_inversion(a,p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while((u!=1) and (v!=1)):
        while((u&1)==0):
            u = u>>1
            if((x1&1)==0):
                x1 = x1>>1
            else:
                x1 = (x1+p)>>1
        while ((v&1)==0):
            v= v>>1
            if((x2&1)==0):
                x2 = x2>>1
            else:
                x2 = (x2+p)>>1
        if(u>=v):
            u = u-v
            x1=x1-x2
        else:
            v =v-u
            x2=x2-x1
    if(u == 1):
        return(x1%p)
    else:
        return(x2%p)




