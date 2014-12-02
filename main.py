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
Y1_hat = clfY1.predict(validXBow)

