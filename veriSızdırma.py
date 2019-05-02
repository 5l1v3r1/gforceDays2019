import requests
dosya=open("kritikVeri.txt","r")
icerik=dosya.read()
dosya.close()
for i in icerik.split(" "):
	print i
	url="http://127.0.0.1/A_"+str(i)
	sonuc=requests.get(url)
	print sonuc
