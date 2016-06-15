from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.snowball import SnowballStemmer
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
import datetime

#from nltk.corpus import stopwords #stopwords are not supported, requires download
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
local= True
stem=False
algo=2

if local:
    #filename="H:\R\Hackerrank\MachineLearning\Medium\DocumentClassification\trainingdata.txt"
    filename="trainingdata.txt"
    tstart=datetime.datetime.now()
else:
    filename="trainingdata.txt"

def stem(ls):
    stemmer=SnowballStemmer("english")
    newls=[]
    for x in ls:
        newx=""
        for y in x.split():
            newx+= stemmer.stem(y) + " "
        newls.append(newx)
    return newls

vectorizer = CountVectorizer(min_df=1)

f=open(filename) 
n= int(f.readline())
ln=[]
ls=[]
for _ in range(n):  # change this to n in stead of 3
    x=f.readline()
    xs=x[2:]
    xn=x[0]
    ls.append(xs)
    ln.append(xn)
#stem the words
if stem: ls=stem(ls)
bag_of_words=vectorizer.fit(ls)
bag_of_words=vectorizer.transform(ls)

#sw=stopwords.words() #stopwords are not supported, requires download
if algo==1:
    forest = RandomForestClassifier(n_estimators = 1000) 
    forest = forest.fit( bag_of_words, ln)
elif algo==2:
    svm=LinearSVC(C=0.6)
    svm.fit(bag_of_words,ln)
elif algo==3:
    svm=SVC(C=0.5)
    svm.fit(bag_of_words,ln)
elif algo==4:
    GNB=GaussianNB()
    bag_of_words=bag_of_words.toarray()
    GNB.fit(bag_of_words,ln)
elif algo==5:
    clf = tree.DecisionTreeClassifier(min_samples_split=1,random_state=1,)
    clf.fit(bag_of_words,ln)
    

				

#Now get input (test) data
lt=[]

if local:
    filename=open("testdata.txt")
    line = filename.readline()
    ntests=int(line)
    for _ in range(ntests):
        lt.append(filename.readline())
else:
    for _ in range(input()):
        lt.append(raw_input())

#clean data
if stem: lt=stem(lt)
bag_of_test_words=vectorizer.transform(lt)
if algo==1:
    result = forest.predict(bag_of_test_words)
elif algo==2:
    result=svm.predict(bag_of_test_words)
elif algo==3:
    result=svm.predict(bag_of_test_words)
elif algo==4:
    bag_of_test_words=bag_of_test_words.toarray()
    result=GNB.predict(bag_of_test_words)
elif algo==5:
    result=clf.predict(bag_of_test_words)

if local:
    actuals=[]
    filename=open("testresults.txt")
    z=0
    for x in range(len(result)):
        zz = int(filename.readline())
        if zz==int(result[x]):
            z=z+1
    print float(z)/len(result)
    print datetime.datetime.now()-tstart
else:
    for x in result:
        print x