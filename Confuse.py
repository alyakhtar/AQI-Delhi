from sklearn.metrics import confusion_matrix,accuracy_score
import matplotlib.pyplot as plt
import numpy as np


def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(4)
    plt.xticks(tick_marks, ['0', '1', '2' , '3'])
    plt.yticks(tick_marks, ['0', '1', '2' , '3'])
    plt.tight_layout()
    plt.ylabel('Expected ')
    plt.xlabel('Observed')
    plt.show()


def confuse(Expected,Observed):
	A_O = []
	A_E = []


	for i in Observed:
		if i >= -1.0 and i < -0.5:
			A_O.append(0)
		elif i >= -0.5 and i < 0:
			A_O.append(1)
		elif i >= 0 and i < 0.5:
			A_O.append(2)
		else:
			A_O.append(3)

	for i in Expected:
		if i >= -1.0 and i < -0.5:
			A_E.append(0)
		elif i >= -0.5 and i < 0:
			A_E.append(1)
		elif i >= 0 and i < 0.5:
			A_E.append(2)
		else:
			A_E.append(3)
	return confusion_matrix(A_E,A_O)

def main(true,pred):
	sum = 0.0
	a = confuse(true,pred)
	# plot_confusion_matrix(a)
	for i in xrange(4):
		for j in xrange(4): 
			if i == j:
				sum += a[i][j]

	print "Accuracy : ",(sum/len(true))*100

