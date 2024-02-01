def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    from sklearn.svm import SVC
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    
    clf = make_pipeline(StandardScaler(), SVC(C=1000000))
    clf.fit(features_train, labels_train)
    return(clf)

    
    