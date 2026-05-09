import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(filepath):
    data = pd.read_csv(filepath)

    X = data.drop(columns=["CompressiveStrength"])
    y = data["CompressiveStrength"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler