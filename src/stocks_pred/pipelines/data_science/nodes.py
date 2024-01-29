import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error
from autogluon.tabular import TabularDataset, TabularPredictor
import pickle
import wandb

def create_model(X_train, y_train, model_type, hyper):
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # if(model_type == "autogluon"):

    #     label = 'stocks_pred'
    #     dataset = TabularDataset(X_train)
    #     clf = TabularPredictor(label)
    #     clf.fit(dataset, hyperparameters=hyper)
    # elif(model_type == "regression"):
    #     X_train = X_train.drop("stocks_pred", axis=1)
    #     clf = LogisticRegression()
    #     clf.fit(X_train, y_train)
    # else:            
    #     X_train = X_train.drop("stocks_pred", axis=1)   
    #     clf = RandomForestClassifier(n_estimators=100, random_state=42)
    #     clf.fit(X_train, y_train)
     
    coln = []
    for col in X_train.columns:
        coln.append(col)
        
    wandb.sklearn.plot_learning_curve(model, X_train, y_train)
    wandb.sklearn.plot_feature_importances(model, coln)
    
    return model

def predict(X_test, y_test, clf):
    
    y_pred = clf.predict(X_test)
    wandb.sklearn.plot_confusion_matrix(y_test, y_pred, ['Up', 'Down'])   
    accuracy = accuracy_score(y_test, y_pred)
    wandb.log({"accuracy": accuracy})
    return accuracy
    
def save_model(clf):
    pickle.dump(clf, open('src\\fastapi\model.pkl', 'wb'))
    