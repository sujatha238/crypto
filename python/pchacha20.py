#! /bin/python3.6

def rotate(input, value):
    return ((input << value) & 0xffffffff | (input >> (32 - value)))

def print_all_state(state):
    print("\n")
    for i in range(16):
        print_int_in_hex(state[i], 4)
        if((i+1)%4 == 0):
            print("\n")
    return

def int_state_to_byte_array(state):
    byte_a = int.to_bytes(state[0], 4, "little")
    for i in range(1, 16):
        byte_a = byte_a + int.to_bytes(state[i], 4, "little")
    return byte_a

def qround(s, a, b, c, d):

    s[a] = (s[a] + s[b]) & 0xffffffff
    s[d] = s[d] ^ s[a]
    s[d] = rotate(s[d], 16)
    s[c] = (s[c] + s[d]) & 0xffffffff 
    s[b] = s[b] ^ s[c]
    s[b] = rotate(s[b], 12)
    s[a] = (s[a] + s[b]) & 0xffffffff 
    s[d] = s[d] ^ s[a]
    s[d] = rotate(s[d], 8)
    s[c] = (s[c] + s[d]) & 0xffffffff
    s[b] = s[b] ^ s[c]
    s[b] = rotate(s[b], 7)
    return s


def b_c(byte_input):
    return (int.from_bytes(byte_input, 'little', signed=False))

def inner_block (state):
    state = qround(state, 0, 4, 8,12)
    state = qround(state, 1, 5, 9,13)
    state = qround(state, 2, 6,10,14)
    state = qround(state, 3, 7,11,15)
    state = qround(state, 0, 5,10,15)   #row round
    state = qround(state, 1, 6,11,12)
    state = qround(state, 2, 7, 8,13)
    state = qround(state, 3, 4, 9,14)
    return state


constants = bytes.fromhex("617078653320646e79622d326b206574")
def chacha20_block(key, int_counter, nonce):
    counter = int.to_bytes(int_counter, 4, "little")

    byte_state = constants + key + counter + nonce   #concatination
    state = [b_c(byte_state[0:4][::-1]), 
            b_c(byte_state[4:8][::-1]), 
            b_c(byte_state[8:12][::-1]), 
            b_c(byte_state[12:16][::-1]),
            b_c(byte_state[16:20]), 
            b_c(byte_state[20:24]), 
            b_c(byte_state[24:28]), 
            b_c(byte_state[28:32]),
            b_c(byte_state[32:36]), 
            b_c(byte_state[36:40]), 
            b_c(byte_state[40:44]), 
            b_c(byte_state[44:48]),
            b_c(byte_state[48:52]), 
            b_c(byte_state[52:56]), 
            b_c(byte_state[56:60]), 
            b_c(byte_state[60:64])]

    working_state = state[:]

    for i in range(10):         # 10 rounds
        working_state = inner_block(working_state)

    #Add inital state to final state
    final_state = [0] * 20
    for i in range(16):
        final_state[i] = (state[i] + working_state[i]) & 0xffffffff

    key_stream = int_state_to_byte_array(final_state)
    return (key_stream)

def print_int_in_hex(input, len):
    print(int.to_bytes(input, len, "little").hex(), end=' ')


def chacha20_encryption(plaintext, key, nonce):
    length = len(plaintext)
    cipher = [0] * (length)
    counter = 1
    
    for i in range((length+64)//64):
    
        key_stream = chacha20_block(key, counter, nonce)
        if(length > 64):
            blocksize = 64 
        else:
            blocksize = length 
        length = length - blocksize
    
        for ii in range(blocksize):
            cipher[(i*64)+ii] = plaintext[(i*64)+ii] ^ key_stream[ii]
        counter = counter + 1
    return(bytearray(cipher))


















### Test vector from RFC-7539
Plaintext = "4c616469657320616e642047656e746c656d656e206f662074686520636c617373206f66202739393a204966204920636f756c64206f6666657220796f75206f6e6c79206f6e652074697020666f7220746865206675747572652c2073756e73637265656e20776f756c642062652069742e"
Key = "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f"
Nonce = "000000000000004a00000000"

plaintext = bytes.fromhex(Plaintext)
nonce = bytes.fromhex(Nonce)
key = bytes.fromhex(Key)
    

cipher_bytes = chacha20_encryption(plaintext, key, nonce)
print("cipher : ", cipher_bytes.hex())
cipher_bytes = chacha20_encryption(cipher_bytes, key, nonce)
print("Plaintext : ", cipher_bytes.hex())

