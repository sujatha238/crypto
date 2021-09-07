

debug = 1

def mont_recover_y(u,p):
    minus_u = -u % p
    if(debug):
        print("\n")
        print("     decimal         u = ",u)
        print(" hexadecimal         u = ",hex(u))
        print("     decimal   minus_u = ",minus_u)
        print(" hexadecimal   minus_u = ",hex(minus_u))
    
    u3 = (u*u*u)%p
    Au2 = (486662*u*u)%p
    u_result = (u3 + Au2 + u)%p
    sqrt_u  = sqrt_25519(u_result)
    v = sqrt_u
    v = -v%p
    minus_v = -v%p
    if(debug):
        print("\n")
        print(" After recoring v from u through  v^2 = u^3 + Au^2 + u    : ")
        print("     decimal          v = ",v)
        print(" hexadecimal          v = ",hex(v))
        print("     decimal    minus_v = ",minus_v)
        print(" hexadecimal    minus_v = ",hex(minus_v))
        print("\n")
    return(minus_v)



#/*
# **  Syntax:
# **    curve25519_ladder_step()
# ** 
# **  Description:
# **
# **  (Initially only)
# **  X1 <------  1
# **  Z1 <------  0
# **  X2 <------  xP (original x-coordinate)
# **  Z2 <------  1
# **
# **    This subroutine does the ladderstep of curve25519 of a point (X1,Z1) 
# **    and (X2,Z2) with xP(original x-coordinate)
# **    The resulting (X1, Z1) has Double Result and  (X2, Z2) has Add Result.
# **    
# **  Inputs:
# **    X1,Z1,X2,Z2 and xP(original x-coordinate) 
# **    PRIME 2^255  - 19  
# **     
# **  Output:
# **    X1,Z1,X2,Z2   i.e (X1,Z1) has Double Result,  (X2,Z2) has Add Result. 
# **   
# **  Registers Modified:
# **    All
# ** 
# **  Implementation Algorithm: 
#     Ladder Step: http://cr.yp.to/ecdh/curve25519-20060209.pdf
#
 	
def x25519_ladder_step(X1,Z1,X2,Z2,xP,A24,p):
    T1 = (X2  +  Z2  )%p  
    X2 = (X2  -  Z2  )%p  
    Z2 = (X1  +  Z1  )%p  
    X1 = (X1  -  Z1  )%p  
    T1 = (T1  *  X1  )%p  
    X2 = (X2  *  Z2  )%p  
    Z2 = (Z2  *  Z2  )%p  
    X1 = (X1  *  X1  )%p  
    T2 = (Z2  -  X1  )%p  
    Z1 = (T2  *  A24 )%p   
    Z1 = (Z1  +  X1  )%p  
    Z1 = (T2  *  Z1  )%p  
    X1 = (Z2  *  X1  )%p  
    Z2 = (T1  -  X2  )%p  
    Z2 = (Z2  *  Z2  )%p  
    Z2 = (Z2  *  xP  )%p  
    X2 = (T1  +  X2  )%p  
    X2 = (X2  *  X2  )%p  
    return(X1,Z1,X2,Z2)


def cswap(a,b,c):
    #tmp <---- X1
    #X1  <---- X2
    #X2  <---- tmp
    #print(" c = ", c)
    if(c == 1):
        #print(" inside c = ", c)
        tmp = a
        a = b
        b = tmp
    return(a,b)

def mask(swap):
    if(swap == 0):
        return(0)
    else:
        return(2**255 - 1)

def RFC_7748_cswap(swap, x_2, x_3):
         if(debug):
             print("\n --------------- in RFC_7748_cswap --- start \n")
         dummy = mask(swap) & (x_2 ^ x_3)
         if(debug):
             print("dummy = ", hex(dummy))
             print("b4 XOR dummy, \n x_2 =  ",hex(x_2), "\n x_3 = ",hex(x_3))
         x_2 = x_2 ^ dummy
         x_3 = x_3 ^ dummy
         if(debug):
             print("after XOR dummy,\n  x_2 =  ",hex(x_2), "\n x_3 = ",hex(x_3))
             print("\n --------------- in RFC_7748_cswap --- end \n")
         return (x_2, x_3)

