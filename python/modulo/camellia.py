

#ROTL64(x,n)  =  SHL64(x,n) | SHR(x,(64-n))
#ROTL32(x,n)  =  SHL32(x,n) | SHR(x,(32-n))
#ROTL16(x,n)  =  SHL16(x,n) | SHR(x,(16-n))
#ROTL8(x,n)   =  SHL8(x,n)  | SHR(x,(8-n))

MASK8   = 0xff
MASK32  = 0xffffffff
MASK64  = 0xffffffffffffffff
MASK128 = 0xffffffffffffffffffffffffffffffff

def rotl_128(x,n):
    return( ((x<<n)&MASK128) | (x >> (128-n)))

def rotl_64(x,n):
    return( ((x<<n)&MASK64) | (x >> (64-n)))

def rotl_32(x,n):
    return( ((x<<n)&MASK32) | (x >> (32-n)))

def rotl_8(x,n):
    return( ((x<<n)&MASK8) | (x >> (8-n)))


'''   0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f'''
SBOX1 =  \
   [
        0x70, 0x82, 0x2c, 0xec, 0xb3, 0x27, 0xc0, 0xe5, 
        0xe4, 0x85, 0x57, 0x35, 0xea, 0x0c, 0xae, 0x41, 
        0x23, 0xef, 0x6b, 0x93, 0x45, 0x19, 0xa5, 0x21, 
        0xed, 0x0e, 0x4f, 0x4e, 0x1d, 0x65, 0x92, 0xbd, 
        0x86, 0xb8, 0xaf, 0x8f, 0x7c, 0xeb, 0x1f, 0xce, 
        0x3e, 0x30, 0xdc, 0x5f, 0x5e, 0xc5, 0x0b, 0x1a, 
        0xa6, 0xe1, 0x39, 0xca, 0xd5, 0x47, 0x5d, 0x3d, 
        0xd9, 0x01, 0x5a, 0xd6, 0x51, 0x56, 0x6c, 0x4d, 
        0x8b, 0x0d, 0x9a, 0x66, 0xfb, 0xcc, 0xb0, 0x2d, 
        0x74, 0x12, 0x2b, 0x20, 0xf0, 0xb1, 0x84, 0x99, 
        0xdf, 0x4c, 0xcb, 0xc2, 0x34, 0x7e, 0x76, 0x05, 
        0x6d, 0xb7, 0xa9, 0x31, 0xd1, 0x17, 0x04, 0xd7, 
        0x14, 0x58, 0x3a, 0x61, 0xde, 0x1b, 0x11, 0x1c, 
        0x32, 0x0f, 0x9c, 0x16, 0x53, 0x18, 0xf2, 0x22, 
        0xfe, 0x44, 0xcf, 0xb2, 0xc3, 0xb5, 0x7a, 0x91, 
        0x24, 0x08, 0xe8, 0xa8, 0x60, 0xfc, 0x69, 0x50, 
        0xaa, 0xd0, 0xa0, 0x7d, 0xa1, 0x89, 0x62, 0x97, 
        0x54, 0x5b, 0x1e, 0x95, 0xe0, 0xff, 0x64, 0xd2, 
        0x10, 0xc4, 0x00, 0x48, 0xa3, 0xf7, 0x75, 0xdb, 
        0x8a, 0x03, 0xe6, 0xda, 0x09, 0x3f, 0xdd, 0x94, 
        0x87, 0x5c, 0x83, 0x02, 0xcd, 0x4a, 0x90, 0x33, 
        0x73, 0x67, 0xf6, 0xf3, 0x9d, 0x7f, 0xbf, 0xe2, 
        0x52, 0x9b, 0xd8, 0x26, 0xc8, 0x37, 0xc6, 0x3b, 
        0x81, 0x96, 0x6f, 0x4b, 0x13, 0xbe, 0x63, 0x2e, 
        0xe9, 0x79, 0xa7, 0x8c, 0x9f, 0x6e, 0xbc, 0x8e, 
        0x29, 0xf5, 0xf9, 0xb6, 0x2f, 0xfd, 0xb4, 0x59, 
        0x78, 0x98, 0x06, 0x6a, 0xe7, 0x46, 0x71, 0xba, 
        0xd4, 0x25, 0xab, 0x42, 0x88, 0xa2, 0x8d, 0xfa, 
        0x72, 0x07, 0xb9, 0x55, 0xf8, 0xee, 0xac, 0x0a, 
        0x36, 0x49, 0x2a, 0x68, 0x3c, 0x38, 0xf1, 0xa4, 
        0x40, 0x28, 0xd3, 0x7b, 0xbb, 0xc9, 0x43, 0xc1, 
        0x15, 0xe3, 0xad, 0xf4, 0x77, 0xc7, 0x80, 0x9e 
   ]
