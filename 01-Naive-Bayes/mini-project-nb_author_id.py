#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


##############################################################
# Enter Your Code Here

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """Compute the accuracy of the Naive Bayes classifier."""
    
    ### Create classifier
    clf = GaussianNB()

    ### Record time for training
    t0 = time()

    ### Fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
    training_time = round(time()-t0, 3)

    ### Record time for predicting
    t0 = time()

    ### Use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)
    predicting_time = round(time()-t0, 3)

    ### Calculate and return the accuracy on the test data
    accuracy = accuracy_score(labels_test, pred)
    return accuracy, training_time, predicting_time

# Use NBAccuracy function with your training and testing data
# Replace the placeholder data with your actual training and testing data
# For example, replace 'features_train', 'labels_train', 'features_test', 'labels_test'
# with your actual feature and label data
accuracy, training_time, predicting_time = NBAccuracy(features_train, labels_train, features_test, labels_test)

# Print the results
print("Accuracy:", accuracy)
print("Training Time:", training_time, "s")
print("Predicting Time:", predicting_time, "s")
##############################################################

##############################################################
'''
You Will be Required to record time for Training and Predicting 
The Code Given on Udacity Website is in Python-2
The Following Code is Python-3 version of the same code
'''

# t0 = time()
# # < your clf.fit() line of code >
# print("Training Time:", round(time()-t0, 3), "s")

# t0 = time()
# # < your clf.predict() line of code >
# print("Predicting Time:", round(time()-t0, 3), "s")

##############################################################


### The Answer

# No. of Chris training emails :  7936
# No. of Sara training emails :  7884
# Accuracy: 0.9732650739476678
# Training Time: 1.346 s
# Predicting Time: 0.141 s












