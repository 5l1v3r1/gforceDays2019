import requests
apikey=""
url="http://104.237.140.134/api/top_attackers/?api_key="+str(apikey)+"&hours_ago=4"
sonuc=requests.get(url)
for i in  sonuc.json()['data']:
	print i['source_ip']
	kural="iptables -A INPUT -p tcp --source "+str(i['source_ip']) +" -j DROP\n"
	dosya("iptablesKural.txt","a")
	dosya.write(kural)
	dosya.close()
