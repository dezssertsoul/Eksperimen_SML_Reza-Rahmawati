import os
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import mlflow

def run_modelling():
    # Jalur dinamis agar bisa dibaca oleh MLflow Project saat re-training
    data_path = "dataset_preprocessing.csv"
    if not os.path.exists(data_path):
        data_path = "Workflow-CI/MLProject/dataset_preprocessing.csv"
        
    df = pd.read_csv(data_path)
    X = df[['Length']]
    y = df['Protocol']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    
    with mlflow.start_run(run_name="CI_ReTraining_RandomForest"):
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        # Manual Logging untuk kriteria Advance
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("max_depth", 10)
        mlflow.log_metric("accuracy", accuracy_score(y_test, y_pred))
        
        # Menyimpan artefak model
        mlflow.sklearn.log_model(model, "ci_model")
        print("[SUCCESS] Re-training via CI Workflow berhasil.")

if __name__ == '__main__':
    run_modelling()
