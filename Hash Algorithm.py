import hashlib

print("Enter a string:")
str2hash = input()
print ("\r")

result = hashlib.md5(b'str2hash')
print("The byte equivalent of MD5 hash is : ", end ="")
print(result.digest())
print ("\r")

result = hashlib.md5(str2hash.encode())
print("The hexadecimal equivalent of MD5 hash is : ", end ="")
print(result.hexdigest())
print ("\r")

result = hashlib.sha256(str2hash.encode())
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())
print ("\r")

result = hashlib.sha384(str2hash.encode())
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())
print ("\r")

result = hashlib.sha224(str2hash.encode())
print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())
print ("\r")

result = hashlib.sha512(str2hash.encode())
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())
print ("\r")

result = hashlib.sha1(str2hash.encode())
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
