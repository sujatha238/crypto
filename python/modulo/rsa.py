

from modulo_lib import *


#e = 65537
#p = 0xfaa3bda5b5f0c65e736247b2b015cb5aeb5586dca229c680593470bdde74b843
#q = 0xfa919ba26783dcd0f25681f5dd577fb29ed396dfc33a9edc5180f6c61fabfecb

#p=0xbd4a47eb230ea9a8cef664b6be6e7f811fbd0009ed111fba5f98a748c1d95b9846cb5a5bf1b8bf376c4a5a4a610b2c5f78244f1786eced1f03e49056a62e961f
#q=0xc257cc8147515985a96c605c6faf2a8f76ed06060fe93191031d8c00d77cbd492a56ef86441c968d63bfee62eba72b3bba0ab9bb7d38b3f1c0303eb1bcc88b7f


p = 0xeb5b24b8c950355165b187c1cffb95c07dc942376401ce623100fbaebc59e45b69c22f9d9d26a0f7c0bd1ca4f7c1784ee24c3e0fa765b41b36ecec2417d193fb0f0cb4078211be0c91d6b5be290c1df7597d0951b71ca3a7378e53aae4b6a842ff7d18104388e48b115df1410d508ad9731378ce021b6b626a20a31daa43927728f0d352251e0813a52e28e70b915bc9aa907b4c9cdc6a0f06d2fcb0f72b39f1f10cc8514a707f72419c9891c239046dde4ee2316c72ef51e0c8a3bc92d471b6d250b46db0c23d255c6a849b186cfeecdd1a075e6c5da79e305b55b1173c71c000993585e020d65fff93f85df07c7ad44dc2c00d82aea82d9fdbc171dfdfd855
			
q = 0xfb0e83e72464164e49fb6bd19416c927086b1438d2e25bb07e867493ef3aba71ef395a2c3b39115552e61cb044aa832b00224f8adb48d5564816d72a3acf6d53737d25ed4ffd84065c41618c19ddd67e4fd5c808d402cfeef1ac8657b77a9707970eb5500efa10870f9eb8fcd7e3ccae5034bbe4ff96d66f9e4251590f1fbed223cb9c409ec84288f89e3474daf1b6c3c51fb9bd078b3f53a988d11a08b9b6503f13c57e54b3ead3bb0f3e7162923097e3623490ac8edac723ea300728210855d848af79c17b2cd042bbbb82711a039539e69caf4e4b858de37182f731106ac4803e79698a404df39eceb73ae66e2dd27c248e49997beda6675a4312d623cbb3

e = 65537 
#p=0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
#q=0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551

print()
print("p = ",hex(p))
print()
print("q = ",hex(q))
print()
print("e = ",hex(e))
n = p*q
print("n = p*q = ",hex(n))

p_1 = p-1
q_1 = q-1
print("p-1 = ",hex(p_1))
print("q-1 = ",hex(q_1))

mul_p_1__q_1 = p_1 * q_1
print("phi = mul_p_1__q_1 = (p-1)*(q-1) = \n ", hex(mul_p_1__q_1))
phi = mul_p_1__q_1

print(" n % p  = ", hex(n%p))
print(" n % q  = ", hex(n%q))


d = 0
print("gcd(e,n) = ", gcd(e,n))
#print(" n - phi  = ", n-phi)

co_prime = gcd(e,phi)
print("gcd(e,phi) = ",co_prime)

