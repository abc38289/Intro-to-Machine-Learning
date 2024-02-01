import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################



#### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def TreeAccuracy(features_train, labels_train, features_test, labels_test):
  clf = DecisionTreeClassifier(random_state=0)
  clf.fit(features_train, labels_train)

  pred = clf.predict(features_test)

  acc = accuracy_score(pred, labels_test)

  return acc


acc = TreeAccuracy(features_train, labels_train, features_test, labels_test)
### be sure to compute the accuracy on the test set


    
def submitAccuracies():
  return {"acc":round(acc,3)}

