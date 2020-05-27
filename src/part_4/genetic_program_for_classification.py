import graphviz
import pandas as pd


# Main code
from gplearn.genetic import SymbolicClassifier
from sklearn.metrics import roc_auc_score

if __name__ == '__main__':
    # creating data structures
    train_set = pd.read_csv("satellite", sep=" ")

    # creating x and y axis
    x_train = train_set.drop("Target", axis=1)
    y_train = train_set["Target"]

    est = SymbolicClassifier(parsimony_coefficient=.01,
                             feature_names=list(x_train.columns.values),
                             random_state=1)
    est.fit(x_train, y_train)

    y_true = y_train
    y_score = est.predict_proba(x_train)[:, 1]
    print(roc_auc_score(y_true, y_score))
