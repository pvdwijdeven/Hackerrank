# Enter your code here. Read input from STDIN. Print output to STDOUT

import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from sklearn.svm import LinearSVC
import numpy as np

def buildFeatureVectorFromMap(thisMap):
	return thisMap['city'] + ' ' + thisMap['section'] + ' ' + thisMap['heading']

data = []
with open('training.json') as f:
    next(f) #ignore number of problems, just read file to end
    for line in f:
        data.append(json.loads(line))

N = len(data)
X = ['']*N
y = np.ndarray(shape=(N,),dtype='int')

le = preprocessing.LabelEncoder()

categories = ['activities','appliances','artists','automotive','cell-phones','childcare','general',
	'household-services','housing','photography','real-estate','shared','temporary','therapeutic',
	'video-games','wanted-housing']

le.fit(categories)

for r in xrange(0,N):
	thisMap = data[r]
	X[r] = buildFeatureVectorFromMap(data[r])
	thisCategory = thisMap['category']
	y[r] = le.transform([thisCategory])
print X[0]
classifier = LinearSVC()
textClassifier = Pipeline([('tfidf', TfidfVectorizer(ngram_range=(1,2))),('clf', classifier)])
textClassifier.fit(X,y)

f=open('sample-test.in.json')
Ntest = int(f.readline())
Xtest = ['']*Ntest
for r in xrange(0,Ntest):
	jsonDict = json.loads(f.readline())
	Xtest[r] = buildFeatureVectorFromMap(jsonDict)
f.close()

f=open('sample-test.out.json')
Y_test=[]
for i in range(Ntest):
    h=f.readline().strip()
    Y_test.append(h)
f.close()



outputClasses = le.inverse_transform(textClassifier.predict(Xtest))
#for c in outputClasses: print(c)
total=0
for i in range(len(outputClasses)): 
    if outputClasses[i]==Y_test[i]: total=total + 1
print str(float(total)/len(Y_test) * 100)