__author__ = 'priya'

'''
Flows A. Train B. Test C. Modify
A. Train
1. Initialize database. Call database.py
2. Stream Twitter data
3. Call TextProcessing.py
4. libsvminput
5. testSVM

B. Test
1. Initialize testdatabase. Call database.py
2. Stream Twitter data
3. Call TextProcessing.py
4. libsvminput
5. testSVM

C. Modify
'''
from nlp import TextProcessing as tp

from database import Database as db
from database import TestDatabase as tdb
#from twist.stream import collectTweets
from svm import SVMProcessing as svmp

if __name__=='__main__':
    flow=input("1.Train 2.Classify 3.Re-classify")
    if flow==1:
        #initialize the databases
        db.clear()
        #db.InitializeDB()
        #stream twitter data
        #to-do insert python streaming code here
        #Pre-process tweets
        tp.process(1)

        #TF-IDF
        db.tfidf()
        #SVM Processing
        #1. Create libSVM file
        svmp.createTrainFile()
        #2. Train the SVM
        svmp.trainSVM()
    elif flow==2:
        #initialize the test databases
        #tdb.InitializeTestDB()
        tdb.clear()
        #stream twitter data
        #to-do insert python streaming code here
        #Pre-process tweets
        tp.process(2)
        tdb.tfidf()
        #SVM Processing
        #1. Create libSVM file
        svmp.createTestFile()
        #2. Train the SVM
        #svmp.testSVM()
    elif flow==3:
        print "nothign"

        # Edit the databases with the re-classified tweet
        # Fit the re-classified tweet into the SVM
