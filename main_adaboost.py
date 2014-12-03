import csvfuncs as cf
import bagOfWords as bow
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

td = cf.readTrainingData();

### if getting the bow for the first time
#trainXRaw = td.cities;
#trainXBow = bow.getBOWTrain(trainXRaw,'training')

### reading the bow saved in a file, its slow to generate
trainXBow = bow.getBOWFromFile('training_BOW.csv')
trainY1   = td.cityCodes
trainY2   = td.countryCodes

### reading the trainind data word list, used to create
### the validation, test data bow
#wordList = bow.getWordListFromCSV('training_wordList.csv')

### if getting the bow for the validation for the first time
#validXRaw = cf.readXData('validation.csv')
#validXBow = bow.getBOW(validXRaw,wordList,'validation')

### reading the validation bow saved in a file
validXBow = bow.getBOWFromFile('validation_BOW.csv')


### training the AdaBoostClassifier to 
### predict the city codes
print "training a AdaBoostClassifier with the training data for Y1"
clfY1 = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2), n_estimators=600, learning_rate=1)
clfY1.fit(trainXBow,trainY1)
print "predicting Y1 using the AdaBoostClassifier"
Y1_hat = clfY1.predict(validXBow)

### training the AdaBoostClassifier to 
### predict the country codes
print "training a AdaBoostClassifier with the training data for Y2"
clfY2 = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2), n_estimators=600, learning_rate=1)
clfY2.fit(trainXBow,trainY2)
print "predicting Y2 using the AdaBoostClassifier"
Y2_hat = clfY2.predict(validXBow)

print "prediction complete"

### saving the validation result to a file in the required format
f = open('validation_result_AdaBoost.csv','w')
for i in range(len(Y1_hat)):
	str1 = str(int(Y1_hat[i])) + "," + str(int(Y2_hat[i])) + "\n"
	f.write(str1)

f.close()


### The End
