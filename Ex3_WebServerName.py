import requests	
import urllib.request
url = 'tinhte.vn'
#url = str(input('Enter URL: '))
if 'http' not in url:
	url = 'http://' + url
	try:
		r = urllib.request.urlopen(url)
		if r.getcode() == 200:
			respone = requests.get(url)
			print (respone.headers['Server'])
	except urllib.error.HTTPError as e:
		print ('An error occurred : ' + str(e))
else:
	respone = requests.get(url)
	print (respone.headers['Server'])
