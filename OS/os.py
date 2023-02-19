import os
from datetime import datetime


x = os.listdir('C:/Users/gabri/OneDrive/Imagens') # exibi os arquivos dentro da pasta
print(f'a pasta exibida: {x}\n')


'''
o metodo stat retorna os seguintes atributos: st_mode, st_ino, st_dev, st_nlink, st_uid, st_gid, st_size, 
st_atime, st_mtime, st_ctime
'''
atr = os.stat('C:/Users/gabri/OneDrive/Imagens/Saved Pictures')
print(f'propriedades do arquivo: {atr}\n')

'''
usa a propriedade st_mtime para verificar a ultima alteração do arquivo#
e transforma o valor apresentado em um tipo data
'''
timestamp = datetime.fromtimestamp(atr.st_mtime)


print(f'ultima atualizacao: {timestamp}\n')


#for i in x:
    
    #print(f'a pasta exibida: {i}\n')
