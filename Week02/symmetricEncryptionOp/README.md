Perform symmetric encryption operation in the order below:
Find the right library that provide you with access to AES256 algorithm
Create and save your AES256 key
Create a string to test encryption
Perform AES256 symmetric encryption on the data to get cipher text
Use AES256 symmetric decryption on the cipher text to get original text
Use `assert` to check if decrypted data is the same as original string

free free to find the right library for the job

install with `pip3 install .....`
use chat gpt


Miller's tips
Step 1: Use terminal and install the right library pycryptodome
pip install pycryptodome

Step 2: Create an AES256 key and save it
with open('key.bin', 'wb') as f:
    f.write(key)

Step 3: Create a string to test encryption
from Crypto.Cipher import AES

with open('key.bin', 'rb') as f:
    key = f.read()

cipher = AES.new(key, AES.MODE_EAX)
plaintext = b''

ciphertext, tag = cipher.encrypt_and_digest(plaintext)


Step 4: Perform AES256 symmetric decryption on the cipher text