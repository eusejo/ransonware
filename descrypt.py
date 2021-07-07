import os
import pyaes

# open file
file_name = 'é_noix.jpeg.unv'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# remove file_name
os.remove(file_name)

# descrypt
key = b'0123456789abcdef'
aes = pyaes.AESModeOfOperationCTR(key)
descrypt_data = aes.decrypt(file_data)

# save file
new_file_name = 'descriptografado.jpeg'
new_file = open(new_file_name, 'wb')
new_file.write(descrypt_data)
new_file.close()