if(co_prime == 1):
    #d = { ((k*phi(n))+1)/e }
    
    d= extended_euclidean(e,phi)
    print("d = ",hex(d))
    
    ed = (e*d)%phi 
    print("e*d mod phi = ", hex(ed))
    print("\n\n\n------------------------------------------------------------")
    print("RSA public keys  n, e ")
    print("n = p*q = ",hex(n))
    print("e = ",hex(e))
    print("\n\n\nRSA private keys  n, d ")
    print("n = p*q = ",hex(n))
    print("d = ",hex(d))
    
    print("\n\nRSA encrypt :  c  = m^e  mod n  ")
    m=0xffff00000001000000000000000000000000ffffffffffffffffffffffff
    #m=0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
    m= 0xa22087dba332c9c0a57f082105ba49a2d0ef4798230c5120436823effe2786fb2321ee8500601316d241a73fb7dcecfd2434a40e6c53fce4bbe12d24ef0bc9fffb15574481d649684d1d8dcdc39dd2df97b0d8a8f5d8716e3c02d217dca372c1bf4fbc75e4646b94b1aa6932b72090c17a74623e64ebe4abb0834fb6db83d1b2d975179a21816c2622afd439d1a718994c0491b77911a3194fd7a960fdd1b55b2ab9ec9187287dd3d64fd1c2836166ac021dbb43a4b10cab07a401dff6fbf3ab8ca9496d532e91b56452c58c57fb569f8342f4e08dab18762b987d5dc9c1b123174f503ed0420745a8f31fdaad45c7ad4b86d88156810fabfd7f04dc951a6928d7c08eaa768147eb742f3935faec3c41a8e0a94bdd7c89f73c9e8630872ac397422336e0ed3c862a21cb8bae62519447338a9d7924e773910f9ddb7c888334ef9c2f58bf252468d05580d0ba95c009a92b8ab9785faa28f75378b52a3178756692c41d0acfaa3406a7dbef0d1d21dede185ec8d82d8fc1a61262254dcaef7641ca35e2b066067fbd424d08404d1891b9dba20870f3b63e894b268b5c150ac240ff89f1d9526c094bab171f5a93d0fba3b59d66975e7c6aac993ffd494aad0319845040e797ec00ca525516b8026ade5e0c6ef88e138b0e54eba610a8c4067216d9806e3ae95044d55a73817b370b572f4c14c69ef99a70eb4407e0efd6a17409
    m = 0x4556666f1657d7a24f1df38a46849b3e2339072b6a7847c44978f3cfbd14909c4030b4cb2b94151db3d01fb33be4bd0df58854234d3b9b03b9649567ce2df479af7a3b943b7ccc056781b6e3260ffc18d3657e11bed072c1d5f8e8a0c78e7b1d6defe6be038a52d57aa7215b48b37acd5656582b4440a3ee391c3bdef0d84f00dfd9f6075e6b761a14d3be456e26baa935667e8d43d6b524c8493fd63f9ff82e72dd7ebe3442990d17b603ca1f858f1f3a5afffd1bf7c9c18cbfdae5b3e20e4a4af900957cced70b1bb6b6e3601ddabbbe44f6e53facc2e8177d2ca3220ed0553586f7b26e31da1682b23ff20c7902ad05f46c6a669d0ed77dc641cb8dee71a4ec106c043ab79a9d86659f7a015cb63966473223c32cb82352c8df93f6ec4b90f3641f28bc51388f9e5ee29e480b0fc40acc6a19ebad1333402f6edd942e949a5de968e95c9fa5b8e4a052daa5ebf3557502827d5608ded50c33a7a91732756ecac6b720051f6fa0893f9c40b6c8db14965493bd456cac6ecff73c3058c49c183ad1431c1982e86b235341f2e8e96eff58cbca98fa7d33485dd7d6884a2d3692b283c3b0d0246c940388728dfd0d589796156f63d72a63e7a319528e632593aab578632cef48fcd82994400aabfdd9dbc3f2dd11360d36b558238904b30881a32cb826d62d40c4b110c3e02691c7c1fde0926ba6cdd1b9afa27194165aafe3bc

    print("m = ", hex(m))
    c = pow(m,d,n)
    print("c = ", hex(c))
    
    print("\n\nRSA decrypt :  m  = c^d  mod n  ")
    m1 = pow(c,e,n)
    print("recoverd_m = ", hex(m1))
else:
    print("\n e and phi are not co-prime \n")

print("------------------------------------------------------------")
print("------------------------------------------------------------")
print()


