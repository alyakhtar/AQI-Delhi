import os
import csv
from sklearn.cross_validation import train_test_split
import pandas as pd


def split_combine():
    for a in pd.read_csv('../Data/Normalised-Data/met_normalised_combine.csv', chunksize=1200):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()

    print len(mylist)
    # mylist_a = []
    # mylist_b = []
    # mylist_c = []
    # mylist_d = []
    # mylist_e = []
    # mylist_f = []

    # for i in xrange(len(mylist)):
    #     if mylist[i][9] == 1:
    #         mylist_a.append(mylist[i])
    #     elif mylist[i][9] == 2:
    #         mylist_b.append(mylist[i])
    #     elif mylist[i][9] == 3:
    #         mylist_c.append(mylist[i])
    #     elif mylist[i][9] == 4:
    #         mylist_d.append(mylist[i])
    #     elif mylist[i][9] == 5:
    #         mylist_e.append(mylist[i])
    #     elif mylist[i][9] == 6:
    #         mylist_f.append(mylist[i])

    # print len(mylist_a)
    # print len(mylist_b)
    # print len(mylist_c)
    # print len(mylist_d)
    # print len(mylist_e)
    # print len(mylist_f)

    mylist_train, mylist_test = train_test_split(
        mylist, test_size=0.2)

    # for i in xrange(0,8,2):
    #     mylist_train.append(mylist_a[i])

    # for j in xrange(1,8,2):
    #     mylist_test.append(mylist_a[j])

    if not os.path.exists("../Data/Train"):
        os.makedirs("../Data/Train")
    if not os.path.exists("../Data/Test"):
        os.makedirs("../Data/Test")

    with open('../Data/Train/Train_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(mylist_train)

    with open('../Data/Test/Test_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(mylist_test)


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

    for a in pd.read_csv('../Data/Normalised-Data/met_normalised_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()

    mylist_train, mylist_test = train_test_split(
        mylist, test_size=0.3)

    if not os.path.exists("../Data/Train"):
        os.makedirs("../Data/Train")
    if not os.path.exists("../Data/Test"):
        os.makedirs("../Data/Test")

    with open('../Data/Train/Train_' + str(year) + '.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(mylist_train)

    with open('../Data/Test/Test_' + str(year) + '.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(mylist_test)


def combine_train(year, cs):
    for a in pd.read_csv('Train/Train_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
    mylist = df.values.tolist()
    return mylist


def combine_test(year, cs):
    for a in pd.read_csv('Test/Test_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
    mylist = df.values.tolist()
    return mylist


if __name__ == "__main__":
    # for year in xrange(2013, 2017):
    #     split(year)

    split_combine()

    # a = combine_train(2013,343)
    # b = combine_train(2014,346)
    # c = combine_train(2015,349)
    # d = combine_train(2016,59)

    # final_train = a+b+c+d
    # with open('Train/Train_Combine.csv', 'w') as csvfile:
    #     wr = csv.writer(csvfile, dialect='excel')
    #     wr.writerow(['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
    #     wr.writerows(final_train)

    # a = combine_test(2013,343)
    # b = combine_test(2014,346)
    # c = combine_test(2015,349)
    # d = combine_test(2016,59)

    # final_test = a+b+c+d
    # with open('Test/Test_Combine.csv', 'w') as csvfile:
    #     wr = csv.writer(csvfile, dialect='excel')
    #     wr.writerow(['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
    #     wr.writerows(final_test)