#   [112,130, 44,236,179, 39,192,229,228,133, 87, 53,234, 12,174, 65,     
#     35,239,107,147, 69, 25,165, 33,237, 14, 79, 78, 29,101,146,189,    
#    134,184,175,143,124,235, 31,206, 62, 48,220, 95, 94,197, 11, 26,    
#    166,225, 57,202,213, 71, 93, 61,217,  1, 90,214, 81, 86,108, 77,    
#    139, 13,154,102,251,204,176, 45,116, 18, 43, 32,240,177,132,153,    
#    223, 76,203,194, 52,126,118,  5,109,183,169, 49,209, 23,  4,215,    
#     20, 88, 58, 97,222, 27, 17, 28, 50, 15,156, 22, 83, 24,242, 34,    
#    254, 68,207,178,195,181,122,145, 36,  8,232,168, 96,252,105, 80,    
#    170,208,160,125,161,137, 98,151, 84, 91, 30,149,224,255,100,210,    
#     16,196,  0, 72,163,247,117,219,138,  3,230,218,  9, 63,221,148,    
#    135, 92,131,  2,205, 74,144, 51,115,103,246,243,157,127,191,226,    
#     82,155,216, 38,200, 55,198, 59,129,150,111, 75, 19,190, 99, 46,    
#    233,121,167,140,159,110,188,142, 41,245,249,182, 47,253,180, 89,    
#    120,152,  6,106,231, 70,113,186,212, 37,171, 66,136,162,141,250,    
#    114,  7,185, 85,248,238,172, 10, 54, 73, 42,104, 60, 56,241,164,    
#     64, 40,211,123,187,201, 67,193, 21,227,173,244,119,199,128,158    
#   ]


Sigma1 = 0xA09E667F3BCC908B
Sigma2 = 0xB67AE8584CAA73B2
Sigma3 = 0xC6EF372FE94F82BE
Sigma4 = 0x54FF53A5F1D36F1C
Sigma5 = 0x10E527FADE682D1D
Sigma6 = 0xB05688C2B3E6C1FD


#SBOX2[x] = SBOX1[x] <<< 1
#SBOX3[x] = SBOX1[x] <<< 7
#SBOX4[x] = SBOX1[x <<< 1]


def F(F_IN, KE):
    #x=0x0000000000000000 as 64-bit unsigned integer
    #t1, t2, t3, t4, t5, t6, t7, t8 as 8-bit unsigned integer
    #y1, y2, y3, y4, y5, y6, y7, y8 as 8-bit unsigned integer
    x  = F_IN ^ KE
    t1 =  x >> 56
    t2 = (x >> 48) & MASK8
    t3 = (x >> 40) & MASK8
    t4 = (x >> 32) & MASK8
    t5 = (x >> 24) & MASK8
    t6 = (x >> 16) & MASK8
    t7 = (x >>  8) & MASK8
    t8 =  x        & MASK8
    t1 = SBOX1[t1]
    t2 = rotl_8(SBOX1[t2],1)
    t3 = rotl_8(SBOX1[t3],7)
    t4 = SBOX1[rotl_8(t4,1)]
    t5 = rotl_8(SBOX1[t5],1)
    t6 = rotl_8(SBOX1[t6],7)
    t7 = SBOX1[rotl_8(t7,1)]
    t8 = SBOX1[t8]
    y1 = t1 ^ t3 ^ t4 ^ t6 ^ t7 ^ t8
    y2 = t1 ^ t2 ^ t4 ^ t5 ^ t7 ^ t8
    y3 = t1 ^ t2 ^ t3 ^ t5 ^ t6 ^ t8
    y4 = t2 ^ t3 ^ t4 ^ t5 ^ t6 ^ t7
    y5 = t1 ^ t2 ^ t6 ^ t7 ^ t8
    y6 = t2 ^ t3 ^ t5 ^ t7 ^ t8
    y7 = t3 ^ t4 ^ t5 ^ t6 ^ t8
    y8 = t1 ^ t4 ^ t5 ^ t6 ^ t7
    F_OUT = (y1 << 56) | (y2 << 48) | (y3 << 40) | (y4 << 32) \
    | (y5 << 24) | (y6 << 16) | (y7 <<  8) | y8
    return F_OUT



