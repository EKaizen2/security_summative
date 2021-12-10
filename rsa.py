try:
   input = input
except NameError:
   pass
try:
   chr = chr
except NameError:
   pass
p=int(input("Enter a one prime number eg 17, 19, 23, etc: "))
q=int(input("Enter another prime number but not one you entered above: "))
print("Choosen primes:\np=" + str(p) + ", q=" + str(q) + "\n")
n=p*q
print("n = " + str(n) + "\n")
phi=(p-1)*(q-1)
# print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l
print("Please select your e from the array below:\n")
print(str(coprimes(phi)) + "\n")
e=int(input())
d=modinv(e,phi)
print("\nHere are your public keys (e=" + str(e) + ", n=" + str(n) + ").\n")
print("Here are your private keys (d=" + str(d) + ", n=" + str(n) + ").\n")
def encrypt_block(m):
    c = modinv(m**e, n)
    if c == None: print('No modular multiplicative inverse for block ' + str(m) + '.')
    return c
def decrypt_block(c):
    m = modinv(c**d, n)
    if m == None: print('No modular multiplicative inverse for block ' + str(c) + '.')
    return m
def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
s = input("Enter the message you would like to encrypt: ")
print("\nHere is your plain message: " + s + "\n")
enc = encrypt_string(s)
print("Here is your encrypted message: " + enc + "\n")
dec = decrypt_string(enc)
print("Here is your decrypted message: " + dec + "\n")
