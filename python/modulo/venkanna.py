

from modulo_lib import *



p = 5
q = 3

n = p * q


phi = (p-1)*(q-1)


shift_phi = phi >> 1
g = 7

if(gcd(g,phi) == 1):
    print("g = ",g,"  and phi = ",phi, "are coprime ")
else:
    print("g = ",g,"  and phi = ",phi, "are coprime ")


g_pow_sh_phi =  pow(g,shift_phi//2,n)

print("g_pow_sh_phi = ", g_pow_sh_phi)

g_pow_sh_phi += 1 

print("g_pow_sh_phi++ = ", g_pow_sh_phi)

g1 = g_pow_sh_phi%n
print("g1 = ", g1)



g_pow_sh_phi =  pow(g,shift_phi//2,n)

print("g_pow_sh_phi = ", g_pow_sh_phi)

g_pow_sh_phi -= 1 

print("g_pow_sh_phi++ = ", g_pow_sh_phi)

g2 = g_pow_sh_phi%n
print("g2 = ", g2)



g1 = gcd(g1, n)
print("g1 = ", g1)

g2 = gcd(g2, n)
print("g2 = ", g2)




