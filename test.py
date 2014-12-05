import difflib as db
a = 'heyay'
b = 'heyyy'
s = db.SequenceMatcher(None,a,b)
#c=s.find_longest_match(0,len(a),0,len(b))
c = s.get_matching_blocks()
print c
print c[0].size;

total_match =0
for e in c:
	total_match=total_match+e.size
print "{} {} {}".format(len(a),len(b),total_match)