import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
np.random.seed(42)
genuine_speed = np.random.normal(loc=3.0, scale=0.5, size=50)
genuine_pressure = np.random.normal(loc=0.8, scale=0.1, size=50)
genuine_labels = [0] * 50
fraud_speed = np.random.normal(loc=1.5, scale=0.5, size=50)
fraud_pressure = np.random.normal(loc=0.3, scale=0.1, size=50)
fraud_labels = [1] * 50
data = pd.DataFrame({
    "typing_speed": np.concatenate([genuine_speed, fraud_speed]),
    "tap_pressure": np.concatenate([genuine_pressure, fraud_pressure]),
    "label": genuine_labels + fraud_labels
})
X = data[["typing_speed", "tap_pressure"]]
y = data["label"]
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
with open("anomaly_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("✅ Model trained and saved as 'anomaly_model.pkl'")
