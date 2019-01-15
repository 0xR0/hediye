#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, sys, requests
from hashlib import *
from colorama import *
from datetime import *

__program__ = 'hediye'
__version__ = 'v.01'
__author__ = 'CW'
__github__ = 'https://github.com/0xR0/hediye'

def banner():
	os.system("resize -s 34 95")
	os.system("clear")
	color=(Style.BRIGHT+Fore.GREEN+'''
                                         ╦ ╦╔═╗╔╦╗┬╦ ╦╔═╗
                                         ╠═╣║╣  ║║│╚╦╝║╣ 
                                         ╩ ╩╚═╝═╩╝o ╩ ╚═╝

\033[0m''' )
	col=(Fore.RED+ '''            .-.
           [.-''-.,
           |  //`~\)
           (<| 0\0|>_	                    .:: 0xR ::.
           ";\  _"/ \\_ _,.:: Hash Generator & Cracker Online Offline ::.
          __\|'._/_  \ '='-,	     .:: cyber-warrior.org ::.
         /\ \    || )_///_\>>
        (  '._ T |\ | _/),-'
         '.   '._.-' /'/ |
         | '._   _.'`-.._/
         ,\ / '-' |/
         [_/\-----j
    _.--.__[_.--'_\__
   /         `--'    '---._
  /  '---.  -'. .'  _.--   '.
  \_      '--.___ _;.-o     /
    '.__ ___/______.__8----'
	\033[0m''')
	print(color,col)
def genpass():
	key = 0
	start = datetime.now()
	parser = argparse.ArgumentParser(
       formatter_class=argparse.RawTextHelpFormatter,
       epilog='''\
use examples:
  {0} -k Key
  {0} -v HASH -f Wordlist
  {0} -n HASH'''.format(__program__ + '.py'))
	parser.add_argument("--hash","-v",help = "Enter Hash Value")
	parser.add_argument("--file","-f",help = "Enter wordlist")
	parser.add_argument("--key","-k",help = "Enter Key")
	parser.add_argument("--net","-n",help = "Enter Hash Value")
	
	x = parser.parse_args()

	if x.key:
		print(Style.BRIGHT+Fore.RED +'Hash Generated For :\033[0m',Fore.GREEN+x.key,)
		h = md5(x.key.encode()).hexdigest()
		h1 = sha1(x.key.encode()).hexdigest()
		h2 = sha224(x.key.encode()).hexdigest()
		h3 = sha256(x.key.encode()).hexdigest()
		h4 = sha384(x.key.encode()).hexdigest()
		h5 = sha512(x.key.encode()).hexdigest()
		print (Style.BRIGHT+Fore.RED +'\nmd5    : \033[0m',Fore.GREEN+h,
				Style.BRIGHT+Fore.RED +'\nsha1   : \033[0m',Fore.GREEN+h1,
				Style.BRIGHT+Fore.RED +'\nsha224 : \033[0m',Fore.GREEN+h2,
				Style.BRIGHT+Fore.RED +'\nsha256 : \033[0m',Fore.GREEN+h3,
				Style.BRIGHT+Fore.RED +'\nsha384 : \033[0m',Fore.GREEN+h4,
				Style.BRIGHT+Fore.RED +'\nsha512 : \033[0m',Fore.GREEN+h5,'\n')
		return False
	if x.net:
		if len(x.net) == 32:
			on = requests.get('http://www.nitrxgen.net/md5db/' + x.net).text
			if len (on) == 0:
				print(Style.BRIGHT+'Md5 Value Not Found  For -->	: ',Fore.RED,x.net)
			else :
				print(Style.BRIGHT+'MD5 Value Found  For -->  :',Fore.GREEN ,x.net,'\n',Fore.WHITE,'		 Key -->  :',Fore.RED ,on)
		else:
			onn = requests.get('https://lea.kz/api/hash/' + x.net).status_code
			
			if onn == 200:
				onn = requests.get('https://lea.kz/api/hash/' + x.net).text
				print(Style.BRIGHT+'Value Found  For -->  :',Fore.GREEN ,x.net,'\n',Fore.WHITE,'           Key -->  :',Fore.RED,onn)
			else :
				print(Style.BRIGHT+'Value Not Found !!! For -->  :',Fore.RED,x.net)
		return False
	if x.hash:
		if len (x.hash) == 32:
			value = md5
		elif len (x.hash) == 40:
			value = sha1
		elif len (x.hash) == 56:
			value = sha224
		elif len (x.hash) == 64:
			value = sha256
		elif len (x.hash) == 96:
			value = sha384
		elif len (x.hash) == 128:
			value = sha512	
		else:
			print(Style.BRIGHT+'\nCheck The Hash !!! ¯\_(ツ)_/¯\n')
			sys.exit()
		with open(x.file,mode='r',encoding='ISO-8859-1') as data:
			for hash in data:
				hash=hash.strip()
				key +=1
				end = datetime.now()
				if value(hash.encode()).hexdigest()==x.hash:
					print(Style.BRIGHT,'\nValue Found  For -->        :',Fore.GREEN ,x.hash,'\n',Fore.WHITE,'	     Key -->        :',Fore.RED,hash,Fore.WHITE,'\nTested',Fore.RED,key,Fore.WHITE,'word in',Fore.RED,x.file,Fore.WHITE,'elapsed time',Fore.CYAN,end - start,'\n')
					sys.exit()
				else:
					els = x 
		x = print(Style.BRIGHT+'\nValue Not Found  For -->       :',Fore.RED ,x.hash,Fore.WHITE,'\nTested',Fore.RED,key,Fore.WHITE,'word in',Fore.RED,x.file,Fore.WHITE,'elapsed time',Fore.GREEN,end - start,'\n')
		sys.exit()
	
if __name__ == "__main__":
	banner()
	try:
		genpass()	
	except UnicodeDecodeError:
		sys.exit()
	except KeyboardInterrupt:
		os.system("clear")
		sys.exit()
	except requests.exceptions.ConnectionError:
		print('Connection Error !!!')
	except FileNotFoundError:
		print(Style.BRIGHT+'Wordlist Not Found !!! ¯\_(ツ)_/¯ ')
