import requests
import sys
# Access https://www.eventbrite.com/login/
################################################################################
URL = 'https://www.eventbrite.com/login/'
payload = {
    "email": "hieuttse03538@fpt.edu.vn", 
    "password": "myangel0105!@#", 
    "csrfmiddlewaretoken": ""
}
f = open('source.txt','w',encoding = 'utf-8')
# Access the check-in page with link = https://www.eventbrite.com/checkin?eid=20785127877
with requests.Session() as c:
	payload['csrfmiddlewaretoken'] = c.get(URL).cookies['csrftoken']
	c.post(URL,data = payload)
	r = c.get('https://www.eventbrite.com/checkin?eid=20785127877')
	f.write ((r.content).decode('utf-8'))
f.close()
################################################################################
# Processing with the source code to extract data we need 
def ConvertEmail(line):
	line = line.replace('email: "',"")
	line = line.replace('",',"")
	line = line.replace(" ","")
	return line
def getline(thefilepath, desired_line_number):
    if desired_line_number < 1: return ''
    current_line_number = 0
    for line in open(thefilepath,encoding = 'utf-8'):
        current_line_number += 1
        if current_line_number == desired_line_number: return line
    return ''
sourcecode = open('source.txt','r',encoding = 'utf-8')
finalmail = open('finalmail.txt','w+',encoding = 'utf-8')
i=0
for line in sourcecode:
	if 'email: "' in line and 'checked_in: 1,' in getline('source.txt',i+4) :
		finalmail.write(ConvertEmail(line))
	i+=1

sourcecode.close()
finalmail.close()