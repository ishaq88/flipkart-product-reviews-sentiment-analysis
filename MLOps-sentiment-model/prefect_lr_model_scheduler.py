import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import joblib
import time
from joblib import Memory

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

from sklearn.model_selection import GridSearchCV

from prefect import flow, task

@task
def load_data(csv_path):
    '''
    Given a path this function loads the data from csv in a pandas dataframe.
    '''
    df = pd.read_csv(path)
    df = df.loc[df['label'] != 'neutral']
    label_map = {'negative': 0, 'positive': 1}
    df['label'] = df['label'].map(label_map)
    return df



@task
def separate_inputs_outputs(data, inputs, outputs):
    '''
    separate the inputs and outputs from the data
    '''

    X = data[inputs]
    y = data[outputs]

    return X, y



@task
def split_train_test(X, y, test_size=0.25, random_state=42):
    '''
    splits the training and test data from inputs and outputs
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test



@task
def train_lr_model(X_train, y_train, **hyperparameters):

    cachedir = '.cache'
    memory = Memory(location=cachedir, verbose=0)
    
    pipe = Pipeline([
        ('vectorization', CountVectorizer()),
        ('classifier', LogisticRegression())
    ], memory=memory)

    clf = GridSearchCV(estimator=pipe, 
                               param_grid=hyperparameters, 
                               cv=3, 
                               scoring='f1', 
                               return_train_score=True,
                               verbose=1
                              )

    clf.fit(X_train, y_train)
    return clf



@task
def evaluate_lr_model(model, X_train, y_train, X_test, y_test):
    """
    Evaluating the model.
    """
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

        
    train_score = metrics.f1_score(y_train, y_train_pred)
    test_score = metrics.f1_score(y_test, y_test_pred)
    
    return train_score, test_score


@flow(name="LR Training flow", version="flow-1-LR")
def workflow():
    DATA_PATH = 'F:/innomatics/sentiment_analysis_project/reviews_data_dump/labeled_sentiment_flipkart_reviews.csv'
    INPUT = 'review_text'
    OUTPUT = 'label'
    HYPERPARAMETERS = {'vectorization': [CountVectorizer()], 
                       'vectorization__max_features': [1000], 
                       'classifier__C': [10], 
                       'classifier__penalty': ['l2'], 
                       'classifier__solver': ['saga'], }

    #load data
    data = load_data(DATA_PATH)

    #Identify inputs and outputs
    X, y = separate_inputs_outputs(data, INPUT, OUTPUT)

    #split train and test data
    X_train, X_test, y_train, y_test = split_train_test(X, y)

    # Build a model
    model = train_lr_model(X_train, y_train, **HYPERPARAMETERS)
    
    # Evaluation
    train_score, test_score = evaluate_lr_model(model, X_train, y_train, X_test, y_test)
    
    print("Train f1 Score:", train_score)
    print("Test f1 Score:", test_score)


if __name__  == '__main__':
    path = 'F:/innomatics/sentiment_analysis_project/reviews_data_dump/labeled_sentiment_flipkart_reviews.csv'
    workflow.serve(
        name="my-first-deployment",
        cron="5 * * * *"
    )