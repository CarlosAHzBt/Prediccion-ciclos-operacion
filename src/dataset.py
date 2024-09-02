# Este script carga datos desde fuentes externas y los guarda en la carpeta data/raw/.
# Ejemplo: Descargar un conjunto de datos de una API y guardarlo como CSV.
# Este script se encarga de la carga y guardado de datos desde y hacia diferentes fuentes.
# Incluye funciones para cargar datos crudos, transformarlos y guardarlos en la estructura del proyecto.


import pandas as pd
from sklearn.preprocessing import StandardScaler
 
def load_data(file_path):
    """
    Cargar los datos desde un archivo de texto.
    
    Args:
        file_path (str): Ruta al archivo de datos.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    df = pd.read_csv(file_path, sep=" ", header=None)
    df.dropna(axis=1, how="all", inplace=True)  # Eliminar columnas vacías
    return df



def preprocess_data(df):
    """
    Preprocesar los datos (normalización, selección de características, etc.)
    
    Args:
        df (pd.DataFrame): DataFrame con los datos crudos.

    Returns:
        pd.DataFrame: DataFrame con los datos preprocesados.
    """
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    return pd.DataFrame(df_scaled)

def save_processed_data(df, file_path):
    """
    Guardar los datos preprocesados en un archivo.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos preprocesados.
        file_path (str): Ruta donde se guardarán los datos.
    """
    df.to_csv(file_path, index=False)


# Ejemplo de uso:
if __name__ == "__main__":
    raw_data_path = "data/raw/test_FD001.txt"  # Cambia esto según el archivo que quieras cargar
    processed_data_path = "data/processed/test_FD001_processed.csv"

    # Cargar datos
    df = load_data(raw_data_path)
    print(f"Datos cargados: {df.shape}")

    # Preprocesar datos
    df_processed = preprocess_data(df)
    print(f"Datos preprocesados: {df_processed.shape}")

    # Guardar datos procesados
    save_processed_data(df_processed, processed_data_path)
    print(f"Datos guardados en: {processed_data_path}")