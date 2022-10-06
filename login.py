
from asyncio import sleep
from cmath import isnan
from curses.ascii import isupper
import random
import string

def menu():
 chs = int(input(''' [0] Gerador de Senhas
 [1] Analisar senha
 (?)>>> '''))

 if chs == 0:
    gerador()
    
 elif chs == 1:
    
  analise()

letras_mais = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
especiais = 'çÇ^~`´;:.,></*-+\|!@#$%¢£³²¬¨&()§'
letras_menos = 'abcdefghijklmnopqrstuvwxyz'
numeros = '1234567890'  

def gerador():
 pre = ''
 for i in range(2):
  l = random.choice(letras_mais)
  ln =random.choice(letras_menos)
  esp = random.choice(especiais)
  num = random.choice(numeros)
 
  pre += l + ln + esp + num
 
 print(pre)
 gr = input('''Quer gerar outra senha? Y/N
 (?)>>> ''')
 if gr == 'Y':
     gerador()
 else:
  ans = input('''Quer analisar uma senha? Y/N
  (?)>>> ''')
  if ans == 'Y':
    analise()
    
 
 
 

def analise():
 password = input('''Digite sua senha:
 (...)>>> ''')
 
 p = 0
 carac = list(password)
 leng = len(carac)
 numeros = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'  
 i = 0
 for i in range(leng):
  if  password[i] not in numeros:
      print(f'Requisito {i + 1}: Analisando')
      
  else:
      print(f'Requisito {i + 1}: OK'); p = p + 1
      break
      

 if not leng >= 6:
  print(f'Requisito {i + 2}: Analisando')
    
 else:
    print(f'Requisito {i+2}: OK'); p = p + 1
 for i in range(leng):
   if password[i] not in list(especiais):
      if i == leng: 
       print(f'Requisito {i+3}: Analisando')
       
   else:
    print(f'Requisito {i+2}: OK'); p = p + 1
    break
       
 for i in range(leng):
    if not password[i].isupper():
        
       
 if p == 4:
     print('Senha Forte')
     menu()
 elif p == 3:
     print('Senha Fraca')
     gr = input('''Quer uma senha forte? Y/N
 (?)>>> ''')
     if gr == 'Y':
         gr = gr.upper
         gerador()
         exit()
     else:
         ans = input('''Quer analisar outra senha? Y/N
 (?)>>> ''')
    
         if ans == 'Y':
             analise()
             
             
         else:
             exit()
 elif p == 2:
     print('Senha Muito Fraca')
     gr = input('''Quer uma senha forte? Y/N
 (?)>>> ''')
     if gr == 'Y':
         gr = gr.upper
         gerador()
     else:
         ans = input('''Quer analisar outra senha? Y/N
 (?)>>> ''')
    
         if ans == 'Y':
             analise()
             
         else:
             exit()
 elif p <= 1:
     print('Senha Extremamente Fraca')
     gr = input('''Quer uma senha forte? Y/N
 (?)>>> ''')
     if gr == 'Y':
         gr = gr.upper
         gerador()
     else:
         ans = input('''Quer analisar outra senha? Y/N
 (?)>>> ''')
    
         if ans == 'Y':
             analise()
             
         else:
             exit()
             

             

     
    
 





menu()



