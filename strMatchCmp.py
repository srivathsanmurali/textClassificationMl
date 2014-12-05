def strMatchCmp(a,b):
# compares word a to word b
# results gives the number of chars, the words are diff in
	res = abs(len(a) - len(b))
	for i in range(0,len(a)):
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

a = 'hey'
b = ['heyyy','hey','heb','hye']
print a
print b
print strMatchCmpList(a,b)

