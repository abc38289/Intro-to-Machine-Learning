#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import numpy as np
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def SVMAccuracy(features_train, labels_train, features_test, labels_test):

    #features_train = features_train[:int(len(features_train)/100)]
    #labels_train = labels_train[:int(len(labels_train)/100)]

    clf = SVC(kernel="rbf", C=10000)

    ### Record time for training
    t0 = time()

    clf.fit(features_train, labels_train)
    training_time = round(time()-t0, 3)

    ### Record time for predicting
    t0 = time()

    pred = clf.predict(features_test)
    predicting_time = round(time()-t0, 3)

    # Extract and print predicted classes for specific elements
    #predicted_class_10 = pred[10]  # Element 10 (Python uses 0-based indexing)
    #predicted_class_26 = pred[26]  # Element 26
    #predicted_class_50 = pred[50]  # Element 50

    #print("Predicted class for element 10:", predicted_class_10)
    #print("Predicted class for element 26:", predicted_class_26)
    #print("Predicted class for element 50:", predicted_class_50)

    # Count the number of events predicted to be in the "Chris" (1) class
    chris_count = np.sum(pred == 1)

    acc = accuracy_score(pred, labels_test)
    return acc, training_time, predicting_time, chris_count

acc, training_time, predicting_time, chris_count = SVMAccuracy(features_train, labels_train, features_test, labels_test)

# Print the results
print("Accuracy:", acc)
print("Training Time:", training_time, "s")
print("Predicting Time:", predicting_time, "s")
print("Number of events predicted to be in the 'Chris' (1) class:", chris_count)
#########################################################

#########################################################
'''
You'll be Provided similar code in the Quiz
But the Code provided in Quiz has an Indexing issue
The Code Below solves that issue, So use this one
'''

# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[:int(len(labels_train)/100)]

#########################################################


### The Answer

# Accuracy: 0.9840728100113766
# Training Time: 83.629 s
# Predicting Time: 8.015 s


### A Smaller Training Set
## When we add smaller training set into the function, the answer change below
# Accuracy: 0.8845278725824801
# Training Time: 0.023 s
# Predicting Time: 0.177 s






