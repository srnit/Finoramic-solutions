import json
import pip
with open('data.json') as data_file:    
	myObj = json.load(data_file)
	#print myObj['Dependencies']
	#print len(myObj['Dependencies'])
	li=[];
	for i in range(len(myObj['Dependencies'])):
		print myObj['Dependencies'][i]
		failed = pip.main(["install", str(myObj['Dependencies'][i])])
		if failed==1:
			li.append(myObj['Dependencies'][i]);		
	if len(li)==0:
		print ("sucess")
	else:
		for i in range(len(li)):
			print li[i];


