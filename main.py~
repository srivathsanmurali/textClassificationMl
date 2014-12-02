import csvfuncs as cf
import bagOfWords as bow
from sklearn.neighbors import KNeighborsClassifier

td = cf.readTrainingData();
#trainXRaw = td.cities;
trainXBow = bow.getBOWFromFile('training_BOW.csv')
trainY1   = td.cityCodes
trainY2   = td.countryCodes
#wordList = bow.getWordListFromCSV('training_wordList.csv')

#validXRaw = cf.readXData('validation.csv')
#validXBow = bow.getBOW(validXRaw,wordList,'validation')
validXBow = bow.getBOWFromFile('validation_BOW.csv')

print "training a KNN classifier with the training data for Y1"
clfY1 = KNeighborsClassifier(n_neighbors =3)
clfY1.fit(trainXBow,Y1)
print "predicting Y1 using the KNN classifier"
Y1_hat = clfY1.predict(validXBow)

print "training a KNN classifier with the training data for Y2"
clfY2 = KNeighborsClassifier(n_neighbors =3)
clfY2.fit(trainXBow,Y2)
print "predicting Y2 using the KNN classifier"
Y2_hat = clfY2.predict(validXBow)

print "prediction complete"

f = open('validation_result_KNN.csv','w')
for i in range(len(Y1_pre)):
	str1 = str(int(Y1_hat[i])) + "," + str(int(Y2_hat[i])) + "\n"
	f.write(str1)

f.close()

