import joblib
model=joblib.load("linear_regression.pkl")
def predict(a):
    return model.predict([[a]])