def FL(FL_IN, KE):
    #var x1, x2 as 32-bit unsigned integer
    #var k1, k2 as 32-bit unsigned integer
    print("\n-------------- FL() --------------------1\n")
    x1 = FL_IN >> 32
    x2 = FL_IN & MASK32
    print("\nx1 = ",hex(x1),"  x2 = ",hex(x2))
    k1 = KE >> 32
    k2 = KE & MASK32
    print("\nk1 = ",hex(k1),"  k2 = ",hex(k2))
    print("\n ((x1 & k1)) = ", hex(x1 & k1))
    print("\n (rotl_32((x1 & k1),1) = ", hex((rotl_32((x1 & k1),1))))
    x2 = x2 ^ (rotl_32((x1 & k1),1))
    x1 = x1 ^ (x2 | k2)
    print("\nx1 = ",hex(x1),"  x2 = ",hex(x2))
    FL_OUT = (x1 << 32) | x2
    print("\n FL_OUT = ",hex(FL_OUT))
    print("\n-------------- FL() --------------------2\n")
    return(FL_OUT)


def FLINV(FLINV_IN, KE):
    #var y1, y2 as 32-bit unsigned integer
    #var k1, k2 as 32-bit unsigned integer
    y1 = FLINV_IN >> 32
    y2 = FLINV_IN & MASK32
    k1 = KE >> 32
    k2 = KE & MASK32
    y1 = y1 ^ (y2 | k2)
    y2 = y2 ^ (rotl_32((y1 & k1),1))
    FLINV_OUT = (y1 << 32) | y2
    return(FLINV_OUT)





##   128-bit key K:
#KL = K;    KR = 0;
#
##   192-bit key K:
#KL = K >> 64;
#KR = ((K & MASK64) << 64) | (~(K & MASK64));
#
##   256-bit key K:
#KL = K >> 128;
#KR = K & MASK128;


def key_schedule_128(K):
    #   128-bit key K:
    KL = K
    KR = 0
    
    D1 = (KL ^ KR) >> 64
    D2 = (KL ^ KR) & MASK64
    D2 = D2 ^ F(D1, Sigma1)
    D1 = D1 ^ F(D2, Sigma2)
    D1 = D1 ^ (KL >> 64)
    D2 = D2 ^ (KL & MASK64)
    D2 = D2 ^ F(D1, Sigma3)
    D1 = D1 ^ F(D2, Sigma4)
    KA = (D1 << 64) | D2
    D1 = (KA ^ KR) >> 64
    D2 = (KA ^ KR) & MASK64
    D2 = D2 ^ F(D1, Sigma5)
    D1 = D1 ^ F(D2, Sigma6)
    KB = (D1 << 64) | D2
    print("KL = ",hex(KL))
    print("KR = ",hex(KR))
    print("KA = ",hex(KA))
    print("KB = ",hex(KB))

