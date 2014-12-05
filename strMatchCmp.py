def strMatchCmp(a,b):
# compares word a to word b
# results gives the number of chars, the words are diff in
	res = abs(len(a) - len(b))
	l = min(len(a),len(b))
	for i in range(0,l):
		if (a[i] != b[i]):
			res = res + 1
	return res

def strMatchCmpList(a,bList):
# compares word a to wordList b
# results gives list of compare resutls
	res = list()
	for j in range(0,len(b)):
		res.append(strMatchCmp(a,b[j]))
	return res

def findBestMatch(a,bList):
# compares word a to wordList b
# results gives list of compare resutls
	res_0 = list();
	res_1 = list();
	for j in range(0,len(b)):
		mr =strMatchCmp(a,b[j]) 
		if(mr==0):
			res_0.append(b[j]);
		if(mr==1):
			res_1.append(b[j]);
	res = res_0 + res_1
	return res

a = 'hey'
b = ['heyyy','hey','heb','he','heyy','hye']
print a
print b
print strMatchCmpList(a,b)
print findBestMatch(a,b)

