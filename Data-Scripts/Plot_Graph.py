import pandas as pd
import matplotlib.pyplot as plt


def data_2013():
    i = 0
    main_avg = []
    for a in pd.read_csv('../Data/PM2.5/aqm2013.csv', chunksize=24):
        add = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=a)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for pm in data:
            if type(pm) is long or type(pm) is float or type(pm) is int:
                var = pm
                add = add + var
            elif type(pm) is str:
                if pm != 'NoData' and pm != 'PwrFail':
                    var = float(pm)
                    add = add + var
        avg = add/24
        i += 1
        # if avg == 0.0:
        #   print "No Data", i
        # else:
        #   print round(avg,2),i
        main_avg.append(avg)

    # new1 = pd.DataFrame(main_avg)
    # new1.columns = ['2013']
    return main_avg


def data_2014():
    i = 0
    main_avg = []
    for a in pd.read_csv('../Data/PM2.5/aqm2014.csv', chunksize=24):
        add = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=a)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for pm in data:
            if type(pm) is long or type(pm) is float or type(pm) is int:
                var = pm
                add = add + var
            elif type(pm) is str:
                if pm != 'NoData' and pm != 'PwrFail':
                    var = float(pm)
                    add = add + var
        avg = add/24
        i += 1

        # if avg == 0.0:
        #   print "No Data", i
        # else:
        #   print round(avg,2),i
        main_avg.append(avg)

    # new2 = pd.DataFrame(main_avg)
    # new2.columns = ['2014']
    return main_avg


def data_2015():
    i = 0
    main_avg = []
    for a in pd.read_csv('../Data/PM2.5/aqm2015.csv', chunksize=24):
        add = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=a)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for pm in data:
            if type(pm) is long or type(pm) is float or type(pm) is int:
                var = pm
                add = add + var
            elif type(pm) is str:
                if pm != 'NoData' and pm != '---' and pm != 'InVld' and pm != 'PwrFail':
                    var = float(pm)
                    add = add + var
        avg = add/24
        i += 1

        # if avg == 0.0:
        #   print "No Data", i
        # else:
        #   print round(avg,2),i
        main_avg.append(avg)

    # new3 = pd.DataFrame(main_avg)
    # new3.columns = ['2015']
    return main_avg


def data_2016():
    i = 0
    main_avg = []
    for a in pd.read_csv('../Data/PM2.5/aqm2016.csv', chunksize=24):
        add = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=a)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for pm in data:
            if type(pm) is long or type(pm) is float or type(pm) is int:
                var = pm
                add = add + var
            elif type(pm) is str:
                if pm != 'NoData' and pm != '---' and pm != 'InVld' and pm != 'PwrFail':
                    var = float(pm)
                    add = add + var
        avg = add/24
        i += 1

        # if avg == 0.0:
        #   print "No Data", i
        # else:
        #   print round(avg,2),i
        main_avg.append(avg)

    # new3 = pd.DataFrame(main_avg)
    # new3.columns = ['2015']
    return main_avg

if __name__ == "__main__":
    a = []
    b = []
    a = data_2013()
    b = data_2014()
    c = data_2015()
    d = data_2016()
    plt.plot(xrange(0, 365), a, label='2013')
    plt.plot(xrange(0, 364), b, label='2014')
    plt.plot(xrange(0, 365), c, label='2015')
    plt.plot(xrange(0, 31), d, label='2016')
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()
