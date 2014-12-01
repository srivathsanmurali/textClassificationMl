import numpy; 
from PyML import *
from PyML.classifiers import multi 
from PyML.classifiers import composite

def getMultiModel(X, Y):
	data = VectorDataSet(X,L=Y)
	#cc = composite.CompositeClassifier(svm.SVM())
	#mc = multi.OneAgainstRest(cc)
	mc = multi.OneAgainstRest (SVM())
	mc.train(data)
	return mc

def getModel(X,Y):
	data = VectorDataSet(X,L=Y)
	s = SVM()
	s.train(data)
	return s

def test(model,X):
	testData = VectorDataSet(X)
	r = model.test(testData);
	return r.getPredictedLabels();
