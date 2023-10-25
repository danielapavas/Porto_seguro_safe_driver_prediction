import argparse
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from loguru import logger
import os

# Argumentos de línea de comandos

parser = argparse.ArgumentParser(description="Entrenar un modelo y guardar una nueva versión")
parser.add_argument('--data_file', required=True, type=str, help='train.csv')
parser.add_argument('--model_file', required=True, type=str, help='model.pkl')
parser.add_argument('--overwrite_model', default=False, action='store_true', help='Si se establece, sobrescribe el archivo del modelo si ya existe')

args = parser.parse_args()

model_file = args.model_file
data_file = args.data_file
overwrite = args.overwrite_model

if os.path.isfile(model_file) and not overwrite:
    logger.info(f"El archivo del modelo {model_file} ya existe. Utilice la opción --overwrite_model para sobrescribirlo.")
    exit(-1)

try:
    logger.info("Cargando los datos de entrenamiento")
    train_data = pd.read_csv(data_file)
    Xtr = train_data.values[:, :-1]  # Se asume que la última columna es la etiqueta y se excluye
    ytr = train_data.values[:, -1]  # La última columna se asume como la etiqueta

    logger.info("Entrenando el modelo")
    model = RandomForestClassifier()
    model.fit(Xtr, ytr)

    logger.info(f"Modelo entrenado con éxito.")

    # Calcula y muestra la precisión en los datos de entrenamiento
    train_accuracy = model.score(Xtr, ytr)
    logger.info(f"Precisión en los datos de entrenamiento: {train_accuracy:.2f}")

    logger.info(f"Guardando el modelo en {model_file}")
    joblib.dump(model, model_file)

except Exception as e:
    logger.error(f"Error al cargar los datos o entrenar el modelo: {str(e)}")
