import requests
import sys
import os
import time


def fetch():
    done = 2.63
    i = 1
    for year in xrange(2013, 2017):
        for month in xrange(1, 13):

            if year == 2016:
                if month < 4:
                    url = 'http://en.tutiempo.net/climate/0%i-%i/ws-421820.html' % (
                        month, year)
                else:
                    break
            else:
                if month < 10:
                    url = 'http://en.tutiempo.net/climate/0%i-%i/ws-421820.html' % (
                        month, year)
                else:
                    url = 'http://en.tutiempo.net/climate/%i-%i/ws-421820.html' % (
                        month, year)

            source_code = requests.get(url)

            plain_text = source_code.text.encode('utf-8')

            if not os.path.exists("%i" % year):
                os.makedirs("%i" % year)

            with open("%i/%i.html" % (year, month), "w") as output_file:
                output_file.write(plain_text)

            if i == 37:
                done = 98

            sys.stdout.write("\r[%s%s] %d%% Completed" %
                             ('=' * i, ' ' * (38 - i), done))
            done = done + 2.63
            i += 1

            sys.stdout.flush()


if __name__ == "__main__":
    start = time.time()
    fetch()
    end = time.time()
    print '\nTime Taken : ', end - start, 'seconds'

# with open('test.csv', 'wb') as fp:
#     a = csv.writer(fp, delimiter=',')
#     data = []
#     a.writerows(data)
