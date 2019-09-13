#!/san/bin/python3.7
# -*- Coding: utf-8 -*-


## PROGRAM MENGGUNAKAN PYTHON VERSI 3 ##

import os, sys, requests, hashlib
from time import sleep
from getpass import getpass
from multiprocessing.pool import ThreadPool

s = requests.Session()
url = "https://graph.facebook.com/{}"
api="https://api.facebook.com/{}"

target     = []
found      = []
checkpoint = []

W  = "\033[1;97m"
G  = "\033[1;92m"
R  = "\033[1;91m"
P  = "\033[1;95m"
Y  = "\033[1;93m"
C  = "\033[1;96m"
GB = "\033[1;42m"
PM = "\033[3;95m"
CM = "\033[3;96m"
RM = "\033[3;91m"
RE = "\033[0m"


#=================FORM LOGIN

def login():
	print("%s\n\n* login your account facebook first *\n"%(W))
	email = input("%s [📧]  %sUser     : "%(P,W))
	pasw = getpass("%s[🔓]  %sPassword : "%(P,W))
	
	
	
	
	get(email,pasw)	
#=================FORM TOKEN
def     get(email,pasw):
	print("%s[⚙]%s membuat kode masuk ..."%(P,W))
	b = open("cookie/token.log","w")
	try:
		sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+email+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pasw+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
		data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":email,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pasw,"return_ssl_resources":"0","v":"1.0"}
		x = hashlib.new('md5')
		x.update(sig.encode("utf-8"))
		data.update({'sig':x.hexdigest()})
		ok=s.get(api.format("restserver.php"),params=data).json()
		if "access_token" in ok:
			b.write(ok["access_token"])
			b.close()
			print("%s[📤]%s sukses membuat kode masuk..."%(G,W))
			exit("%s[📥]%s kode disimpan di: cookie/token.log"%(G,W))
		elif "www.facebook.com" in ok["error_msg"]:
			os.system("rm -rf cookie")
			print("%s[⚠️]%s failed to generate access token !!"%(R,W))
			exit("%s[❌] %syour account checkpoint !!"%(R,W))
		else:
			os.system("rm -rf cookie")
			print("%s[⚠️]%s failed to generate access token !!"%(R,W))
			exit("%s[✉] %swrong email or password !!"%(R,W))		
	except requests.exceptions.ConnectionError:
		print("%s[⚠️] %sfailed to generate access token"%(R,W))
		exit("%s[📵] %scheck your connection !!"%(R,W))
