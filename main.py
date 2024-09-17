from Crypto.Cipher import AES



iv = "aaaaaaaaaaaaaaaa"
key = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
texto = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
cipher = AES.new (key,AES.MODE_CBC,iv)
ciphertext = cipher.encrypt(texto)
print(ciphertext.encode("hex"))
cipher = AES.new (key,AES.MODE_CBC,iv)
text = cipher.decrypt(ciphertext)
print(text.encode("hex"))