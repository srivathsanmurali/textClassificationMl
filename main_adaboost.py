import csvfuncs as cf
import bagOfWords as bow
from sklearn.ensemble import AdaBoostClassifier

td = cf.readTrainingData();
#trainXRaw = td.cities;
trainXBow = bow.getBOWFromFile('training_BOW.csv')
trainY1   = td.cityCodes
trainY2   = td.countryCodes
#wordList = bow.getWordListFromCSV('training_wordList.csv')

#validXRaw = cf.readXData('validation.csv')
#validXBow = bow.getBOW(validXRaw,wordList,'validation')
validXBow = bow.getBOWFromFile('validation_BOW.csv')

print "training a AdaBoost classifier with the training data for Y1"
clfY1 = AdaBoostClassifier(n_estimators=100)
clfY1.fit(trainXBow,trainY1)
print "predicting Y1 using the AdaBoost classifier"
Y1_hat = clfY1.predict(validXBow)

print "training a AdaBoost classifier with the training data for Y2"
clfY2 = AdaBoostClassifier(n_estimators=100)
clfY2.fit(trainXBow,trainY2)
print "predicting Y2 using the AdaBoost classifier"
Y2_hat = clfY2.predict(validXBow)

print "prediction complete"

f = open('validation_result_AdaBoost.csv','w')
for i in range(len(Y1_hat)):
	str1 = str(int(Y1_hat[i])) + "," + str(int(Y2_hat[i])) + "\n"
	f.write(str1)

f.close()

