from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
import numpy as np

def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(4)
    plt.xticks(tick_marks, ['0', '1', '2', '3'])
    plt.yticks(tick_marks, ['0', '1', '2', '3'])
    plt.tight_layout()
    plt.ylabel('Expected ')
    plt.xlabel('Observed')
    plt.show()


def confuse(Expected, Observed):
    A_O = []
    A_E = []

    if len(Observed[0]) == 2:
        for i in Observed:
            if i[0] > i[1]:
                A_O.append(0)
            else:
                A_O.append(1)
    else:
        for i in Observed:
            if i >= 0.5 and i < 1:
                A_O.append(1)
            else:
                A_O.append(0)
    

    print "Precision : ", precision_score(Expected,A_O, average=None)
    print "Recall : ", recall_score(Expected,A_O, average=None)

    return confusion_matrix(Expected, A_O)


def main(true, pred):
    sum = 0.0
    a = confuse(true, pred)
    print a
    # plot_confusion_matrix(a)
    for i in xrange(len(a)):
        for j in xrange(len(a)):
            if i == j:
                sum += a[i][j]

    print "Accuracy : ", (sum / len(true)) * 100