import sys
from sqlalchemy import create_engine
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
import nltk
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics import classification_report
from sklearn.utils.multiclass import type_of_target
from sklearn.model_selection import GridSearchCV
import pickle

def load_data(database_filepath):
    """ Load data from database """

    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql_table("message", engine)
    X = df['message'].values
    Y = df.iloc[:, 4:].values
    category_names = list(df.iloc[:, 4:].columns)
    return X, Y, category_names


def tokenize(text):
    """ Tokenize the text data """

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    """ Create model pipeline """

    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])

    parameters = {
        'clf__estimator__criterion': ["gini", "entropy"]
    }

    cv = GridSearchCV(pipeline, param_grid=parameters)
    
    return cv



def evaluate_model(model, X_test, Y_test, category_names):
    """ Evaluate the model performance """

    # Predict on test data
    Y_pred = model.predict(X_test)

    index = 0
    for category in category_names:
        print("Category in column {}: {}".format(index, category))
        evaluation_report = classification_report(Y_test[:, index], Y_pred[:, index])
        index += 1
        print(evaluation_report)

    print("Best param of the model: {}".format(model.best_params_))


def save_model(model, model_filepath):
    """ Save model as pickle file """

    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()