import requests
dosya=open("XSSPayload.txt","r")
icerik=dosya.read()
dosya.close()
url="http://192.168.24.139/xss/example1.php?name=hacker"
indis=url.find("=")
for i in icerik.splitlines():
	print i 
	istek=url[:indis+1]+str(i)
	print istek
	sonuc=requests.get(istek)
	if str(i) in sonuc.content:
		print "Muhtemel XSS:",str(i)
