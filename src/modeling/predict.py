# Este script carga un modelo entrenado y realiza predicciones sobre un nuevo conjunto de datos.
# Asegúrate de que los datos de entrada estén en el formato correcto antes de realizar predicciones.
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, mean_absolute_error

def load_processed_data(file_path):
    """
    Cargar los datos procesados desde un archivo CSV.
    """
    return pd.read_csv(file_path)

def load_model(model_path):
    """
    Cargar el modelo entrenado desde un archivo.
    """
    return joblib.load(model_path)

def make_predictions(model, X_test):
    """
    Realizar predicciones utilizando el modelo entrenado.
    """
    return model.predict(X_test)

def save_predictions(real_values, predictions, file_path):
    """
    Guardar las predicciones junto con los valores reales en un archivo CSV.
    """
    results = pd.DataFrame({
        'Real_RUL': real_values,
        'Predicted_RUL': predictions
    })
    results.to_csv(file_path, index=False)

def evaluate_predictions(real_values, predictions):
    """
    Evaluar las predicciones comparando con los valores reales.
    """
    mse = mean_squared_error(real_values, predictions)
    mae = mean_absolute_error(real_values, predictions)
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"Mean Absolute Error (MAE): {mae}")
    return mse, mae

if __name__ == "__main__":
    # Ruta a los datos procesados de prueba
    processed_data_path = "data/processed/test_FD001_processed.csv"
    
    # Cargar los datos de prueba procesados
    df_test = load_processed_data(processed_data_path)
    
    # Supongamos que la última columna es el RUL y las demás son características
    X_test = df_test.iloc[:, :-1]
    y_test = df_test.iloc[:, -1]
    
    # Ruta al modelo entrenado
    model_path = "models/random_forest_model.pkl"
    
    # Cargar el modelo entrenado
    model = load_model(model_path)
    
    # Realizar predicciones
    predictions = make_predictions(model, X_test)
    
    # Evaluar las predicciones
    mse, mae = evaluate_predictions(y_test, predictions)
    
    # Guardar las predicciones y los valores reales
    predictions_path = "data/processed/test_FD001_predictions.csv"
    save_predictions(y_test, predictions, predictions_path)
    
    print(f"Predicciones guardadas en: {predictions_path}")
