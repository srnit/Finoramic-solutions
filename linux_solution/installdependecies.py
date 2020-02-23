import json
import pip
if int(pip.__version__.split('.')[0])>9:
	from pip._internal import main
else:
	from pip import main

with open('data.json') as data_file:    
	dependenciesObj = json.load(data_file)
	#print myObj['Dependencies']
	#print len(myObj['Dependencies'])
	failedpackagelist=[];
	for i in range(len(dependenciesObj['Dependencies'])):
		print dependenciesObj['Dependencies'][i]
		failed_status =main(["install", str(dependenciesObj['Dependencies'][i])])
		if failed_status==1:
			failedpackagelist.append(dependenciesObj['Dependencies'][i]);		
	if len(failedpackagelist)==0:
		print ("success")
	else:
		print("list of failed package")
		for i in range(len(failedpackagelist)):
			print failedpackagelist[i];


