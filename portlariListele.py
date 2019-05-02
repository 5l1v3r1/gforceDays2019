import subprocess
for i in range(1,65535,1):
	print "Port:",i
	komut="cat portTaramasi1.gnmap |grep '"+str(i)+"/open'|cut -d ' ' -f2"
	cikti=subprocess.check_output(komut,shell=True)
	print cikti
	if len(cikti)>10:
		dosyaIsmi=str(i)+".txt"
		dosya=open(dosyaIsmi,"w")
		dosya.write(cikti)
		dosya.close()
