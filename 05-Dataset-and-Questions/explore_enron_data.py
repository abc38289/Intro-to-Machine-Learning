#!/usr/bin/python3

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import joblib
import numpy as np
import seaborn as sns

enron_data = joblib.load(open("../final_project/final_project_dataset.pkl", "rb"))



# 1.Find the number of data points
num_data_points = len(enron_data)

print("How many data points are in the Enron dataset:",num_data_points)




# 2.Find the number of features are available
#for person, features_dict in enron_data.items():
    # Print the person's name and the number of features
#    print(f"{person}: Number of features = {len(features_dict)}")





# 3.Finding POIs in the Enron Data
poi_count = 0

for person, poi in enron_data.items():
    poi_count += int(enron_data[person]['poi'] == 1)

print("How many POIs are there in the E+F dataset:", poi_count)







# 4.Specify the path to poi_names.txt
poi_names_path = "../final_project/poi_names.txt"


# Read the file and count the number of lines
with open(poi_names_path, 'r') as file:
    # Skip the header lines
    poi_lines = file.readlines()[2:]

    # Count the number of POIs
    num_pois = len(poi_lines)

print("Number of POIs listed in poi_names.txt:", num_pois)    


''' Check the features name '''
# Choose a person from the dataset
'''chosen_person = 'COLWELL WESLEY'  # Replace with the actual name

# Get the features for the chosen person
features_for_chosen_person = enron_data[chosen_person]

# Print the feature names
print("Available feature names for", chosen_person, ":", list(features_for_chosen_person.keys()))'''




# 5.Find the total value of the stock belonging to James Prentice
for person, features in enron_data.items():
    if person == 'PRENTICE JAMES':
        total_value = features.get('total_stock_value', 0)
        break

print('What is the total value of the stock belonging to James Prentice?', total_value)




# 6. Find the total email messages form Wesley Colwell to persons of interest

# Iterate through each person in the dataset
for person, features in enron_data.items():
    # Check if the person is Wesley Colwell
    if person == 'COLWELL WESLEY':
        # Check if Wesley Colwell sent emails
        if features.get('from_this_person_to_poi', 0):
            # Add the number of emails to persons of interest
            total_email = features['from_this_person_to_poi']
            break

print('How many email messages do we have from Wesley Colwell to persons of interest?', total_email)





# 7. What’s the value of stock options exercised by Jeffrey K Skilling?
# Iterate through each person in the dataset
for person, features in enron_data.items():
    # Check if the person is Wesley Colwell
    if person == 'SKILLING JEFFREY K':
        # Check if Wesley Colwell sent emails
        if features.get('exercised_stock_options', 0):
            # Add the number of emails to persons of interest
            exercised_options = features['exercised_stock_options']
            break

print('What’s the value of stock options exercised by Jeffrey K Skilling?', exercised_options)




# 8. How much money did that person get?

''' Jerry Version
# Initialize variables
total_skilling = 0
total_lay = 0
total_fastow = 0

# Iterate through each person in the dataset
for person, features in enron_data.items():
    if person == 'SKILLING JEFFREY K':
        total_skilling = features.get('total_payments', 0)
    elif person == 'LAY KENNETH L':
        total_lay = features.get('total_payments', 0)
    elif person == 'FASTOW ANDREW S':
        total_fastow = features.get('total_payments', 0)
    

print("How much did Lay get?", total_lay)
print("How much did Skilling get?", total_skilling)
print("How much did Fastow get?", total_fastow)'''


''' Refine Version'''
# Initialize a dictionary to store total payments for each person
total_payments_dict = {'SKILLING JEFFREY K': 0, 'LAY KENNETH L': 0, 'FASTOW ANDREW S': 0}

# Iterate through each person in the dataset
for person, features in enron_data.items():
    # Check if the person is one of the specified individuals
    if person in total_payments_dict:
        # Update the total payments for the current person
        total_payments_dict[person] = features.get('total_payments', 0)

# Print the results
for person, total_payments in total_payments_dict.items():
    print(f"How much did {person[:-2]} get? {total_payments}")





# 9. How many folks in this dataset have a quantified salary? What about a known email address?
folks_counts = 0
email_counts = 0

for person, features in enron_data.items():
    if enron_data[person]['salary'] != 'NaN': # can also use features.get('salary')
        folks_counts += 1
    if features.get('email_address') != 'NaN':
        email_counts += 1

print("How many folks in this dataset have a quantified salary?", folks_counts)
print("What about a known email address counts?", email_counts)




# 10.
# How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? 
# What percentage of people in the dataset as a whole is this?
NaN_counts = 0
total_payments_counts = 0 

for person, features in enron_data.items():
    total_payments_counts += 1
    if features.get('total_payments') == 'NaN':
        NaN_counts += 1

percentage_of_people = NaN_counts / total_payments_counts *100

print("Total number of people in the E+F dataset:", total_payments_counts)
print("How many people have “NaN” for their total payments?", NaN_counts)
print("Percentage of people with 'NaN' for total payments:", percentage_of_people)





# 11.
# How many POIs in the E+F dataset have “NaN” for their total payments? 
# What percentage of POI’s as a whole is this?
NaN_POIs = 0
poi_count = 0

for person, features in enron_data.items():
    poi_count += int(features.get('poi') == 1)
    if features.get('poi') == 1 and features.get('total_payments') == 'NaN':
        NaN_POIs += 1

percentage_of_poi = NaN_POIs / poi_count * 100

print('How many POIs have "NaN" for their total payments?', NaN_POIs)
print("What percentage of POI's as a whole is this?", percentage_of_poi)






















