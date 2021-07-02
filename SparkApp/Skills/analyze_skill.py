import pandas as pd 
from sklearn.model_selection import train_test_split   # To split the dataset for training and testing.
from sklearn import svm   # For suport vector machine algorithm.
from sklearn import metrics   # For checking the model accuracy.

def lacking_skill(wb):
    hb = pd.read_csv(r"SparkApp/skills/train_data.csv")

    train, test = train_test_split(hb, test_size=0.3)   # Our main data splits into two, train=70% and test=30%

    train_X = train[['Time Management', 'Evaluating', 'Questioning', 'Describing', 'Empathy', 'Creativity ']]   # Taking the training data features.
    train_y = train.skill   # Output of the training data.

    test_X = test[['Time Management', 'Evaluating', 'Questioning', 'Describing', 'Empathy', 'Creativity ']]
    test_y = test.skill

    model = svm.SVC()   # Select the svm algorithm
    
    model.fit(train_X, train_y)   # We train the algorithm with training data and training output.
    
    prediction = model.predict(test_X)   # We pass the testing data to the stored algorithm to predict the outcome.

    print('The accuracy of the SVM is: ', metrics.accuracy_score(prediction, test_y))   # We check the accuracy of the algorithm.

    final = pd.DataFrame(wb)
    prediction = model.predict(final)[0]   # Output predicted using wb as input.
    return prediction