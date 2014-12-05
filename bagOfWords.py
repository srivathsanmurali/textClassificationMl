import csvfuncs as cf
import difflib as dl
from numpy import *
import csv

def getWordList(td):
	print "getting word list from list of cities"
	wordList = list()
	i = 0;
	for city in td:
		words = city.split(' ')
		for word in words:
			word = word.upper()
			match = dl.get_close_matches(word,wordList);
			if(match == []): 
				wordList.append(word)
				print "word count :" + str(len(wordList))
			else:
				match_word = match.pop(0)
				diff = len(match_word) - len(word)
				diff = abs(diff)
				if(abs > 1):
					wordList.append(word)
					print "word count :" + str(len(wordList))

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
	bow = zeros((len(td),len(wordList)))	
	i = 0;
	for city in td:
		print "city no {}".format(i)
		words = city.split(' ')
		for word in words:
			word = word.upper()
			word = dl.get_close_matches(word,wordList)
			if(len(word) > 0):
				word = word.pop(0)
				bow[i,wordList.index(word)] = 1;
		i = i+1
	print "Bag of Words Generated"
	return bow;
def getBOWFromFile(filename):
	#BOW from file
	bow = genfromtxt(filename,delimiter=',')
	print "successfully read BOW from " + filename
	return bow;

################################################
#
#
#	for training data
#	td - the city names
#	filename - 'training'
#
#
def getBOWTrain(td,filename):
	# Generating the wordList
	wordList = getWordList(td)
	filen = filename + "_wordList.csv"
	cf.writeWordListToCSV(wordList,filen);

	# reading saved WordList
	#wordList = getWordListFromCSV('training_wordList.csv');

	#Bag Of Words model generation
	bow = generateBagOfWords(td,wordList)
	filen = filename + "_BOW.csv"
	cf.writeListToCSV(bow,filen)
	return bow


################################################
#
#
#	for validation and test data
#	td - the city names
#	trainWordList - 
#		wordlist from training data
#	filename - 'validation'
#
#	
def getBOW(td,trainWordList,filename):
	#Bag Of Words model generation
	bow = generateBagOfWords(td,trainWordList)
	filen = filename + "_BOW.csv"
	cf.writeListToCSV(bow,filen)
	return bow
##################################################

def getCityCodes(td):

	cityCodes = zeros((len(td.cityCodes),1));
	j=0;
	for city in td.cityCodes:
		cityCodes[j] = city.pop(0);
		j=j+1
	return cityCodes;
	
def getCountryCodes(td):
	countryCodes = zeros((len(td.countryCodes),1))
	i=0
	for c in td.countryCodes:
		countryCodes[i] = c;
		i=i+1
	return countryCodes;
