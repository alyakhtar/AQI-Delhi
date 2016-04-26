from keras.models import Sequential, Graph
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import pandas as pd
import time
import math
import matplotlib.pyplot as plt
import numpy
from Confuse import main
from sklearn.metrics import mean_absolute_error
from keras.utils import np_utils
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

Y = np_utils.to_categorical(Y)
Y3 = np_utils.to_categorical(Y2)


model = Sequential()

model.add(Dense(10, input_dim=8, init='uniform'))
model.add(Activation('tanh'))
model.add(Dense(10, input_dim=10, init='uniform'))
model.add(Activation('tanh'))
model.add(Dense(2, input_dim=10, init='uniform'))
model.add(Activation('softmax'))

sgd = SGD(lr=0.1, decay=1e-3, momentum=0.5, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)

model.fit(X, Y, nb_epoch=20, batch_size=1, show_accuracy=True)
score = model.evaluate(X2, Y3, batch_size=1)
preds = model.predict(X2, batch_size=1, verbose=0)
# print preds
main(Y2, preds)

# plt.plot(xrange(0, 441), preds, label='Observed')
# plt.plot(xrange(0, 441), Y2, label='Expected')
# plt.xlabel('Data Points')
# plt.ylabel('PM 2.5')
# plt.legend(loc='upper right')
# plt.show()

print "Error : ", score

A = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['PM 2.5'])
B = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['T'])
C = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['TM'])
D = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['Tm'])
E = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['SLP'])
F = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['H'])
G = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['VV'])
H = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['VM'])
I = pd.read_csv('Data/Original-Data/Original_Combine.csv', usecols=['V'])

# a = pearsonr(A,B)
# b = pearsonr(A,C)
# c = pearsonr(A,D)
# d = pearsonr(A,E)
# e = pearsonr(A,F)
# f = pearsonr(A,G)
# g = pearsonr(A,H)
# h = pearsonr(A,I)

plt.plot(xrange(0, 1125), A, label='PM 2.5')
plt.plot(xrange(0, 1125), E, label='SLP')
plt.xlabel('DAYS')
plt.ylabel('Feature')
plt.legend(loc='upper right')
plt.show()

# coerr = []
# coerr.append(a)
# coerr.append(b)
# coerr.append(c)
# coerr.append(d)
# coerr.append(e)
# coerr.append(f)
# coerr.append(g)
# coerr.append(h)
# myvar = 0
# mydoosravar = 0
# flag1 = -2
# flag2 = 2
# for i in coerr:
#     for j in i:
#         if j > flag1:
#             flag1 = j
#         if j < flag2:
#             flag2 = j

# print coerr

# print "Max Poistive Correlation : ",flag1,"Max Negative Correlation : ",flag2