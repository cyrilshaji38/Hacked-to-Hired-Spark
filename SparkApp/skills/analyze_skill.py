import pandas as pd 
from sklearn.model_selection import train_test_split   # To split the dataset for training and testing.
from sklearn import svm   # For suport vector machine algorithm.
from sklearn import metrics   # For checking the model accuracy.
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

def lacking_skill(wb):
    hb = pd.read_csv(r"SparkApp/skills/train_data.csv")

    train, test = train_test_split(hb, test_size=0.3)   # Our main data splits into two, train=70% and test=30%

    train_X = train[['Time Management', 'Evaluating', 'Questioning', 'Describing', 'Empathy', 'Creativity ']]   # Taking the training data features.
    train_y = train.skill   # Output of the training data.

    test_X = test[['Time Management', 'Evaluating', 'Questioning', 'Describing', 'Empathy', 'Creativity ']]
    test_y = test.skill

    # Select the svm algorithm and train the algorithm with training data and training output.
    rbg_alg = svm.SVC(kernel='rbf', C=1).fit(train_X, train_y)
    rgb_pred = rbg_alg.predict(test_X)   # We pass the testing data to the stored algorithm to predict the outcome.
    rgb_accuracy = accuracy_score(test_y, rgb_pred)
    rgb_f1 = f1_score(test_y, rgb_pred, average='weighted')
    accuracy = ('Accuracy (rbf Kernel): ', "%.2f" % (rgb_accuracy*100))   # We check the accuracy of the algorithm.
    # print('F1 (rbf Kernel): ', "%.2f" % (rgb_f1*100))
   
    final = pd.DataFrame(wb)
    prediction =rbg_alg.predict(final)[0]   # Output predicted using wb as input.
    return prediction