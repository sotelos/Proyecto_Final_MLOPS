import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import os
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature

def run_experiment():
    # ESTO ASEGURA QUE TODO SE GUARDE EN UN SOLO LUGAR (OneDrive Proof)
    base_path = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_path, "..", "mlflow_final.db")
    mlflow.set_tracking_uri(f"sqlite:///{db_path}")
    
    # ... resto de tu código igual ...
    mlflow.set_experiment("Proyecto_Final_Seguros_EAN")

    # Carga de datos
    url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
    df = pd.read_csv(url)
    
    # Preprocesamiento: Variables dummy para Sexo, Fumador y Región
    df = pd.get_dummies(df, drop_first=True)
    
    X = df.drop('charges', axis=1)
    y = df['charges']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Iniciar MLflow
    mlflow.set_experiment("Proyecto_Final_Seguros_EAN")

    with mlflow.start_run(run_name="RandomForest_Baseline"):
        # Modelo
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Predicciones y Métricas
        preds = model.predict(X_test)
        mse = mean_squared_error(y_test, preds)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, preds)
        r2 = r2_score(y_test, preds)

        # Registro de métricas
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        # Firma y ejemplo (Crucial para Auditoría en la Rúbrica)
        signature = infer_signature(X_test, preds)
        input_example = X_test.iloc[0:1]

        # Guardar modelo
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="insurance_model",
            signature=signature,
            input_example=input_example,
            registered_model_name="ModeloSeguros_Final"
        )
        
        print(f"Éxito: Experimento finalizado con R2: {r2:.4f}")

if __name__ == "__main__":
    run_experiment()