#For 128-bit keys, 64-bit subkeys kw1, ..., kw4, k1, ..., k18,
#   ke1, ..., ke4 are generated as follows.
#
#   kw1 = (KL <<<   0) >> 64;
#   kw2 = (KL <<<   0) & MASK64;
#   k1  = (KA <<<   0) >> 64;
#   k2  = (KA <<<   0) & MASK64;
#   k3  = (KL <<<  15) >> 64;
#   k4  = (KL <<<  15) & MASK64;
#   k5  = (KA <<<  15) >> 64;
#   k6  = (KA <<<  15) & MASK64;
#   ke1 = (KA <<<  30) >> 64;
#   ke2 = (KA <<<  30) & MASK64;
#   k7  = (KL <<<  45) >> 64;
#   k8  = (KL <<<  45) & MASK64;
#   k9  = (KA <<<  45) >> 64;
#   k10 = (KL <<<  60) & MASK64;
#   k11 = (KA <<<  60) >> 64;
#   k12 = (KA <<<  60) & MASK64;
#   ke3 = (KL <<<  77) >> 64;
#   ke4 = (KL <<<  77) & MASK64;
#   k13 = (KL <<<  94) >> 64;
#   k14 = (KL <<<  94) & MASK64;
#   k15 = (KA <<<  94) >> 64;
#   k16 = (KA <<<  94) & MASK64;
#   k17 = (KL <<< 111) >> 64;
#   k18 = (KL <<< 111) & MASK64;
#   kw3 = (KA <<< 111) >> 64;
#   kw4 = (KA <<< 111) & MASK64;


    kw1 = rotl_128(KL,  0) >> 64
    kw2 = rotl_128(KL,  0) & MASK64
    k1  = rotl_128(KA,  0) >> 64
    k2  = rotl_128(KA,  0) & MASK64
    k3  = rotl_128(KL, 15) >> 64
    k4  = rotl_128(KL, 15) & MASK64
    k5  = rotl_128(KA, 15) >> 64
    k6  = rotl_128(KA, 15) & MASK64
    ke1 = rotl_128(KA, 30) >> 64
    ke2 = rotl_128(KA, 30) & MASK64
    k7  = rotl_128(KL, 45) >> 64
    k8  = rotl_128(KL, 45) & MASK64
    k9  = rotl_128(KA, 45) >> 64
    k10 = rotl_128(KL, 60) & MASK64
    print("k9 = ",hex(k9))
    print("k10 = ",hex(k10))
    k11 = rotl_128(KA, 60) >> 64
    k12 = rotl_128(KA, 60) & MASK64
    ke3 = rotl_128(KL, 77) >> 64
    ke4 = rotl_128(KL, 77) & MASK64
    k13 = rotl_128(KL, 94) >> 64
    k14 = rotl_128(KL, 94) & MASK64
    k15 = rotl_128(KA, 94) >> 64
    k16 = rotl_128(KA, 94) & MASK64
    k17 = rotl_128(KL,111) >> 64
    k18 = rotl_128(KL,111) & MASK64
    kw3 = rotl_128(KA,111) >> 64
    kw4 = rotl_128(KA,111) & MASK64
    #print("k17 = ",hex(k17))
    #print("k18 = ",hex(k18))

    return(kw1,kw2,k1,k2,k3,k4,k5,k6,ke1,ke2,k7,k8,k9,k10,k11,k12,ke3,ke4,k13,k14,k15,k16,k17,k18,kw3,kw4)

