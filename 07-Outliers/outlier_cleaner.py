#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    # Calculate residuals
    errors = net_worths - predictions

    # Create a list of tuples (age, net_worth, error)
    cleaned_data = list(zip(ages, net_worths, errors))

    # Sort the list based on the absolute values of errors
    cleaned_data.sort(key=lambda x: abs(x[2]))

    # Determine the number of points to keep (90%)
    keep_count = int(0.9 * len(cleaned_data))

    # Keep the top 90% of points
    cleaned_data = cleaned_data[:keep_count]

    
    return cleaned_data

