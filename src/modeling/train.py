import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

def load_processed_data(file_path):
    return pd.read_csv(file_path)

def train_random_forest(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")
    return predictions

if __name__ == "__main__":
    # Cargar los datos procesados
    processed_data_path = "data/processed/test_FD001_processed.csv"
    df = load_processed_data(processed_data_path)
    
    # Supongamos que la última columna es el RUL y las demás son características
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Entrenar el modelo
    model = train_random_forest(X_train, y_train)
    
    # Evaluar el modelo
    predictions = evaluate_model(model, X_test, y_test)
    
    # Guardar el modelo entrenado
    joblib.dump(model, "models/random_forest_model.pkl")
