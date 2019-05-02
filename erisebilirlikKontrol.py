# -*- coding: utf-8 -*-
import requests
import datetime
dosya=open("alanAdlari.txt","r")
icerik=dosya.read()
dosya.close()
for i in icerik.splitlines():
	sonuc=requests.get(i)
	if "200" in str(sonuc.status_code):
		print "Erişim olan:",str(i)
		log="Erişim olan:"+str(i)+"|"+str(datetime.datetime.now())+"\n"
		dosya=open("logErisim.txt","a")
		dosya.write(log)
		dosya.close()
	else:
		print "Erişm yok:",str(i)
                log="Erişim olmayan:"+str(i)+"|"+str(datetime.datetime.now())+"\n"
                dosya=open("logErisim.txt","a")
                dosya.write(log)
                dosya.close() 
		requests.post('https://textbelt.com/text', {
  'phone': '',
  'message': log,
  'key': '',
})
