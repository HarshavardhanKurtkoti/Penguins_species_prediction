from sklearn.ensemble import RandomForestClassifier

def train_model(df):

    """
    Trains a Random Forest model on the provided data.
    Returns the trained classifier.
    """

    X = df.drop('species', axis=1)
    y = df['species']
    
    clf = RandomForestClassifier()
    clf.fit(X, y)
    return clf

def predict_species(clf, input_data):

    """
    Predicts the species for the given input data using the trained model.
    Returns the predicted species and probabilities.
    """
    
    prediction = clf.predict(input_data)
    prediction_proba = clf.predict_proba(input_data)
    return prediction, prediction_proba
