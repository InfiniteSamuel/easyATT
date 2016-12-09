from subprocess import call
import re
import csv

call(["pdf2txt.py", "-t", "tag", "-o", "output", "att1.pdf"])

raw = open("output").read()

searchObj = re.findall(r'Total for(\d\d\d \d\d\d-\d\d\d\d)(\d*.\d*) ', raw)
total=0


with open('RawData.csv','w') as output:
	writer = csv.writer(output)
	if searchObj:
		# print searchObj.group()
		for item in searchObj:
			phone = item[0][0]+item[0][1]+item[0][2]+item[0][4]+item[0][5]+item[0][6]+item[0][8]+item[0][9]+item[0][10]+item[0][11]			#print phone+": "+item[1]
			writer.writerow((item[0],phone,item[1]))
			total += float(item[1])
	else:
		print "No match!"
	#print "Total: " + str(total)
	writer.writerow(('Total',str(total)))
