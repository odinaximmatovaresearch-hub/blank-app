import joblib
import numpy as np

def load_model(path="data/model.pkl"):
    try:
        model = joblib.load(path)
        return model
    except Exception:
        return None

def predict_activity(model, descriptors):
    if model is None or descriptors is None:
        return None
    X = np.array([[v for v in descriptors.values()]])
    if hasattr(model, "predict_proba"):
        y_pred = model.predict_proba(X)[0][1] * 100
    else:
        y_pred = model.predict(X)[0]
    return round(float(y_pred), 2)
