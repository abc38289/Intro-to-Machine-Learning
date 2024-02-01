#!/usr/bin/python3
import os
import joblib
import sys
import matplotlib.pyplot
sys.path.append(os.path.abspath("../tools/"))
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = joblib.load( open("../final_project/final_project_dataset.pkl", "rb") )
#remove the outliers
data_dict.pop('TOTAL', 0)
features_list = ["bonus", "salary"]
data = featureFormat(data_dict, features_list)
target, features = targetFeatureSplit(data)


### your code below
from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"




from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit(feature_train, target_train)


print("slope:", reg.coef_)
print("test data r-squared score:", reg.score(feature_test, target_test))



### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
	plt.scatter( feature, target, color=test_color )
for feature, target in zip(feature_train, target_train):
	plt.scatter( feature, target, color=train_color )

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")


### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
    plt.plot( feature_train, reg.predict(feature_train), color="g")   
except NameError:
    pass
reg.fit(feature_test, target_test) 
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()