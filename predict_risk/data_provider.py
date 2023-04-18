import os
import pickle
import joblib

config = {
    'heart': {
        'SVC': 'production/svc_model.pkl',
        'LogisticRegression': 'production/Logistic_regression_model.pkl',
        'NaiveBayes': 'production/naive_bayes_model.pkl',
        'DecisionTree':'production/decision_tree_model.pkl',
        'scalar_file': 'production/standard_scalar.pkl',
        'deep_learning': 'production/deep_learning_model.pkl',
        'KNN': 'production/KNN_model.pkl',
    }}

dir = os.path.dirname(__file__)

def GetJobLibFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    return None

def GetPickleFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return pickle.load( open(os.path.join(dir, filepath), "rb" ) )
    return None

def GetStandardScalarForHeart():
    return GetPickleFile(config['heart']['scalar_file'])

def GetAllClassifiersForHeart():
    return (GetSVCClassifierForHeart(),GetLogisticRegressionClassifierForHeart(),GetNaiveBayesClassifierForHeart(),GetDecisionTreeClassifierForHeart(),GetDeepLearningClassifierForHeart(),GetKNNClassifierForHeart())

def GetSVCClassifierForHeart():
    return GetJobLibFile(config['heart']['SVC'])

def GetLogisticRegressionClassifierForHeart():
    return GetJobLibFile(config['heart']['LogisticRegression'])

def GetNaiveBayesClassifierForHeart():
    return GetJobLibFile(config['heart']['NaiveBayes'])

def GetDecisionTreeClassifierForHeart():
    return GetJobLibFile(config['heart']['DecisionTree'])

def GetKNNClassifierForHeart():
    return GetJobLibFile(config['heart']['KNN'])

def GetDeepLearningClassifierForHeart():
    return GetJobLibFile(config['heart']['deep_learning'])