def key_schedule_192_256(K):
    print(" key = ",hex(K))
    print(" K.bit_length() = ",K.bit_length())
    KR = 0
    if(K.bit_length() < 192):
        KL = K >> 64
        KR = (((K & MASK64) << 64) | (MASK64 ^(K & MASK64)))
    else:
        KL = K >> 128
        KR =  K & MASK128;

    D1 = (KL ^ KR) >> 64
    D2 = (KL ^ KR) & MASK64
    D2 = D2 ^ F(D1, Sigma1)
    D1 = D1 ^ F(D2, Sigma2)
    D1 = D1 ^ (KL >> 64)
    D2 = D2 ^ (KL & MASK64)
    D2 = D2 ^ F(D1, Sigma3)
    D1 = D1 ^ F(D2, Sigma4)
    KA = (D1 << 64) | D2
    D1 = (KA ^ KR) >> 64
    D2 = (KA ^ KR) & MASK64
    D2 = D2 ^ F(D1, Sigma5)
    D1 = D1 ^ F(D2, Sigma6)
    KB = (D1 << 64) | D2
    print("KL = ",hex(KL))
    print("KR = ",hex(KR))
    print("KA = ",hex(KA))
    print("KB = ",hex(KB))

    kw1 = rotl_128(KL,   0) >> 64;
    kw2 = rotl_128(KL,   0) & MASK64;
    k1  = rotl_128(KB,   0) >> 64;
    k2  = rotl_128(KB,   0) & MASK64;
    k3  = rotl_128(KR,  15) >> 64;
    k4  = rotl_128(KR,  15) & MASK64;
    k5  = rotl_128(KA,  15) >> 64;
    k6  = rotl_128(KA,  15) & MASK64;
    ke1 = rotl_128(KR,  30) >> 64;
    ke2 = rotl_128(KR,  30) & MASK64;
    k7  = rotl_128(KB,  30) >> 64;
    k8  = rotl_128(KB,  30) & MASK64;
    k9  = rotl_128(KL,  45) >> 64;
    k10 = rotl_128(KL,  45) & MASK64;
    k11 = rotl_128(KA,  45) >> 64;
    k12 = rotl_128(KA,  45) & MASK64;
    ke3 = rotl_128(KL,  60) >> 64;
    ke4 = rotl_128(KL,  60) & MASK64;
    k13 = rotl_128(KR,  60) >> 64;
    k14 = rotl_128(KR,  60) & MASK64;
    k15 = rotl_128(KB,  60) >> 64;
    k16 = rotl_128(KB,  60) & MASK64;
    k17 = rotl_128(KL,  77) >> 64;
    k18 = rotl_128(KL,  77) & MASK64;
    ke5 = rotl_128(KA,  77) >> 64;
    ke6 = rotl_128(KA,  77) & MASK64;
    k19 = rotl_128(KR,  94) >> 64;
    k20 = rotl_128(KR,  94) & MASK64;
    k21 = rotl_128(KA,  94) >> 64;
    k22 = rotl_128(KA,  94) & MASK64;
    k23 = rotl_128(KL, 111) >> 64;
    k24 = rotl_128(KL, 111) & MASK64;
    kw3 = rotl_128(KB, 111) >> 64;
    kw4 = rotl_128(KB, 111) & MASK64;
    return(kw1,kw2,k1,k2,k3,k4,k5,k6,ke1,ke2,k7,k8,k9,k10,k11,k12,ke3,ke4,k13,k14,k15,k16,k17,k18,ke5,ke6,k19,k20,k21,k22,k23,k24,kw3,kw4)


def camellia_encryption_128(M,\
        kw1,kw2,k1,k2,k3,k4,k5,k6,ke1,ke2,k7,k8,k9,k10,k11,k12,ke3,ke4,k13,k14,k15,k16,k17,k18,kw3,kw4):

    print("\n------------------Camellia Encryption---------------------------1\n")
    D1 = M >> 64;
    D2 = M & MASK64;
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))

    D1 = D1 ^ kw1;           #// Prewhitening
    D2 = D2 ^ kw2;
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k1);     #// Round 1
    D1 = D1 ^ F(D2, k2);     #// Round 2
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k3);     #// Round 3
    D1 = D1 ^ F(D2, k4);     #// Round 4
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k5);     #// Round 5
    D1 = D1 ^ F(D2, k6);     #// Round 6
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D1 = FL   (D1, ke1);     #// FL
    D2 = FLINV(D2, ke2);     #// FLINV
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k7);     #// Round 7
    D1 = D1 ^ F(D2, k8);     #// Round 8
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k9);     #// Round 9
    D1 = D1 ^ F(D2, k10);    #// Round 10
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k11);    #// Round 11
    D1 = D1 ^ F(D2, k12);    #// Round 12
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D1 = FL   (D1, ke3);     #// FL
    D2 = FLINV(D2, ke4);     #// FLINV
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k13);    #// Round 13
    D1 = D1 ^ F(D2, k14);    #// Round 14
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k15);    #// Round 15
    D1 = D1 ^ F(D2, k16);    #// Round 16
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k17);    #// Round 17
    D1 = D1 ^ F(D2, k18);    #// Round 18
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ kw3;           #// Postwhitening
    D1 = D1 ^ kw4;
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    C = (D2 << 64) | D1;

    print("\n------------------Camellia Encryption---------------------------2\n")
    return C


