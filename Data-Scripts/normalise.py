import pandas as pd
import csv


def maximum(list):
    maxi = 0.0
    for a in list:
        if a is not '-':
            if type(a) is str:
                print a
                abc = float(a)
            else:
                abc = a

            if abc > maxi:
                maxi = a
    return maxi


def minimum(list):
    mini = max(list)
    for a in list:
        if a is not '-':
            if type(a) is str:
                abc = float(a)
            else:
                abc = a

            if abc < mini:
                mini = a
    return mini


def normalize_input(maxi, mini, list):
    mylist = []
    for a in list:
        if a is '-':
            y = '-'
        else:
            y = (((a - mini) / (maxi - mini)) * 2) - 1
        mylist.append(y)
    return mylist


def normalize_output(PM):
    mylist = []
    for poll in PM:
        if type(poll) is str:
            NewPoll = float(poll)
        else:
            NewPoll = poll

        if NewPoll > 0 and NewPoll <= 30:
            y = 1
        elif NewPoll > 30 and NewPoll <= 60:
            y = 2
        elif NewPoll > 60 and NewPoll <= 90:
            y = 3
        elif NewPoll > 90 and NewPoll <= 120:
            y = 4
        elif NewPoll > 120 and NewPoll <= 250:
            y = 5
        else:
            y = 6
        mylist.append(y)
    return mylist

def normalize_output_binary(PM):
    mylist = []
    for poll in PM:
        if type(poll) is str:
            NewPoll = float(poll)
        else:
            NewPoll = poll

        if NewPoll <= 90:
            y = 0
        else:
            y = 1
        mylist.append(y)
    return mylist


def normalization(year):
    with open('../Data/Normalised-Data/met_normalised_'+str(year)+'.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
    final = []
    Temp = []
    T = []
    MaxTemp = []
    TM = []
    MinTemp = []
    Tm = []
    SLP = []
    Pr = []
    Humidity = []
    H = []
    Visibility = []
    VV = []
    Wind = []
    V = []
    MaxWind = []
    VM = []
    PM = []
    PM2 = []

    for a in pd.read_csv('../Data/Original-Data/met_'+str(year)+'.csv', chunksize=1):
        df = pd.DataFrame(data=a)
        for index, row in df.iterrows():
            PM.append(row['PM 2.5'])
            Temp.append(row['T'])
            MaxTemp.append(row['TM'])
            MinTemp.append(row['Tm'])
            SLP.append(row['SLP'])
            Humidity.append(row['H'])
            Wind.append(row['V'])
            Visibility.append(row['VV'])
            MaxWind.append(row['VM'])

    T = normalize_input(maximum(Temp), minimum(Temp), Temp)
    TM = normalize_input(maximum(MaxTemp), minimum(MaxTemp), MaxTemp)
    Tm = normalize_input(maximum(MinTemp), minimum(MinTemp), MinTemp)
    Pr = normalize_input(maximum(SLP), minimum(SLP), SLP)
    H = normalize_input(maximum(Humidity), minimum(Humidity), Humidity)
    V = normalize_input(maximum(Wind), minimum(Wind), Wind)
    VV = normalize_input(maximum(Visibility), minimum(Visibility), Visibility)
    VM = normalize_input(maximum(MaxWind), minimum(MaxWind), MaxWind)
    PM2 = normalize_input(maximum(PM),minimum(PM),PM)

    TwoD = []
    for a in xrange(len(T)):
        oneD = []
        oneD.append(a+1)
        oneD.append(T[a])
        oneD.append(TM[a])
        oneD.append(Tm[a])
        oneD.append(Pr[a])
        oneD.append(H[a])
        oneD.append(VV[a])
        oneD.append(V[a])
        oneD.append(VM[a])
        oneD.append(PM2[a])
        TwoD.append(oneD)

    with open('../Data/Normalised-Data/met_normalised_'+str(year)+'.csv', 'a') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerows(TwoD)

    # print tabulate(TwoD,headers=['S
    # No','T','TM','Tm','SLP','H','V','VV','VM','PM
    # 2.5'],tablefmt='fancy_grid')

def normalization_combine():
    with open('../Data/Normalised-Data/met_normalised_combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['SNO', 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
    final = []
    Temp = []
    T = []
    MaxTemp = []
    TM = []
    MinTemp = []
    Tm = []
    SLP = []
    Pr = []
    Humidity = []
    H = []
    Visibility = []
    VV = []
    Wind = []
    V = []
    MaxWind = []
    VM = []
    PM = []
    PM2 = []

    for a in pd.read_csv('../Data/Original-Data/Original_Combine.csv', chunksize=1):
        df = pd.DataFrame(data=a)
        for index, row in df.iterrows():
            PM.append(row['PM 2.5'])
            Temp.append(row['T'])
            MaxTemp.append(row['TM'])
            MinTemp.append(row['Tm'])
            SLP.append(row['SLP'])
            Humidity.append(row['H'])
            Wind.append(row['V'])
            Visibility.append(row['VV'])
            MaxWind.append(row['VM'])

    T = normalize_input(maximum(Temp), minimum(Temp), Temp)
    TM = normalize_input(maximum(MaxTemp), minimum(MaxTemp), MaxTemp)
    Tm = normalize_input(maximum(MinTemp), minimum(MinTemp), MinTemp)
    Pr = normalize_input(maximum(SLP), minimum(SLP), SLP)
    H = normalize_input(maximum(Humidity), minimum(Humidity), Humidity)
    V = normalize_input(maximum(Wind), minimum(Wind), Wind)
    VV = normalize_input(maximum(Visibility), minimum(Visibility), Visibility)
    VM = normalize_input(maximum(MaxWind), minimum(MaxWind), MaxWind)
    # PM2 = normalize_input(maximum(PM),minimum(PM),PM)
    PM2 = normalize_output_binary(PM)

    TwoD = []
    for a in xrange(len(T)):
        oneD = []
        oneD.append(a+1)
        oneD.append(T[a])
        oneD.append(TM[a])
        oneD.append(Tm[a])
        oneD.append(Pr[a])
        oneD.append(H[a])
        oneD.append(VV[a])
        oneD.append(V[a])
        oneD.append(VM[a])
        oneD.append(PM2[a])
        TwoD.append(oneD)

    with open('../Data/Normalised-Data/met_normalised_combine.csv', 'a') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerows(TwoD)



if __name__ == "__main__":
    for year in xrange(2013, 2017):
        normalization(year)
    normalization_combine()
