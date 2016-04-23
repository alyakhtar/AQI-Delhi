from keras.models import Sequential, Graph
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import pandas as pd
import time
import numpy as np
import math
import matplotlib.pyplot as plt
from Confuse import main
from sklearn.metrics import mean_absolute_error
from scipy.stats import chisquare
import scipy
from scipy.stats.stats import pearsonr

X = pd.read_csv('Data/Train/Train_Combine.csv', usecols=[
                'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
Y = pd.read_csv('Data/Train/Train_Combine.csv', usecols=['PM 2.5'])

X = X.values
Y = Y.values

X2 = pd.read_csv('Data/Test/Test_Combine.csv', usecols=[
                 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
Y2 = pd.read_csv('Data/Test/Test_Combine.csv', usecols=['PM 2.5'])

X2 = X2.values
Y2 = Y2.values

model = Sequential()

model.add(Dense(10, input_dim=8, init='uniform'))
model.add(Activation('tanh'))
model.add(Dense(10, input_dim=10, init='uniform'))
model.add(Activation('tanh'))
model.add(Dense(1, input_dim=10, init='uniform'))
model.add(Activation('tanh'))

sgd = SGD(lr=0.1, decay=1e-3, momentum=0.5, nesterov=True)
model.compile(loss='mse', optimizer=sgd)

model.fit(X, Y, nb_epoch=100, batch_size=1, show_accuracy=False)
score = model.evaluate(X2, Y2, batch_size=1)
preds = model.predict(X2, batch_size=1, verbose=0)


main(Y2, preds)

# plt.plot(xrange(0, 441), preds, label='Observed')
# plt.plot(xrange(0, 441), Y2, label='Expected')
# plt.xlabel('Data Points')
# plt.ylabel('PM 2.5')
# plt.legend(loc='upper right')
# plt.show()
A = pd.read_csv('Data/Train/Train_Combine.csv', usecols=['PM 2.5'])
B = pd.read_csv('Data/Train/Train_Combine.csv', usecols=['T'])
C = pd.read_csv('Data/Train/Train_Combine.csv', usecols=['TM'])
D = pd.read_csv('Data/Train/Train_Combine.csv', usecols=['Tm'])
E = pd.read_csv('Data/Train/Train_Combine.csv', usecols=['SLP'])
F = pd.read_csv('Data/Train/Train_Combine.csv', usecols=['H'])
G = pd.read_csv('Data/Train/Train_Combine.csv', usecols=['VV'])
H = pd.read_csv('Data/Train/Train_Combine.csv', usecols=['VM'])
I = pd.read_csv('Data/Train/Train_Combine.csv', usecols=['V'])


print "Error : ", score
# print B
# print chisquare(A, f_exp=B)	
a = pearsonr(A,B)
b = pearsonr(A,C)
c = pearsonr(A,D)
d = pearsonr(A,E)
e = pearsonr(A,F)
f = pearsonr(A,G)
g = pearsonr(A,H)
h = pearsonr(A,I)

print a,b,c,d,e,f,g,h
