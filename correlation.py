import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Confuse import main
from scipy.stats.stats import pearsonr 
import seaborn as sns
import math


def print_heat_map():
	data = pd.read_csv("Data/Original-Data/Original_Combine.csv")
	cm = data.corr()

	sns.heatmap(cm,square=True)
	plt.yticks(rotation=0)
	plt.xticks(rotation=90)
	plt.show()

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def single_correlation():
	A = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['PM 2.5'])
	B = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['T'])
	C = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['TM'])
	D = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['Tm'])
	E = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['SLP'])
	F = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['H'])
	G = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['VV'])
	H = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['VM'])
	I = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['V'])

	# Positive Correlation - PM 2.5 and Atmospheric pressure
	# plt.plot(xrange(0, 1125), A, label='PM 2.5')
	# plt.plot(xrange(0, 1125), E, label='Pressure')
	# plt.xlabel('DAYS')
	# plt.ylabel('Feature')
	# plt.legend(loc='upper right')
	# plt.show()

	# Negative Correlation - PM 2.5 and Minimun Temperature
	# plt.plot(xrange(0, 1125), A, label='PM 2.5')
	# plt.plot(xrange(0, 1125), D, label='Temprature')
	# plt.xlabel('DAYS')
	# plt.ylabel('Feature')
	# plt.legend(loc='upper right')
	# plt.show()

	a = pearsonr(A, B)
	b = pearsonr(A, C)
	c = pearsonr(A, D)
	d = pearsonr(A, E)
	e = pearsonr(A, F)
	f = pearsonr(A, G)
	g = pearsonr(A, H)
	h = pearsonr(A, I)

	coerr = []
	coerr.append(a)
	coerr.append(b)
	coerr.append(c)
	coerr.append(d)
	coerr.append(e)
	coerr.append(f)
	coerr.append(g)
	coerr.append(h)

	myvar = 0
	mydoosravar = 0
	flag1 = -2
	flag2 = 2
	for i in coerr:
	    for j in i:
	        if j > flag1:
	            flag1 = j
	        if j < flag2:
	            flag2 = j

	# print coerr
	print "Max Positive Correlation : ", flag1[0], "\nMax Negative Correlation : ", flag2[0]

def multiple_correlation():
	A = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['PM 2.5'])
	B = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['T'])
	C = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['TM'])
	D = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['Tm'])
	E = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['SLP'])
	F = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['H'])
	G = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['VV'])
	H = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['VM'])
	I = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['V'])

	coerr = []
	coerr.append(B)
	coerr.append(C)
	coerr.append(D)
	coerr.append(E)
	coerr.append(F)
	coerr.append(G)
	coerr.append(H)
	coerr.append(I)
	
	myfinalcorr = []	
	k = 7

	# for i in xrange(len(coerr)):
	# 	mycorr = []
	# 	for j in xrange(1,k+1):
	# 		corr1 = pearsonr(A,coerr[i])
	# 		corr2 = pearsonr(A,coerr[i+j])
	# 		corr3 = pearsonr(coerr[i],coerr[i+j])
	# 		corr = math.sqrt((math.pow(corr1[0],2)+math.pow(corr2[0],2)-(2*corr1[0]*corr2[0]*corr3[0]))/(1-math.pow(corr3[0],2)))
	# 		mycorr.append(corr)
	# 	k = k - 1
	# 	print mycorr
	# 	myfinalcorr.append(mycorr)

	for i in xrange(len(coerr)):
		mycorr = []
		for j in xrange(8):
			corr1 = pearsonr(A,coerr[i])
			corr2 = pearsonr(A,coerr[j])
			corr3 = pearsonr(coerr[i],coerr[j])
			corr = math.sqrt((math.pow(corr1[0],2)+math.pow(corr2[0],2)-(2*corr1[0]*corr2[0]*corr3[0]))/(1-math.pow(corr3[0],2)))
			mycorr.append(corr)
		k = k - 1
		print mycorr
		myfinalcorr.append(mycorr)

	# print max(myfinalcorr)

	a = 0.0
	for i in myfinalcorr:
		for j in i:
			if a < j:
				a = j

	print a,index_2d(myfinalcorr,a)

	tick_marks = np.arange(8)	
	h = sns.heatmap(myfinalcorr,square=True)	
	plt.yticks(tick_marks, ['T', 'TM', 'Tm', 'SLP','H','VV','VM','V'],rotation=45)
	plt.xticks(tick_marks, ['T', 'TM', 'Tm', 'SLP','H','VV','VM','V'],ha='left',rotation=45)
	plt.show()

if __name__ == "__main__":
	# print_heat_map()
	# single_correlation()
	multiple_correlation()