def camellia_encryption_192_256(M,\
        kw1,kw2,k1,k2,k3,k4,k5,k6,ke1,ke2,k7,k8,k9,k10,k11,k12,ke3,ke4,k13,k14,k15,k16,k17,k18,ke5,ke6,k19,k20,k21,k22,k23,k24,kw3,kw4):
    print("\n------------------Camellia Encryption---------------------------1\n")
    D1 = M >> 64;
    D2 = M & MASK64
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))

    D1 = D1 ^ kw1;           #// Prewhitening
    D2 = D2 ^ kw2;
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k1);     #// Round 1
    D1 = D1 ^ F(D2, k2);     #// Round 2
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k3);     #// Round 3
    D1 = D1 ^ F(D2, k4);     #// Round 4
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k5);     #// Round 5
    D1 = D1 ^ F(D2, k6);     #// Round 6
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D1 = FL   (D1, ke1);     #// FL
    D2 = FLINV(D2, ke2);     #// FLINV
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k7);     #// Round 7
    D1 = D1 ^ F(D2, k8);     #// Round 8
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k9);     #// Round 9
    D1 = D1 ^ F(D2, k10);    #// Round 10
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k11);    #// Round 11
    D1 = D1 ^ F(D2, k12);    #// Round 12
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D1 = FL   (D1, ke3);     #// FL
    D2 = FLINV(D2, ke4);     #// FLINV
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k13);    #// Round 13
    D1 = D1 ^ F(D2, k14);    #// Round 14
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k15);    #// Round 15
    D1 = D1 ^ F(D2, k16);    #// Round 16
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k17);    #// Round 17
    D1 = D1 ^ F(D2, k18);    #// Round 18
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D1 = FL   (D1, ke5);     #// FL
    D2 = FLINV(D2, ke6);     #// FLINV
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k19);    #// Round 19
    D1 = D1 ^ F(D2, k20);    #// Round 20
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k21);    #// Round 21
    D1 = D1 ^ F(D2, k22);    #// Round 22
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ F(D1, k23);    #// Round 23
    D1 = D1 ^ F(D2, k24);    #// Round 24
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))
    D2 = D2 ^ kw3;           #// Postwhitening
    D1 = D1 ^ kw4;
    print("\n D1 = ",hex(D1),"  D2 = ",hex(D2))

    print("\n------------------Camellia Encryption---------------------------2\n")

    C = (D2 << 64) | D1;
    return C



print("---------Start----------------")
#   128-bit key
#       Key       : 01 23 45 67 89 ab cd ef fe dc ba 98 76 54 32 10
#       Plaintext : 01 23 45 67 89 ab cd ef fe dc ba 98 76 54 32 10
#       Ciphertext: 67 67 31 38 54 96 69 73 08 57 06 56 48 ea be 43

Key = 0x0123456789abcdeffedcba9876543210
M   = 0x0123456789abcdeffedcba9876543210
#M   = 0x000102030405060708090a0b0c0d0e0f
print(" Plaint Text = ",hex(M))
kw1,kw2,k1,k2,k3,k4,k5,k6,ke1,ke2,k7,k8,k9,k10,k11,k12,ke3,ke4,k13,k14,k15,k16,k17,k18,kw3,kw4=key_schedule_128(Key)
print("kw1 = ",hex(kw1),"  kw2 = ",hex(kw2))
print("k1 = ",hex(k1),"  k2 = ",hex(k2),"  k3 = ",hex(k3),"  k4 = ",hex(k4),"  k5 = ",hex(k5),"  k6 = ",hex(k6))
print("ke1 = ",hex(ke1),"  ke2 = ",hex(ke2))
print("k7 = ",hex(k7),"  k8 = ",hex(k8),"  k9 = ",hex(k9),"  k10 = ",hex(k10),"  k11 = ",hex(k11),"  k12 = ",hex(k12))
print("ke3 = ",hex(ke3),"  ke4 = ",hex(ke4))
print("k13 = ",hex(k13),"  k14 = ",hex(k14),"  k15 = ",hex(k15),"  k16 = ",hex(k16),"  k17 = ",hex(k17),"  k18 = ",hex(k18))
print("kw3 = ",hex(kw3),"  kw4 = ",hex(kw4))
C = camellia_encryption_128(M,kw1,kw2,k1,k2,k3,k4,k5,k6,ke1,ke2,k7,k8,k9,k10,k11,k12,ke3,ke4,k13,k14,k15,k16,k17,k18,kw3,kw4)
print(" Encrypted Cipher Text = ",hex(C))
M = 0x101112131415161718191a1b1c1d1e1f
C = camellia_encryption_128(M,kw1,kw2,k1,k2,k3,k4,k5,k6,ke1,ke2,k7,k8,k9,k10,k11,k12,ke3,ke4,k13,k14,k15,k16,k17,k18,kw3,kw4)
print(" Encrypted Cipher Text = ",hex(C))
# Decryption 128-bit key
#       kw1 <-> kw3
#       kw2 <-> kw4
#       k1  <-> k18
#       k2  <-> k17
#       k3  <-> k16
#       k4  <-> k15
#       k5  <-> k14
#       k6  <-> k13
#       k7  <-> k12
#       k8  <-> k11
#       k9  <-> k10
#       ke1 <-> ke4
#       ke2 <-> ke3

