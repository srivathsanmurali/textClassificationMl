from numpy import *

Y1_pre = genfromtxt('valid_Y1_predicted_KNN.csv')
Y2_pre = genfromtxt('valid_Y2_predicted_KNN.csv')

f = open('validation_result.csv','w')
for i in range(len(Y1_pre)):
	str1 = str(int(Y1_pre[i])) + "," + str(int(Y2_pre[i])) + "\n"
	f.write(str1)

f.close()
