#p =14
# p = { 1, 2, 3, ..........., 65535, 65536}

# 1. Find gcd(a,p)
# 2. Find a^p mod p
# 3. Find a^p-1 mod p
# 4. Find a^p-2 mod p
# 5. Find a * (result of step 4) mod p ; and observe the result



mod=14
for a in range(1,mod):
    print(2,"*","*",14,"%",mod,"=",pow(2,mod,mod))
