import string
import random
chars = " "+string.punctuation+string.digits+string.ascii_letters
# print(chars)
chars = list(chars)
key = chars.copy()
random.shuffle(key)
# print(f"chars:{chars}")
# print(f"key:{key}")
plain = input("Enter your message for encryption : ")
cipher = " "

for letter in plain:
    index=chars.index(letter)
    cipher+=key[index]
# print(f"Original message: {plain}")
print(f"Encrypted message : {cipher}")

cipher = input("Enter your encrypted message for decryption : ")
plain = " "
for letter in cipher:
    index=key.index(letter)
    plain+=chars[index]
# print(f"encrypted:{cipher}")
print(f"Original message : {plain}")
