# Importing hashlib
# The Python hashlib module is an interface for hashing messages easily. The core purpose of this module is to use a hash function on a string, and encrypt it so that it
# Is very difficult to decrypt it.
import hashlib

# Here we collect the string we would like to hash and also we collect our salt
hashh = input("Enter any string you would like to hash: ")
salt = input("Enter your salt string here: ")
hashh = hashh + salt
# Combining our hashh and salt

# Below we will be encoding our hash and hashing it.
hashh = hashh.encode()
output = hashlib.sha256(hashh)
# Displaying the result result of our sha256 hash algorithm.
print("Hashed input displayed:- ")
print(output.digest())
