import hashlib
mystring = input('Enter string: ')
hash_obj = hashlib.md5(mystring.encode())
print('This is your md5:')
print(hash_obj.hexdigest())