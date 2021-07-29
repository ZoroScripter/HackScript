import os 
import sys
import time

os.system('clear')
print('=====================')
print('INSTALANDO RECURSOS=')
print('=====================')
os.system('pkg install figlet')
os.system('clear')
os.system('setterm -foreground red -background black -store')
os.system('clear')
os.system('figlet HackScript V2')
os.system('setterm -foreground green -background black -store')
print("""
卍__________________卍
<1> instalar o nmap 
<2> install git
<3> install nano 
<4> install python3
<5> install python2 
<6> install python 
<7> install figlet
<8> install curl
<9> install update
<10> install upgrade
==============================
Especiais!=
=========
<11> parceiro Narutin das edit
<12> meu canal tmj passa
==============================
<13> Black-Hydra
<14> SocialSploit
<15> Tbomb
<99> apoio
<00> Sair
[i] Digite o numero da opção!
卍__________________卍
""")
op = int(input('Digite uma das Opções: '))

if op == 1:
	os.system('clear')
	os.system('pkg install nmap')
	os.system('python3 HackScript.py')
if op == 2:
	os.system('clear')
	os.system('pkg install git')
	os.system('python3 HackScript.py')
if op == 3:
	os.system('clear')
	os.system('pkg install nano')
	os.system('python3 HackScript.py')
if op == 4:
	os.system('clear')
	os.system('pkg install python3')
	os.system('python3 HackScript.py')
if op == 5:
	os.system('clear')
	os.system('pkg install python2')
	os.system('python3 HackScript.py')
if op == 6:
	os.system('clear')
	os.system('pkg install python')
	os.system('python3 HackScript.py')
if op == 7:
	os.system('clear')
	os.system('pkg install figlet')
	os.system('python3 HackScript.py')
if op == 8:
	os.system('clear')
	os.system('pkg install curl')
	os.system('python3 HackScript.py')
if op == 9:
	os.system('clear')
	os.system('pkg update')
	os.system('python3 HackScript.py')
if op == 10:
	os.system('clear')
	os.system('pkg upgrade -y')
	os.system('python3 HackScript.py')
if op == 11:
	os.system('xdg-open https://youtube.com/channel/UCsrhJTlW7agHd6pR1w0Or6A')
if op == 12:
	os.system('xdg-open https://youtube.com/channel/UCfswyN1ty2no6qZw4WvWSlw')
	os.system('python3 HackScript.py')
if op == 13:
	os.system('git clone https://github.com/Gameye98/Black-Hydra')
	os.system('clear')
	os.system('python3 HackScript.py')
if op == 14:
	os.system("""
	pkg install -y git
	git clone https://github.com/Cesar-Hack-Gray/SocialSploit
	python3 HackScript.py
	""")
if op == 15:
	os.system('git clone https://github.com/TheSpeedX/TBomb.git')
	os.system('python3 HackScript.py')
if op == 99:
	print('===')
	time.sleep(1)
	print('Narutin Das Editx')
	time.sleep(1)
	print('===')
	time.sleep(1)
	print('Grupos hackers:')
	time.sleep(1)
	print('===')
	time.sleep(1)
	print('✔︎✞︎700 𝐵𝑌𝑇𝐸𝑆✞︎✔︎')
	time.sleep(1)
	print('===')
	time.sleep(1)
	os.system('python3 HackScript.py')
if op == 00:
	os.system('clear')
	print('Author    :h4ck3r 777') 
	print('Apoio      :Ninguém!')
	print('H4ck3r 777 se dispede de vc fique com deu tmj')
exit()
print('')