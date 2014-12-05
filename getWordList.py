import csvfuncs as cf

def getRawList(cityList):
	print "getting Raw WordList"
	rawWordList = list()
	i = 0;
	for city in cityList:
		words = city.split(' ')
		for word in words:
			word = word.lower()
			if (word not in rawWordList):
				zeroList = list()
				oneList = list()
				for wd in rawWordList:
					score=getCharMatchCount(word,wd)
					if(score==0):
						zeroList.append()
				rawWordList.append(word)
		print "row {0:6d} done".format(i);
		i = i+1;

	print "Word List is complete"
	print "number of words: ",format(len(rawWordList))
	return rawWordList;

def getCharMatchCount(a,b):
	ab = abs(len(a)-len(b))
	if(ab>1):
		return -1
	l = min(len(a),len(b))
	res=ab
	for i in range(0,l):
		if(a[i] != b[i]):
			res = res+1
	return res


def test():
	td = cf.readTrainingData()
	rwl=getRawList(td.cities)
