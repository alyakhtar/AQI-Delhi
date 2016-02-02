import csv
import requests
import sys
from bs4 import BeautifulSoup
import os,time


def fetch():
	done = 2.7
	i = 1
	for year in xrange(2013,2016):
		for month in xrange(1,13):
			
			if month <10:
				url = 'http://en.tutiempo.net/climate/0%i-%i/ws-421820.html' %(month,year)
			else:
				url = 'http://en.tutiempo.net/climate/%i-%i/ws-421820.html' %(month,year)

			source_code = requests.get(url)

			plain_text = source_code.text.encode('utf-8')

			if not os.path.exists("%i" %year):
			    os.makedirs("%i" %year)

			with open("%i/%i.html" %(year,month), "w") as output_file:
			    output_file.write(plain_text)

			if i == 35:
				done = 98

			sys.stdout.write("\r[%s%s] %d%% Completed" % ('=' * i, ' ' * (36-i), done))
			done = done + 2.7
			i += 1
	        
	        sys.stdout.flush()


if __name__ == "__main__":
	start = time.time()
	fetch()
	end = time.time()
	print '\nTime Taken : ',end-start, 'seconds'

# with open('test.csv', 'wb') as fp:
#     a = csv.writer(fp, delimiter=',')
#     data = []
#     a.writerows(data)