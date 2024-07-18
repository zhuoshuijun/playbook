from passlib.hash import sha512_crypt


test = "Test@ABC#ARMS*stp"

pwd = sha512_crypt.hash(test)
print(pwd)