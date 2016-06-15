# -*- coding: utf-8 -*-
import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

#import data
X_traintest=[]
Y_train=[]


f=open('training.json')
ntrain= int(f.readline())
for i in range(ntrain):
    h=json.loads(f.readline())
    x=" ".join(h['heading'].split(','))
    x=" ".join(re.compile('[A-Za-z]+').findall(x))
    X_traintest.append(h['city']+" " + h['section']+" " +x)
    Y_train.append(h['category'])
f.close()

f=open('sample-test.in.json')
ntest= int(f.readline())
for i in range(ntest):
    h=json.loads(f.readline())
    x=" ".join(h['heading'].split(','))
    x=" ".join(re.compile('[A-Za-z]+').findall(x))
    X_traintest.append(h['city']+" " + h['section']+" " +x)
f.close()

f=open('sample-test.out.json')
Y_test=[]
for i in range(ntest):
    h=f.readline().strip()
    Y_test.append(h)
f.close()


transformer=TfidfVectorizer(sublinear_tf=True, max_df = 0.1, ngram_range=(1,2),stop_words='english')
X_traintest = transformer.fit_transform(X_traintest)
#X_traintest = np.append(X_train_section,X_traintest,axis=1)


#split test/train
X_train=X_traintest[0:ntrain]
X_test=X_traintest[ntrain:ntrain+ntest]
clf=SGDClassifier(alpha=0.00003)
clf.fit(X_train,Y_train)
    
Y_pred=clf.predict(X_test)
total=0
for i in range(len(Y_test)): 
    if Y_pred[i]==Y_test[i]: total=total + 1
print float(total)/len(Y_test) * 100