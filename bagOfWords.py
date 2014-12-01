import csvfuncs as cf
import difflib as dl
from numpy import *
import csv

def getWordList(td):
	print "getting word list from list of cities"
	wordList = list()
	i = 0;
	for city in td.cities:
		words = city.split(' ')
		for word in words:
			word = word.upper()
			if(dl.get_close_matches(word,wordList) == []):
				wordList.append(word)
		print "row {0:6d} done".format(i);
		i = i+1;
	print "Word List is complete"
	print "number of words: ",format(len(wordList))
	return wordList;
def getWordListFromCSV(filename):
	with open(filename,'rb') as cf:
		wordList = list();
		wlr = csv.reader(cf)
		for row in wlr:
			wordList.append(row.pop(0))
	print "wordList read from  {}".format(filename)
	print "number of words is {}".format(len(wordList))
	return wordList;	

def generateBagOfWords(td,wordList):
	print "generating Bag of Words"
	bow = zeros((len(td.cities),len(wordList)))	
	i = 0;
	for city in td.cities:
		print "city no {}".format(i)
		words = city.split(' ')
		for word in words:
			word = word.upper()
			word = dl.get_close_matches(word,wordList).pop(0)
			bow[i,wordList.index(word)] = 1;
		i = i+1
	print "Bag of Words Generated"
	return bow;


def getBOW():
	td = cf.readTrainingData()

	# Generating the wordList
	#wordList = getWordList(td)
	#cf.writeWordListToCSV(wordList,'training_wordList.csv');

	# reading saved WordList
	#wordList = getWordListFromCSV('training_wordList.csv');

	#Bag Of Words model generation
	#bow = getBagOfWords(td,wordList)
	#cf.writeListToCSV(bow,'training_bow.csv')

	#BOW from file
	bow = genfromtxt('training_bow.csv',delimiter=',')
	return bow;

def getCityCodes():
	td = cf.readTrainingData();

	cityCodes = zeros((len(td.cityCodes),1));
	j=0;
	for city in td.cityCodes:
		cityCodes[j] = city;
		j=j+1
	return cityCodes;
	
def getCountryCodes():
	td = cf.readTrainingData()	
	countryCodes = zeros((len(td.countryCodes),1))
	i=0
	for c in td.countryCodes:
		countryCodes[i] = c;
		i=i+1
	return countryCodes;
