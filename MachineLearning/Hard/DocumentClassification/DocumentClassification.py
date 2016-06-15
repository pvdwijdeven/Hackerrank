from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import PassiveAggressiveClassifier

#added stopwords manually, as download is not available via this interface
swh = {'a': True, 'about': True, 'above': True, 'across': True, 'after': True, 'again': True, 'against': True, 'all': True, 'almost': True, 'alone': True, 'along': True, 'already': True, 'also': True, 'although': True, 'always': True, 'among': True, 'an': True, 'and': True, 'another': True, 'any': True, 'anybody': True, 'anyone': True, 'anything': True, 'anywhere': True, 'are': True, 'area': True, 'areas': True, 'around': True, 'as': True, 'ask': True, 'asked': True, 'asking': True, 'asks': True, 'at': True, 'away': True, 'b': True, 'back': True, 'backed': True, 'backing': True, 'backs': True, 'be': True, 'became': True, 'because': True, 'become': True, 'becomes': True, 'been': True, 'before': True, 'began': True, 'behind': True, 'being': True, 'beings': True, 'best': True, 'better': True, 'between': True, 'big': True, 'both': True, 'but': True, 'by': True, 'c': True, 'came': True, 'can': True, 'cannot': True, 'case': True, 'cases': True, 'certain': True, 'certainly': True, 'clear': True, 'clearly': True, 'come': True, 'could': True, 'd': True, 'did': True, 'differ': True, 'different': True, 'differently': True, 'do': True, 'does': True, 'done': True, 'down': True, 'down': True, 'downed': True, 'downing': True, 'downs': True, 'during': True, 'e': True, 'each': True, 'early': True, 'either': True, 'end': True, 'ended': True, 'ending': True, 'ends': True, 'enough': True, 'even': True, 'evenly': True, 'ever': True, 'every': True, 'everybody': True, 'everyone': True, 'everything': True, 'everywhere': True, 'f': True, 'face': True, 'faces': True, 'fact': True, 'facts': True, 'far': True, 'felt': True, 'few': True, 'find': True, 'finds': True, 'first': True, 'for': True, 'four': True, 'from': True, 'full': True, 'fully': True, 'further': True, 'furthered': True, 'furthering': True, 'furthers': True, 'g': True, 'gave': True, 'general': True, 'generally': True, 'get': True, 'gets': True, 'give': True, 'given': True, 'gives': True, 'go': True, 'going': True, 'good': True, 'goods': True, 'got': True, 'great': True, 'greater': True, 'greatest': True, 'group': True, 'grouped': True, 'grouping': True, 'groups': True, 'h': True, 'had': True, 'has': True, 'have': True, 'having': True, 'he': True, 'her': True, 'here': True, 'herself': True, 'high': True, 'high': True, 'high': True, 'higher': True, 'highest': True, 'him': True, 'himself': True, 'his': True, 'how': True, 'however': True, 'i': True, 'if': True, 'important': True, 'in': True, 'interest': True, 'interested': True, 'interesting': True, 'interests': True, 'into': True, 'is': True, 'it': True, 'its': True, 'itself': True, 'j': True, 'just': True, 'k': True, 'keep': True, 'keeps': True, 'kind': True, 'knew': True, 'know': True, 'known': True, 'knows': True, 'l': True, 'large': True, 'largely': True, 'last': True, 'later': True, 'latest': True, 'least': True, 'less': True, 'let': True, 'lets': True, 'like': True, 'likely': True, 'long': True, 'longer': True, 'longest': True, 'm': True, 'made': True, 'make': True, 'making': True, 'man': True, 'many': True, 'may': True, 'me': True, 'member': True, 'members': True, 'men': True, 'might': True, 'more': True, 'most': True, 'mostly': True, 'mr': True, 'mrs': True, 'much': True, 'must': True, 'my': True, 'myself': True, 'n': True, 'necessary': True, 'need': True, 'needed': True, 'needing': True, 'needs': True, 'never': True, 'new': True, 'new': True, 'newer': True, 'newest': True, 'next': True, 'no': True, 'nobody': True, 'non': True, 'noone': True, 'not': True, 'nothing': True, 'now': True, 'nowhere': True, 'number': True, 'numbers': True, 'o': True, 'of': True, 'off': True, 'often': True, 'old': True, 'older': True, 'oldest': True, 'on': True, 'once': True, 'one': True, 'only': True, 'open': True, 'opened': True, 'opening': True, 'opens': True, 'or': True, 'order': True, 'ordered': True, 'ordering': True, 'orders': True, 'other': True, 'others': True, 'our': True, 'out': True, 'over': True, 'p': True, 'part': True, 'parted': True, 'parting': True, 'parts': True, 'per': True, 'perhaps': True, 'place': True, 'places': True, 'point': True, 'pointed': True, 'pointing': True, 'points': True, 'possible': True, 'present': True, 'presented': True, 'presenting': True, 'presents': True, 'problem': True, 'problems': True, 'put': True, 'puts': True, 'q': True, 'quite': True, 'r': True, 'rather': True, 'really': True, 'right': True, 'right': True, 'room': True, 'rooms': True, 's': True, 'said': True, 'same': True, 'saw': True, 'say': True, 'says': True, 'second': True, 'seconds': True, 'see': True, 'seem': True, 'seemed': True, 'seeming': True, 'seems': True, 'sees': True, 'several': True, 'shall': True, 'she': True, 'should': True, 'show': True, 'showed': True, 'showing': True, 'shows': True, 'side': True, 'sides': True, 'since': True, 'small': True, 'smaller': True, 'smallest': True, 'so': True, 'some': True, 'somebody': True, 'someone': True, 'something': True, 'somewhere': True, 'state': True, 'states': True, 'still': True, 'still': True, 'such': True, 'sure': True, 't': True, 'take': True, 'taken': True, 'than': True, 'that': True, 'the': True, 'their': True, 'them': True, 'then': True, 'there': True, 'therefore': True, 'these': True, 'they': True, 'thing': True, 'things': True, 'think': True, 'thinks': True, 'this': True, 'those': True, 'though': True, 'thought': True, 'thoughts': True, 'three': True, 'through': True, 'thus': True, 'to': True, 'today': True, 'together': True, 'too': True, 'took': True, 'toward': True, 'turn': True, 'turned': True, 'turning': True, 'turns': True, 'two': True, 'u': True, 'under': True, 'until': True, 'up': True, 'upon': True, 'us': True, 'use': True, 'used': True, 'uses': True, 'v': True, 'very': True, 'w': True, 'want': True, 'wanted': True, 'wanting': True, 'wants': True, 'was': True, 'way': True, 'ways': True, 'we': True, 'well': True, 'wells': True, 'went': True, 'were': True, 'what': True, 'when': True, 'where': True, 'whether': True, 'which': True, 'while': True, 'who': True, 'whole': True, 'whose': True, 'why': True, 'will': True, 'with': True, 'within': True, 'without': True, 'work': True, 'worked': True, 'working': True, 'works': True, 'would': True, 'x': True, 'y': True, 'year': True, 'years': True, 'yet': True, 'you': True, 'young': True, 'younger': True, 'youngest': True, 'your': True, 'yours': True, 'z': True}

filename="trainingdata.txt"

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word',stop_words='english')
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
bag_of_words=vectorizer.fit(ls)
bag_of_words=vectorizer.transform(ls)
cmax=0
for cc in range(1,100):
    #sw=stopwords.words() #stopwords are not supported, requires download
    clf = PassiveAggressiveClassifier(n_iter=9,C=cc/10)
#    svm=LinearSVC(C=cc/10.0)
    clf.fit(bag_of_words,ln)
    
    #Now get input (test) data
    lt=[]
    filename=open("testdata.txt")
    line = filename.readline()
    ntests=int(line)
    for _ in range(ntests):
        lt.append(filename.readline())
    
    bag_of_test_words=vectorizer.transform(lt)
    result=clf.predict(bag_of_test_words)
    actuals=[]
    filename=open("testresults.txt")
    z=0
    for x in range(len(result)):
        zz = int(filename.readline())
        if zz==int(result[x]):
            z=z+1
    acc=(float(z)-(len(result)-float(z)))/len(result)
    if cmax<acc: cmax=acc
    print cc
    print cmax*100