def RFC_7748_ecc_mul_x25519(x1,scalar, A24, p):

    print("------- in RFC_7748_ecc_mul_x25519 ---")
    # mask scalar
    # clear 255-th bit, and set 254-th bit
    #print(" b4 mask scalar : ",hex(scalar))
    mask1 = 0x4000000000000000000000000000000000000000000000000000000000000000
    mask2 = 0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8
    scalar = scalar | mask1
    scalar = scalar & mask2
    print(" after mask scalar : ",hex(scalar))

    x_1 = x1
    x_2 = 1
    z_2 = 0
    x_3 = x1
    z_3 = 1
    swap = 0

    k = scalar
    i = 254
    if(debug):
        print("x_1 = ",hex(x_1))
        print("x_2 = ",hex(x_2))
        print("z_2 = ",hex(z_2))
        print("x_3 = ",hex(x_3))
        print("z_3 = ",hex(z_3))
    while (i>=0):
        k_t = (k >> i) & 1
        swap ^= k_t
        if(debug):
            print(" i = ",i," k_t = ", k_t, " swap = ", swap)
            #print(" scalar ", k)
        # Conditional swap; see text below.
        if(debug):
            print("b4 cswap(x_2,x_3) and cswap(z_2,z_3) : ")
            print(" x_2 = ",hex(x_2))
            print(" x_3 = ",hex(x_3))
            print(" z_2 = ",hex(z_2))
            print(" z_3 = ",hex(z_3))
        (x_2, x_3) = RFC_7748_cswap(swap, x_2, x_3)
        (z_2, z_3) = RFC_7748_cswap(swap, z_2, z_3)
        if(debug):
            print("after cswap(x_2,x_3) and cswap(z_2,z_3) : ")
            print(" x_2 = ",hex(x_2))
            print(" x_3 = ",hex(x_3))
            print(" z_2 = ",hex(z_2))
            print(" z_3 = ",hex(z_3))
        swap = k_t

        A = (x_2 + z_2)%p
        AA = (A**2)%p
        B = (x_2 - z_2)%p
        BB = (B**2)%p
        E = (AA - BB)%p
        C = (x_3 + z_3)%p
        D = (x_3 - z_3)%p
        DA = (D * A)%p
        CB = (C * B)%p
        x_3 = ((DA + CB)**2)%p
        z_3 = (x_1 * (DA - CB)**2)%p
        x_2 = (AA * BB)%p
        z_2 = (E * (AA + (A24 * E)))%p


        if(debug):
            print(" -----------------loop i = ",i)
        i = i - 1

    # Conditional swap; see text below.
    (x_2, x_3) = RFC_7748_cswap(swap, x_2, x_3)
    (z_2, z_3) = RFC_7748_cswap(swap, z_2, z_3)
    return (x_2,z_2)




def ecc_mul_x25519(x1,scalar, A24, p):
    # mask scalar
    # clear 255-th bit, and set 254-th bit
    #print(" b4 mask scalar : ",hex(scalar))
    mask1 = 0x4000000000000000000000000000000000000000000000000000000000000000
    mask2 = 0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8
    scalar = scalar | mask1
    scalar = scalar & mask2
    print(" after mask scalar : ",hex(scalar))
    X1 = 1
    Z1 = 0
    X2 = x1
    Z2 = 1
    pp = 0
    i = 254
    if(debug):
        print(" Before cswap i = ",i," iteration, ladder_step has X1,Z1,X2,Z2 : ")
        print(" X1 : ",hex(X1))
        print(" Z1 : ",hex(Z1))
        print(" X2 : ",hex(X2))
        print(" Z2 : ",hex(Z2))
        print(" xP : ",hex(x1))
    while (i>=0):
        b = ((scalar>>i)&1)
        c = b ^ pp
        if(debug):
            print(" scalar>>",i,"&1, ---------b = ",b,"     c= ",c, "   pp=",pp);
        pp = b
        X1,X2 = cswap(X1,X2,c)
        Z1,Z2 = cswap(Z1,Z2,c)
        if(debug):
            print(" Before Ladder Step i = ",i," iteration, ladder_step has X1,Z1,X2,Z2 : ")
            print(" X1 : ",hex(X1))
            print(" Z1 : ",hex(Z1))
            print(" X2 : ",hex(X2))
            print(" Z2 : ",hex(Z2))
            print(" xP : ",hex(x1))
        X1,Z1,X2,Z2 = x25519_ladder_step(X1,Z1,X2,Z2,x1,A24,p)
        if(debug):
            print(" After Ladder Step i = ",i," iteration, ladder_step has X1,Z1,X2,Z2 : ")
            print(" X1 : ",hex(X1))
            print(" Z1 : ",hex(Z1))
            print(" X2 : ",hex(X2))
            print(" Z2 : ",hex(Z2))
        i = i - 1
    return(X1,Z1)

