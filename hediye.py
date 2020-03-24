#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, sys, requests
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from colorama import *
from datetime import *

__appname__	= 'hediye'
__version__	= 'v.02'
__author__	= 'CW'
__github__	= 'https://github.com/0xR0/hediye'
__yes__		= Fore.GREEN
__kir__ 	= Fore.RED
__res__ 	= Style.RESET_ALL
__size__ 	= Style.BRIGHT

class Hediye:
	

	def __init__(self, key='', net='', dict='', hash=''): # :)


		self.key = x.key
		self.net = x.net
		self.dict = x.dict
		self.hash=x.hash
	
	def keys (self):
		print(Style.BRIGHT+Fore.RED +'Hash Generated For :\033[0m',Fore.GREEN,self.key,)
		h = md5(self.key.encode()).hexdigest()
		h1 = sha1(self.key.encode()).hexdigest()
		h2 = sha224(self.key.encode()).hexdigest()
		h3 = sha256(self.key.encode()).hexdigest()
		h4 = sha384(self.key.encode()).hexdigest()
		h5 = sha512(self.key.encode()).hexdigest()
		print (Style.BRIGHT+Fore.RED +'\nmd5    : \033[0m',Fore.GREEN+h,
				Style.BRIGHT+Fore.RED +'\nsha1   : \033[0m',Fore.GREEN+h1,
				Style.BRIGHT+Fore.RED +'\nsha224 : \033[0m',Fore.GREEN+h2,
				Style.BRIGHT+Fore.RED +'\nsha256 : \033[0m',Fore.GREEN+h3,
				Style.BRIGHT+Fore.RED +'\nsha384 : \033[0m',Fore.GREEN+h4,
				Style.BRIGHT+Fore.RED +'\nsha512 : \033[0m',Fore.GREEN+h5,'\n')

	def nitrxgen(self):
		on = requests.get('http://www.nitrxgen.net/md5db/' + self.net).text
		if len (on) != 0:
			print(Style.BRIGHT+'   Value Found  For -->  :',Fore.GREEN ,self.net,Fore.WHITE,':',Fore.RED ,on,Style.RESET_ALL)
		else:
			self.hashtoolkit()
		
	def hashtoolkit(self):
		words = set()
		on = requests.get('https://hashtoolkit.com/decrypt-md5-hash/' + self.net, headers  = { 'User-agent' : 'Mozilla/11.0' }).text
		if 'Access denied' in on :
			self.search()
		else:
			with open('blabla.txt',mode='w+') as data:
				data.write(on)
			with open('blabla.txt',mode='r') as data:
				for line in data:
					for word in line.replace('.', ' ').replace(
				':', ' ').replace('?', '').replace('('', ' ').replace(''', ' ').split(' '):
						if word not in words:
	
							words.add(word)
							if md5(word.encode()).hexdigest()==self.net:
								print(Style.RESET_ALL,Style.BRIGHT+'   Value Found  For -->  :',Fore.GREEN ,self.net,Fore.WHITE,':',Fore.RED ,word,Style.RESET_ALL)
							else:
								self.search()
							
	def search(self):
		words = set()

		if len (self.net) == 32:
			self.value = md5
		elif len (self.net) == 40:
			self.value = sha1
		elif len (self.net) == 56:
			self.value = sha224
		elif len (self.net) == 64:
			self.value = sha256
		elif len (self.net) == 96:
			self.value = sha384
		elif len (self.net) == 128:
			self.value = sha512	
		else:
			#pass
			print(Style.BRIGHT+'\ncheck this input ',self.net, ' ¯\_(ツ)_/¯','\n')
			sys.exit()
		
		on   = requests.get('https://www1.search-results.com/web?q=' + self.net).text
		goo  = requests.get('https://www.google.com/search?q=' + self.net).text
		ya	 = requests.get('https://search.yahoo.com/search?p=' + self.net).text
		bing = requests.get('https://www.bing.com/search?q=' + self.net).text
		ask  = requests.get('https://de.ask.com/web?q=' + self.net).text
		
		with open('blabla.txt',mode='w+') as data:
			data.write(on+goo+ya+bing+ask)
		with open('blabla.txt',mode='r') as data:
			for line in data:
				for word in line.replace('.', ' ').replace(
			':', ' ').replace('?', '').replace('('', ' ').replace(''', ' ').split(' '):
					if word not in words:

						words.add(word)
						if self.value(word.encode()).hexdigest()==self.net:
							print(Style.RESET_ALL,Style.BRIGHT+'  Value Found  For -->  :',Fore.GREEN ,self.net,Fore.WHITE,':',Fore.RED ,word,Style.RESET_ALL)

	def nets(self):

		try:
			with open(self.net, mode='r') as inn:
				with open('hashfile.txt', mode='w+') as out:
					for line in inn:
						if len (line.strip('\n')) == 32 or len (line.strip('\n')) == 40 or len (line.strip('\n')) == 56 or len (line.strip('\n')) == 64 or len (line.strip('\n')) == 96 or len (line.strip('\n')) == 128 :
							out.write(line)
			lines = sum(1 for line in open('hashfile.txt'))
			print(Style.BRIGHT,Fore.GREEN,'loaded', lines,'hash in',Fore.RED , self.net,'\n',Style.RESET_ALL)
			with open('hashfile.txt',mode='r') as data:
				for self.net in data:
					self.net=self.net.strip()

					if len(self.net) == 32:
						self.nitrxgen()

					else:
						self.search()
										
		except FileNotFoundError:
			

			if len(self.net) == 32:
				self.nitrxgen()

			else:
				self.search()

	
	def words(self):
		keys = 0
		start = datetime.now()

		if len (self.hash) == 32:
			self.value = md5
		elif len (self.hash) == 40:
			self.value = sha1
		elif len (self.hash) == 56:
			self.value = sha224
		elif len (self.hash) == 64:
			self.value = sha256
		elif len (self.hash) == 96:
			self.value = sha384
		elif len (self.hash) == 128:
			self.value = sha512	
		else:
			print(Style.BRIGHT+'\ncheck this input this input The Hash !!! ¯\_(ツ)_/¯\n','\n',self.hash)
			sys.exit()
		with open(self.dict,mode='r',encoding='ISO-8859-1') as data:
			for dic in data:
				dic=dic.strip()
				end = datetime.now()
				keys +=1			
				if self.value(dic.encode()).hexdigest()==self.hash:

					print(Style.RESET_ALL,Style.BRIGHT,'\nValue Found  For -->        :',Fore.GREEN ,self.hash,'\n',Fore.WHITE,'	     Key -->        :',Fore.RED,dic,Fore.WHITE,'\nTested',Fore.RED,keys,Fore.WHITE,'word in',Fore.RED,self.dict,Fore.WHITE,'elapsed time',Fore.CYAN,end - start,'\n',Style.RESET_ALL)
					sys.exit()
					
				else:
					pass
			print(Style.RESET_ALL,Style.BRIGHT+'\nValue Not Found  For -->       :',Fore.RED ,self.hash,Fore.WHITE,'\nTested',Fore.RED,keys,Fore.WHITE,'word in',Fore.RED,self.dict,Fore.WHITE,'elapsed time',Fore.GREEN,end - start,'\n',Style.RESET_ALL)
	def banner(self):
		os.system('resize -s 30 109')
		os.system('clear')
		print('''{3}{0}
                                         ╦ ╦╔═╗╔╦╗┬╦ ╦╔═╗
                                         ╠═╣║╣  ║║│╚╦╝║╣ 
                                         ╩ ╩╚═╝═╩╝o ╩ ╚═╝


	{1}{2}    .-.
           [.-''-.,
           |  //`~\)
           (<| 0\0|>_	                   {0} .:: 0xR ::.{2}
           ';\  _'/ \\_ _,         .:: Hash Generator & Cracker  ::.
          __\|'._/_  \ '='-,	    {0} .:: cyber-warrior.org ::.{2}
         /\ \    || )_///_\>>
        (  '._ T |\ | _/),-'           .:: Supported HASH ::.
         '.   '._.-' /'/ |     {0}md5, sha1, sha224, sha256, sha384, sha512{2}
         | '._   _.'`-.._/
         ,\ / '-' |/
         [_/\-----j
    _.--.__[_.--'_\__
   /         `--'    '---._
  /  '---.  -'. .'  _.--   '.
  \_      '--.___ _;.-o     /
    '.__ ___/______.__8----'
'''.format(__yes__, __res__,  __kir__,__size__))

