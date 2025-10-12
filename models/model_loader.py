import numpy as np
from sklearn.linear_model import LogisticRegression

def load_model():
    """Oddiy demo modelni yaratadi"""
    model = LogisticRegression()
    X = np.array([[0], [1]])
    y = np.array([0, 1])
    model.fit(X, y)
    return model

def predict_activity(model, value: float):
    """Model yordamida bashorat qiladi"""
    pred = model.predict([[value]])
    return "Aktiv" if pred[0] == 1 else "Noaktiv"
