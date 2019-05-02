import requests
dosya=open("crawlListe.txt","r")
icerik=dosya.read()
dosya.close()
for i in icerik.splitlines():
	print i
	url="http://192.168.24.139/"+str(i)
	print url
	sonuc=requests.get(url)
	print sonuc.status_code
	if "200" in str(sonuc.status_code):
		print "[+]Bulunan dizin:",url
	else:
		print "[-]Bulunamayan dizin:",url
