import matplotlib.pyplot as plt

mylist = []
myloss = []
with open('mlp_categorical.txt') as f:
    content = f.readlines()

count = 0
for i in xrange(1,len(content)-6,2):
    loss = []
    # print len(content[i])
    for j in xrange(142970,len(content[i])):
        loss.append(content[i][j])
    mylist.append(loss)

for i in xrange(len(mylist)) :
    mystr = ''
    for j in xrange(len(mylist[i])) : 
        if mylist[i][j] == 'l':
            # print mylist[i][j+6:j+12]
            mystr = mystr + mylist[i][j+6]+mylist[i][j+7]+mylist[i][j+8]+mylist[i][j+9]+mylist[i][j+10]+mylist[i][j+11]
    myloss.append(float(mystr))


plt.plot(xrange(0, 80), myloss, label='LOSS')
plt.xlabel('EPOCHS')
plt.ylabel('LOSS')
plt.legend(loc='upper right')
plt.show()

