import os
import csv
from sklearn.cross_validation import train_test_split
import pandas as pd


def split(year):
    mylist = []
    if year == 2013:
        cs = 343
    elif year == 2014:
        cs = 346
    elif year == 2015:
        cs = 349
    else:
        cs = 59

    for a in pd.read_csv('Normalised-Data/met_normalised_'+str(year)+'.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()

    mylist_train, mylist_test = train_test_split(
        mylist, test_size=0.4)

    if not os.path.exists("Train"):
        os.makedirs("Train")
    if not os.path.exists("Test"):
        os.makedirs("Test")

    with open('Train/Train_'+str(year)+'.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(mylist_train)

    with open('Test/Test_'+str(year)+'.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(mylist_test)


if __name__ == "__main__":
    for year in xrange(2013, 2017):
        split(year)
