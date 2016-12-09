from subprocess import call
import re

call(["pdf2txt.py", "-t", "tag", "-o", "output", "att2.pdf"])

raw = open("output").read()

searchObj = re.findall(r'Total for(\d\d\d \d\d\d-\d\d\d\d)(\d*.\d*) ', raw)
total=0

if searchObj:
	# print searchObj.group()
	for item in searchObj:
		print item[0]+": "+item[1]
		total += float(item[1])
else:
	print "No match!"

print "Total: " + str(total)
