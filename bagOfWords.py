import csvfuncs as cf
import difflib as dl
from numpy import *

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

def getBagOfWords(td,wordList):
	print "generating Bag of Words"
	bow = zeros((len(td.cities),len(wordList)))	
	i = 0;
	for city in td.city:
		print "city no {}".format(i)
		words = city.split(' ')
		for word in words:
			word = word.upper()
			word = dl.get_close_matches(word,wordList).pop(0)
			bow[i,wordList.index(word)] = 1;
		i = i+1
	print "Bag of Words Generated"
	return bow;

td = cf.readTrainingData()
wordList = getWordList(td)
bow = getBagOfWords(td,wordList)
