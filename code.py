import requests
import json
import base64
import pandas as pd
import time

df = pd.read_excel('notfoundurls.xlsx')
notfoundurls = df['NOTFOUNDURLS'].tolist()
df = pd.read_excel('posturls.xlsx')
posturls = df['POSTURLS'].tolist()
df = pd.read_excel('stopwords.xlsx')
stopwords = df['STOPWORDS'].tolist()

# print(notfoundurls)
# print(posturls)
# print(stopwords)



def checkifstopword(word,stopwords):
	
	for sw in stopwords:
		if sw==word:
			return 1
		else:
			return 0


npu=""
totalword=0
for nfu in notfoundurls:
	
	allwords=nfu.split("-")

	for word in allwords:
		checkword=checkifstopword(word,stopwords)
		
		if(checkword==1):
			continue
			#print("stop word.............................")
		else:
			# print("not stop word")
			for pu in posturls:
				allwords2=pu.split("-")
				wordmatchcount=0
				for word2 in allwords2:
					checkword2=checkifstopword(word2,stopwords)
					if(checkword2==1):
						continue
						# print("stop word.............................")
					else:
						# print("not a stop word")
						if(word==word2):
							wordmatchcount=wordmatchcount+1
							totalword=wordmatchcount
							if(totalword > wordmatchcount or totalword == wordmatchcount):
								npu=pu
								
						else:
							continue
				
				#print(nfu)
				print(npu)
				print("/n")

