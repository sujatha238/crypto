
# Carmichael Numbers 561, 1105, 1729, 2465, 2821, 6601, 8911

p = 29 

for a in range(1,p):
    print(a,"^",(p-1)," mod",p," = ",pow(a,(p-1),p))

#https://crypto.stanford.edu/pbc/notes/numbertheory/


