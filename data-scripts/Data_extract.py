import csv
import requests
import sys
from bs4 import BeautifulSoup
from tabulate import tabulate
from Plot_Graph import data_2013, data_2014, data_2015, data_2016


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

    rows = len(oneD) / 15

    for times in xrange(rows):
        newoneD = []
        for i in xrange(15):
            newoneD.append(oneD[0])
            oneD.pop(0)
        twoD.append(newoneD)

    length = len(twoD)

    twoD.pop(length - 1)
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


def data_combine(year, cs):
    for a in pd.read_csv('Original-Data/met_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


if __name__ == "__main__":

    for year in xrange(2013, 2017):
        final = []
        with open('met_' + str(year) + '.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(
                ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        for month in xrange(1, 13):
            if year == 2016:
                if month < 3:
                    a = met_data(month, year)
                    final = final + a
                else:
                    break
            else:
                a = met_data(month, year)
                final = final + a

        pm = getattr(sys.modules[__name__], 'data_%s' % year)()

        if len(pm) == 364:
            pm.insert(364, '-')

        for i in xrange(len(final)):
            final[i].insert(0, i + 1)
            final[i].insert(9, pm[i])

        with open('met_' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final:
                flag = 0
                for elem in row:
                    if elem == 0 or elem == "-":
                        flag = 1
                        # print "Error", elem, row
                if flag != 1:
                    wr.writerow(row)

    a = data_combine(2013, 600)
    b = data_combine(2014, 600)
    c = data_combine(2015, 600)
    d = data_combine(2016, 600)

    total = a + b + c + d

    with open('Original-Data/Original_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
