###Create Dictionary, plot graph and email - created by Daniel## 

#!/usr/bin/env python
import requests
import json

import matplotlib

import subprocess
import os, sys 
import time
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib


#No idea why this works but it does
#Importing a module by itself breaks.
#https://github.com/matplotlib/matplotlib/issues/9954/

matplotlib.use("Agg")
import matplotlib.pyplot as plt


import numpy as np

hostName = os.uname()[1].upper()
todaysDate = datetime.date.today() 
allUniqueUsers = set()
#print(r.status_code)
#print(r.text)
#for x in userList:

address = 'http://<RM Server>:8088/ws/v1/cluster/apps'
headers = {'X-Requested-By': 'ambari'}
r = requests.get(address,headers=headers,verify=False)
JSONResponse = r.json()  #json.loads(r.text)

#print JSONResponse
#Check the return Code
#print("Response: " + str(r))
	
#print(json.dumps(JSONResponse, indent=4, sort_keys=True))

#Get all the unique users.
for x in JSONResponse['apps']['app']:
	allUniqueUsers.add(x['user'])

print(allUniqueUsers)
	
def getUserTotalUsage(userID):
	totalvcoreSeconds = 0
	totalmemorySeconds = 0

	address = 'http://<RM Server>:8088/ws/v1/cluster/apps?user={0}'.format(userID)
	headers = {'X-Requested-By': 'ambari'}
	r = requests.get(address,headers=headers,verify=False)
	JSONResponse = r.json()  #json.loads(r.text)
	for x in JSONResponse['apps']['app']:
		totalvcoreSeconds += x['vcoreSeconds']
		totalmemorySeconds += x['memorySeconds']
	
	#print "For User: " + userID
	#print "total VCore Seconds " + str(totalvcoreSeconds)
	#print "total Mem Seconds: " + str(totalmemorySeconds)
	return totalvcoreSeconds, totalmemorySeconds

userList = {}

for x in allUniqueUsers:
	#Skip this user cause way too much usageMemory
	if x == "<sys account with too much data>":
		continue
	uservcore, usermem = getUserTotalUsage(x)
	userList[x] = [uservcore,usermem]


	
	
users = [] 
usageVCORE = []
usageMemory = []

for x in userList: 
	users.append(x)
	usageVCORE.append(userList[x][0])
	usageMemory.append(userList[x][1])

def createBarChart(x,y,xlabel,ylabel,title,fileName):
	fig, ax = plt.subplots()
	ax.patch.set_facecolor('#001942')
	fig.patch.set_facecolor('#001942')    
	width = 0.75 # the width of the bars
	ind = np.arange(len(y))  # the x locations for the groups	
	ax.barh(ind, y, width, color="#13bb58")
	ax.set_yticks(ind+width/2)
	ax.set_yticklabels(x, minor=False)

	#Adds text to the bars
	for i, v in enumerate(y):
		ax.text(v/y[i]+100, i + .25, str(v), color='white')

	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel) 
	plt.tight_layout()
	plt.savefig('/home/<user account>/{0}.png'.format(fileName))

createBarChart(users,usageVCORE,"VCore Seconds","Users","VCore Seconds Per User","VCoreSeconds")

createBarChart(users,usageMemory,"Memory Seconds","Users","Memory Seconds","MemorySeconds")








myHTMLOutput = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Data Platform Admin - SystemCheck</title>
<style type="text/css">
body {
	color: #2C2A29;
	font: 85% Arial,Helvetica,sans-serif;
	background-color: rgb(240,248,255)
}
h2
{ 
		color: #24596E;
		font-size: 2em;
		line-height: 1.2em;
		font: 2em Georgia,"Times New Roman",Times,serif;
}
hr
{
		background-color: #CCC;
		border: medium none;
		color: #CCC;
		height: 1px;
} 
div.headerTitle
{
		/*background-color: #EEE;*/
		margin-bottom: 5px;
		font: 1.5em Georgia,"Times New Roman",Times,serif;
		text-align: center;
} 


#successTable tr:nth-child(even){background-color: rgb(198, 239, 206);}

#successTable th {
	padding-top: 12px;
	padding-bottom: 12px;
	text-align: center;
	background-color: rgb(0, 133, 164);
	color: white;
}
</style>
</head>

<body>
<div class="headerTitle">
<div><img src="cid:image1" alt="Department logo" id="logo"></img></div>
<img src="cid:image2" id="vcoreseconds"></img>
<img src="cid:image3" id="memseconds"></img>
"""



def sendEmail(sendTo, sendSubject, sendHTML):
	
	smtp_host = "linuxsmtp.gateway.local"
	
	me = os.uname()[1]+ '@gateway.local'
	
	msg = MIMEMultipart('related')
	msg['From'] = me
	msg['To'] = sendTo
	msg['Subject'] = sendSubject  
 
	part2 = MIMEText(sendHTML, 'html') 
	msg.attach(part2)
	
	#Attach the image assuming its in the same directory
	fp = open('/<location to image>/logo.png','rb')
	msgImage = MIMEImage(fp.read())
	fp.close()
	
	msgImage.add_header('Content-ID','<image1>')
	msg.attach(msgImage)
	
	fp = open('/home/<user account>/VCoreSeconds.png','rb')
	msgImage = MIMEImage(fp.read())
	fp.close()
	
	msgImage.add_header('Content-ID','<image2>')
	msg.attach(msgImage)
	
	fp = open('/home/<user account>/MemorySeconds.png','rb')
	msgImage = MIMEImage(fp.read())
	fp.close()
	
	msgImage.add_header('Content-ID','<image3>')
	msg.attach(msgImage)

	s = smtplib.SMTP(smtp_host)
	s.sendmail(me, sendTo, msg.as_string())
	s.quit()




myHTMLOutput += """</body></html>"""
	
sendEmail(sendTo="<Email ID>",sendSubject=(todaysDate.strftime('%d/%m/%y') + "- Resource Usage"),sendHTML=myHTMLOutput)

