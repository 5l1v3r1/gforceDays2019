dosya1=open("canlilar1.txt","r")
dosya1Icerik=dosya1.read()
dosya1.close()
canlilar=[]
for i in dosya1Icerik.splitlines():
	print i
	canlilar.append(i)
dosya2=open("canlilar2.txt","r")
dosya2Icerik=dosya2.read()
dosya2.close()
for i in dosya2Icerik.splitlines():
	if not i in canlilar:
		print "Yeni Bulunan IP:",str(i)
