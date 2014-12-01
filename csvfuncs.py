import csv
import collections


def readTrainingData():
	trainingData = collections.namedtuple('trainingData',['cities','cityCodes','countryCodes']);
	with open('training.csv','rb') as csvfile:
		trainingreader = csv.reader(csvfile,delimiter=',');
		trainingData.cities = list();
		trainingData.cityCodes = list();
		trainingData.countryCodes = list();
		for row in trainingreader:
			trainingData.cities.append(row.pop(0))
			trainingData.cityCodes.append(row.pop(0))
			trainingData.countryCodes.append(row.pop(0))
		
	return trainingData;

def writeListToCSV(li,filename):
	with open(filename,'wb') as csvfile:
		liWriter = csv.writer(csvfile,delimiter=',')
		for row in li:
			liWriter.writerow(row)
		print "list written to {}".format(filename)

def testRead():
	td = readTrainingData();
	print len(td.cities)
	print td.cities[0]
	print td.cityCodes[0]
	print td.countryCodes[0]
