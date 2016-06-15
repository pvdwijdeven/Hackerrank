f = open("training.json","r")
input = f.readlines()
f.close()

#input_test = sys.stdin.readlines()
f = open("sample-test.in.json","r")
input_test = f.readlines()
f.close()

N = int(input[0])
N_test = int(input_test[0])

import json 

categories = set()
cities = set()
sections = set()

training = []

for i in range(1,N+1):
    e = json.loads(input[i])
    categories.add(e['category'])
    cities.add(e['city'])
    sections.add(e['section'])
    training.append(e)

testing = []

for i in range(1,N_test+1):
    e = json.loads(input_test[i])
    cities.add(e['city'])
    sections.add(e['section'])
    testing.append(e)

categories = list(categories)
cities = list(cities)
sections = list(sections)

vcat = {}
vcity = {}
vsection = {} 
#Get numerical values
for v in range(len(categories)):
    vcat[categories[v]] = v
    
for v in range(len(cities)):
    vcity[cities[v]] = v 

for v in range(len(sections)):
    vsection[sections[v]] = v

X = []
y = []
for e in training:
      X.append([vcity[e['city']],vsection[e['section']]])
      y.append(vcat[e['category']])

X_test = []
y_test = []

for e in testing:
      X_test.append([vcity[e['city']],vsection[e['section']]])

#dummify

def dummify(X):
    dummX = []
    for c in range(len(X)):
        l = []
        for v in vcity.itervalues():
            if X[c][0]==v:
                l.append(1)
            else:
                l.append(0)
        for v in vsection.itervalues():
            if X[c][1]==v:
                l.append(1)
            else:
                l.append(0)
        dummX.append(l)
    return dummX

X = dummify(X)
X_test = dummify(X_test)

import scipy.sparse as spsp

X = spsp.csc_matrix(X)
X_test = spsp.csc_matrix(X_test) 


headings = []

for e in training:
    headings.append(e["heading"])

nb_train = len(headings)

for e in testing:
    headings.append(e["heading"])

from sklearn.feature_extraction.text import CountVectorizer

C = CountVectorizer(max_features = 300000, ngram_range=(1,3))

headings = C.fit_transform(headings)

headings_train = headings.tocsc()[:nb_train]
headings_test = headings.tocsc()[nb_train:]

X = spsp.hstack([X,headings_train])
X_test = spsp.hstack([X_test,headings_test])

#from sklearn.svm import LinearSVC
#clf = LinearSVC(random_state=0)
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state = 0) 

clf.fit(X,y)

pred = clf.predict(X_test)

inv_vcat = dict((vcat[k], k) for k in vcat)


f=open('sample-test.out.json')
Y_test=[]
for i in range(N_test):
    h=f.readline().strip()
    Y_test.append(h)
f.close()
l=[]
total=0
for e in pred:
    l.append(inv_vcat[e])
    print inv_vcat[e]
for i in range(len(l)): 
    if l[i]==Y_test[i]: total=total + 1
    print l[i] + ":" + Y_test[i]
print str(float(total)/len(Y_test) * 100)