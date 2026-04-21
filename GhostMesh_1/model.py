import numpy as np
from sklearn.ensemble import IsolationForest

def train_model():
    normal_data = np.random.normal(50, 10, (100, 3))
    model = IsolationForest(contamination=0.15)
    model.fit(normal_data)
    return model

model = train_model()

attack_history = []

def predict(data):
    data = np.array(data).reshape(1, -1)
    result = model.predict(data)
    score = model.decision_function(data)[0]

    return {
        "anomaly": True if result[0] == -1 else False,
        "confidence": round(abs(score) * 100, 2)
    }

def update_defender(features, anomaly):
    attack_history.append((features, anomaly))
    if len(attack_history) > 20:
        attack_history.pop(0)