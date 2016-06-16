# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 22:28:07 2016

@author: Pascal van de Wijdeven
"""

import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

try:
    filename = "SampleInput.txt"
    f = open(filename)
except:
    f= sys.stdin

# read input first
Desc=f.readline().replace('\n',' ')
Desc=Desc.replace("? ",". ")
Train_X=Desc.split(". ")

Test_X_Questions=[]
for _ in range(5):
    quest=f.readline().replace('\n',' ')
    Test_X_Questions.append(quest)
Answers=f.readline().replace('\n',' ')
Test_X_Answers=(Answers.split(";"))

#add labels to Descriptions by numbering them
Train_Y=[]
for i in range(len(Train_X)):
    Train_Y.append(i)

vectorizer = TfidfVectorizer(use_idf=False,  sublinear_tf=True, max_df=0.5, analyzer='word',stop_words="english")
Train_X = vectorizer.fit_transform(Train_X)
Test_X_Questions_V =vectorizer.transform(Test_X_Questions)
Test_X_Answers_V =vectorizer.transform(Test_X_Answers)

clf=LinearSVC(C=0.95)
clf.fit(Train_X,Train_Y)
Pred_Questions=clf.predict(Test_X_Questions_V)
Pred_Answers=clf.predict(Test_X_Answers_V)

# now match answers with questions
# first get obvious matches

Pred_Questions=Pred_Questions.tolist()
Pred_Answers=Pred_Answers.tolist()

Questions_remove=[]
Answers_remove=[]
Final_Answers={}
for x in range(5): 
    for y in range(5):
        if x not in Questions_remove and y not in Answers_remove:
            if Pred_Questions[x]==Pred_Answers[y] :
                Final_Answers[x]=y
                Questions_remove.append(x)
                Answers_remove.append(y)
        
#Now get closest matches
for x in range(5):
    if x not in Questions_remove:
        min_dif=1000
        for y in range(5):
            if y not in Answers_remove:
                if abs(int(x)-int(y))<min_dif:
                    min_dif=abs(int(x)-int(y))
                    min_y=y
        Final_Answers[x]=min_y
        Questions_remove.append(x)
        Answers_remove.append(min_y)

for i in range(5):
    print Test_X_Answers[Final_Answers[i]]