M = camellia_encryption_128(C,kw3,kw4,k18,k17,k16,k15,k14,k13,ke4,ke3,k12,k11,k10,k9,k8,k7,ke2,ke1,k6,k5,k4,k3,k2,k1,kw1,kw2)
print(" Decrypted Plain Text = ",hex(M))

#print("----------- done--------------")
#Key = 0xAE6852F8121067CC4BF7A5765577F39E
#M   = 0x00000030000000000000000000000001
#M   = 0x00000000000000000000000000000000
#print(" Plaint Text = ",hex(M))
#kw1,kw2,k1,k2,k3,k4,k5,k6,ke1,ke2,k7,k8,k9,k10,k11,k12,ke3,ke4,k13,k14,k15,k16,k17,k18,kw3,kw4=key_schedule_128(Key)
#C = camellia_encryption_128(M,kw1,kw2,k1,k2,k3,k4,k5,k6,ke1,ke2,k7,k8,k9,k10,k11,k12,ke3,ke4,k13,k14,k15,k16,k17,k18,kw3,kw4)
#print(" Encrypted Cipher Text = ",hex(C))

#i=0
#while (i<256):
#    print(i," ",(hex(SBOX1[i]))," ")
#    if(((i+1)%16) == 0):
#        print()
#    i = i + 1
print("--------------------------------------------------\n")
#Key = 0x0123456789abcdeffedcba98765432100011223344556677
Key = 0x0123456789abcdeffedcba987654321000112233445566778899aabbccddeeff
kw1,kw2,k1,k2,k3,k4,k5,k6,ke1,ke2,k7,k8,k9,k10,k11,k12,ke3,ke4,k13,k14,k15,k16,k17,k18,ke5,ke6,k19,k20,k21,k22,k23,k24,kw3,kw4=key_schedule_192_256(Key)
print("kw1 = ",hex(kw1),"  kw2 = ",hex(kw2))
print("k1 = ",hex(k1),"  k2 = ",hex(k2),"  k3 = ",hex(k3),"  k4 = ",hex(k4),"  k5 = ",hex(k5),"  k6 = ",hex(k6))
print("ke1 = ",hex(ke1),"  ke2 = ",hex(ke2))
print("k7 = ",hex(k7),"  k8 = ",hex(k8),"  k9 = ",hex(k9),"  k10 = ",hex(k10),"  k11 = ",hex(k11),"  k12 = ",hex(k12))
print("ke3 = ",hex(ke3),"  ke4 = ",hex(ke4))
print("k13 = ",hex(k13),"  k14 = ",hex(k14),"  k15 = ",hex(k15),"  k16 = ",hex(k16),"  k17 = ",hex(k17),"  k18 = ",hex(k18))
print("ke5 = ",hex(ke5),"  ke6 = ",hex(ke6))
print("k19 = ",hex(k19),"  k20 = ",hex(k20),"  k21 = ",hex(k21),"  k22 = ",hex(k22),"  k23 = ",hex(k23),"  k24 = ",hex(k24))
print("kw3 = ",hex(kw3),"  kw4 = ",hex(kw4))
M   = 0x0123456789abcdeffedcba9876543210
C = camellia_encryption_192_256(M,kw1,kw2,k1,k2,k3,k4,k5,k6,ke1,ke2,k7,k8,k9,k10,k11,k12,ke3,ke4,k13,k14,k15,k16,k17,k18,ke5,ke6,k19,k20,k21,k22,k23,k24,kw3,kw4)
print(" Plaint Text = ",hex(M))
print(" Encrypted Cipher Text = ",hex(C))

