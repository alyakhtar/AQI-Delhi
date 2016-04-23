from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score,f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
import pandas as pd
import csv
from Confuse import main

sum = 0.0
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

c = []
for a in Y:
	for b in a:
		c.append(b)

clf = svm.SVC()
clf.fit(X, c)  
preds = clf.predict(X2)

print "*********SVM***************"
print "Precision : ", precision_score(Y2,preds, average='binary')
print "Recall : ", recall_score(Y2,preds, average='binary')
print "F-Measure : ", f1_score(Y2,preds,average='binary')
a = confusion_matrix(Y2, preds)
for i in xrange(len(a)):
        for j in xrange(len(a)):
            if i == j:
                sum += a[i][j]

print "Accuracy : ", (sum / len(Y2)) * 100

sum = 0.0
# **********************************************************************

abc = LogisticRegression()
abc.fit(X, c)
pred = abc.predict(X2)

print "*********Logistic Regression***************"
print "Precision : ", precision_score(Y2,pred, average='binary')
print "Recall : ", recall_score(Y2,pred, average='binary')
print "F-Measure : ", f1_score(Y2,pred,average='binary')
b = confusion_matrix(Y2, pred)
for i in xrange(len(b)):
        for j in xrange(len(b)):
            if i == j:
                sum += b[i][j]

print "Accuracy : ", (sum / len(Y2)) * 100

sum = 0.0
# **********************************************************************

gnb = GaussianNB()
gnb.fit(X, c)
pred = gnb.predict(X2)

print "*********Naive Bayes***************"
print "Precision : ", precision_score(Y2,pred, average='binary')
print "Recall : ", recall_score(Y2,pred, average='binary')
print "F-Measure : ", f1_score(Y2,pred,average='binary')
c = confusion_matrix(Y2, pred)
for i in xrange(len(c)):
        for j in xrange(len(c)):
            if i == j:
                sum += c[i][j]

print "Accuracy : ", (sum / len(Y2)) * 100