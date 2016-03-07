import csv
import requests
import sys
from bs4 import BeautifulSoup
from tabulate import tabulate
from Plot_Graph import data_2013, data_2014, data_2015


def met_data(month, year):

    file = open('%i/%i.html' % (year, month), 'rb')
    plain_text = file.read()

    oneD = []
    twoD = []

    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.findAll('table', {'class': 'medias mensuales'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                oneD.append(a)

    rows = len(oneD)/15

    for times in xrange(rows):
        newoneD = []
        for i in xrange(15):
            newoneD.append(oneD[0])
            oneD.pop(0)
        twoD.append(newoneD)

    length = len(twoD)

    twoD.pop(length-1)
    twoD.pop(0)

    for a in xrange(len(twoD)):
        twoD[a].pop(6)
        twoD[a].pop(13)
        twoD[a].pop(12)
        twoD[a].pop(11)
        twoD[a].pop(10)
        twoD[a].pop(9)
        twoD[a].pop(0)

    return twoD


if __name__ == "__main__":

    for year in xrange(2013, 2016):
        final = []
        with open('met_'+str(year)+'.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        for month in xrange(1, 13):

            a = met_data(month, year)

            final = final + a

        pm = getattr(sys.modules[__name__], 'data_%s' % year)()

        if len(pm) == 364:
            pm.insert(364, '-')

        for i in xrange(len(final)):
            final[i].insert(0, i+1)
            final[i].insert(9, pm[i])


        # print year

        # print tabulate(final, headers=['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'], tablefmt='fancy_grid')
        # break

        with open('met_'+str(year)+'.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerows(final)

