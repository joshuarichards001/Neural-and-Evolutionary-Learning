import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report


# Main code
if __name__ == '__main__':
    # creating data structures
    train_set = pd.read_csv("p2_data/wine_training", sep=" ")
    test_set = pd.read_csv("p2_data/wine_test", sep=" ")

    # creating x and y axis
    x_train = train_set.drop("Class", axis=1)
    y_train = train_set["Class"]
    x_test = test_set.drop("Class", axis=1)
    y_test = test_set["Class"]

    # scaling data
    scaler = StandardScaler().fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    # training model
    mlp = MLPClassifier(max_iter=100)
    mlp.fit(x_train, y_train)

    # predicting test data
    prediction = mlp.predict(x_test)

    print(classification_report(y_test, prediction))