def ecc_mul_x25519_no_mask(x1,scalar, A24, p):
    # mask scalar
    # clear 255-th bit, and set 254-th bit
    #print(" b4 mask scalar : ",hex(scalar))
    print(" after mask scalar : ",hex(scalar))
    X1 = 1
    Z1 = 0
    X2 = x1
    Z2 = 1
    pp = 0
    i = scalar.bit_length()
    if(debug):
        print(" i = scalar.bit_length() = ",i)
    while(((scalar>>i)&1) == 0):
        i = i - 1;
    if(debug):
        print(" Before cswap i = ",i," iteration, ladder_step has X1,Z1,X2,Z2 : ")
        print(" X1 : ",hex(X1))
        print(" Z1 : ",hex(Z1))
        print(" X2 : ",hex(X2))
        print(" Z2 : ",hex(Z2))
        print(" xP : ",hex(x1))
    while (i>=0):
        if(debug):
            print(" i = ",i)
            print(" scalar  = ",hex(scalar))
        b = ((scalar>>i)&1)
        c = b ^ pp
        pp = b
        X1,X2 = cswap(X1,X2,c)
        Z1,Z2 = cswap(Z1,Z2,c)
        if(debug):
            print(" scalar",i,"&1, ---------b = ",b,"     c= ",c, "   pp=",pp);
            print(" Before Ladder Step i = ",i," iteration, ladder_step has X1,Z1,X2,Z2 : ")
            print(" X1 : ",hex(X1))
            print(" Z1 : ",hex(Z1))
            print(" X2 : ",hex(X2))
            print(" Z2 : ",hex(Z2))
            print(" xP : ",hex(x1))
        X1,Z1,X2,Z2 = x25519_ladder_step(X1,Z1,X2,Z2,x1,A24,p)
        if(debug):
            print(" After Ladder Step i = ",i," iteration, ladder_step has X1,Z1,X2,Z2 : ")
            print(" X1 : ",hex(X1))
            print(" Z1 : ",hex(Z1))
            print(" X2 : ",hex(X2))
            print(" Z2 : ",hex(Z2))
        i = i - 1

    return(X1,Z1)



def ecc_mul_x448(x1,scalar, A24, p):
    # mask scalar
    # set 447-th bit, and clear 1,0th bits 
    #print(" b4 mask scalar : ",hex(scalar))
    mask1 = 0x8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    mask2 = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc
    scalar = scalar | mask1
    scalar = scalar & mask2
    #print(" after mask scalar : ",hex(scalar))
    X1 = 1
    Z1 = 0
    X2 = x1
    Z2 = 1
    pp = 0
    i = 447
    while (i>=0):
        b = ((scalar>>i)&1)
        c = b ^ pp
        #print(" scalar>>",i,"&1, ---------b = ",b,"     c= ",c, "   pp=",pp);
        pp = b
        X1,X2 = cswap(X1,X2,c)
        Z1,Z2 = cswap(Z1,Z2,c)
        X1,Z1,X2,Z2 = x25519_ladder_step(X1,Z1,X2,Z2,x1,A24,p)
        #print(" after i = ",i," iteration, ladder_step has X1,Z1,X2,Z2 : ")
        #print(hex(X1))
        #print(hex(Z1))
        #print(hex(X2))
        #print(hex(Z2))
        i = i - 1
    return(X1,Z1)



# from RFC-8032, Sec. 5.1.1
def sqrt_25519(a):
    p = 2**255 - 19
    #print("\n ---------------------------------------")
    minus_a = -a % p
    x = pow(a, (p+3)//8, p)
    x2 = (x*x) % p
    if(debug):
        print(" a : ",hex(a))
        print(" -a : ",hex(minus_a))
        print(" x = a ^ (p+3)//8 mod p  : ",hex(x))
        print(" x^2 : ",hex(x2))
    if  x2 == a:
        if(debug):
            print(" x^2 == a : ")
        sqrt_x = x
    elif x2 == minus_a:
        if(debug):
            print(" x^2 == -a : ")
            print(" sqrt_x = (pow(2,(p-1)//4,p)*x)%p ")
        sqrt_x = (pow(2,(p-1)//4,p)*x)%p
    return sqrt_x

