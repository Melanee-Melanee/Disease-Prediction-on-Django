import os
import pickle
import joblib

config = {
    'Kidney': {
        'SVC': 'production/svc_model.pkl',
        'LogisticRegression': 'production/Logistic_regression_model.pkl',
        'NaiveBayes': 'production/naive_bayes_model.pkl',
        'DecisionTree':'production/decision_tree_model.pkl',
        'NN':'production/NN_model.pkl',
        'KNN':'production/KNN_model.pkl',
        'scalar_file_decision': 'production/standard_scalar_decision.pkl',
        'scalar_file_logistic': 'production/standard_scalar_logistic.pkl',
        'scalar_file_naive': 'production/standard_scalar_naive.pkl',
        'scalar_file_svc': 'production/standard_scalar_svc.pkl',
        'scalar_file_NN': 'production/standard_scalar_NN.pkl',
        'scalar_file_KNN': 'production/standard_scalar_KNN.pkl',

    }}

dir = os.getcwd()+'/predict_risk_1/'

def GetJobLibFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    return None

def GetPickleFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    return None

def GetStandardScalarForD():
    return GetPickleFile(config['Kidney']['scalar_file_decision'])

def GetStandardScalarForL():
    return GetPickleFile(config['Kidney']['scalar_file_logistic'])

def GetStandardScalarForN():
    return GetPickleFile(config['Kidney']['scalar_file_naive'])

def GetStandardScalarForS():
    return GetPickleFile(config['Kidney']['scalar_file_svc'])

def GetStandardScalarForNN():
    return GetPickleFile(config['Kidney']['scalar_file_NN'])

def GetStandardScalarForKNN():
    return GetPickleFile(config['Kidney']['scalar_file_KNN'])

def GetAllClassifiersForKidney():
    return (GetSVCClassifierForKidney(),GetLogisticRegressionClassifierForKidney(),GetNaiveBayesClassifierForKidney(),GetDecisionTreeClassifierForKidney(),GetNNClassifierForKidney(),GetKNNForKidney())

def GetSVCClassifierForKidney():
    return GetJobLibFile(config['Kidney']['SVC'])

def GetLogisticRegressionClassifierForKidney():
    return GetJobLibFile(config['Kidney']['LogisticRegression'])

def GetNaiveBayesClassifierForKidney():
    return GetJobLibFile(config['Kidney']['NaiveBayes'])

def GetDecisionTreeClassifierForKidney():
    return GetJobLibFile(config['Kidney']['DecisionTree'])

def GetNNClassifierForKidney():
    return GetJobLibFile(config['Kidney']['DecisionTree'])

def GetKNNForKidney():
    return GetJobLibFile(config['Kidney']['DecisionTree'])