if __name__ == '__main__':


	parser = argparse.ArgumentParser(
	formatter_class=argparse.RawTextHelpFormatter,add_help=False,
	epilog='''{4}{1}
                                         ╦ ╦╔═╗╔╦╗┬╦ ╦╔═╗
                                         ╠═╣║╣  ║║│╚╦╝║╣ 
                                         ╩ ╩╚═╝═╩╝o ╩ ╚═╝


	{03}{2}    .-.
           [.-''-.,
           |  //`~\)
           (<| 0\0|>_	                   {1} .:: 0xR ::.{2}
           ';\  _'/ \\_ _,         .:: Hash Generator & Cracker  ::.
          __\|'._/_  \ '='-,	    {1} .:: cyber-warrior.org ::.{2}
         /\ \    || )_///_\>>
        (  '._ T |\ | _/),-'           .:: Supported HASH ::.
         '.   '._.-' /'/ |     {1}md5, sha1, sha224, sha256, sha384, sha512{2}
         | '._   _.'`-.._/
         ,\ / '-' |/
         [_/\-----j
    _.--.__[_.--'_\__
   /         `--'    '---._
  /  '---.  -'. .'  _.--   '.
  \_      '--.___ _;.-o     /
    '.__ ___/______.__8----'
	
use examples:
{03}{0} -k {1}Key / For --> Generate Hash {2}(md5, sha1, sha224, sha256, sha384, sha512){3}
{03}{0} -v{1} HASH -d Wordlist / For --> Brute Force Attack
{03}{0} -n {1}HASH or HASHS FILES / For --> Search Engine {2}(Nitrxgen, Hashtoolkit, Google, Yahoo, Bing, Ask ..)
{03}{0} -u{1} Check For update '''.format(__appname__ + '.py' ,__yes__, __kir__, __res__,__size__)) 

	parser.add_argument('--hash','-v')
	parser.add_argument('--key','-k')
	parser.add_argument('--net','-n')
	parser.add_argument('--dict','-d')
	parser.add_argument('--update','-u',action='store_true')
	parser.add_argument('--help','-h',action='store_true')
	x = parser.parse_args()
	cw = Hediye()
	
	if x.key:
		
		cw.keys()
		
	if x.dict:
		
		cw.banner()
		cw.words()
	if x.net:
		
		cw.banner()
		cw.nets()
	if x.update:
		cw.banner()
		on = requests.get('https://raw.githubusercontent.com/0xR0/hediye/master/hediye.py').text
		if 'v.02' in on :
			print(Style.BRIGHT,Fore.GREEN,'You are using latest version !!')
			
		else:
			#os.system('cd .. && rm -r hediye && git clone https://github.com/0xR0/hediye.git' )
			with open('hediye.py',mode='w+') as data:
				data.write(on)			
				print(Style.BRIGHT,Fore.GREEN,'Update completed !! Run again.. ')

		
		
		
		
	if os.path.exists('hashfile.txt'):
		os.remove('hashfile.txt')
	if os.path.exists('blabla.txt'):
		os.remove('blabla.txt')
	if not x.key and not x.dict and not x.net and not x.update :
		print(parser.epilog)
