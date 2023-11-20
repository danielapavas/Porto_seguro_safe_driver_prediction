<<<<<<< HEAD
import argparse
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from loguru import logger
import os
import pandas as pd
import pickle
import joblib

# Argumentos de línea de comandos
parser = argparse.ArgumentParser()
parser.add_argument('--input_file', required=True, type=str, help='test.csv')
parser.add_argument('--predictions_file', required=True, type=str, help='predictions.csv')
parser.add_argument('--model_file', required=True, type=str, help='model.pkl')

args = parser.parse_args()

model_file = args.model_file
input_file = args.input_file
predictions_file = args.predictions_file

# Verificar si los archivos existen
if not os.path.isfile(model_file):
    logger.error(f"El archivo de modelo {model_file} no existe")
    exit(-1)

if not os.path.isfile(input_file):
    logger.error(f"El archivo de entrada {input_file} no existe")
    exit(-1)

try:
    # Cargar el modelo previamente entrenado
    logger.info("Cargando el modelo")
    model = joblib.load(model_file)

    # Cargar el conjunto de datos de entrada desde un archivo CSV
    logger.info("Cargando los datos de entrada")
    input_data = pd.read_csv(input_file)

    # Realizar predicciones
    logger.info("Realizando predicciones")
    predictions = model.predict(input_data)  # Utiliza el modelo para hacer predicciones en los datos de entrada

    # Crear un DataFrame con las predicciones y las columnas adecuadas
    output_df = pd.DataFrame({'Predicciones': predictions})

    # Guardar las predicciones en un archivo CSV
    logger.info(f"Guardando las predicciones en {predictions_file}")
    output_df.to_csv(predictions_file, index=False)
    logger.info("Predicciones guardadas con éxito.")
except Exception as e:
    logger.error(f"Ocurrió un error: {str(e)}")
=======
import argparse
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from loguru import logger
import os
import pandas as pd
import pickle
import joblib

# Argumentos de línea de comandos
parser = argparse.ArgumentParser()
parser.add_argument('--input_file', required=True, type=str, help='test.csv')
parser.add_argument('--predictions_file', required=True, type=str, help='predictions.csv')
parser.add_argument('--model_file', required=True, type=str, help='model.pkl')

args = parser.parse_args()

model_file = args.model_file
input_file = args.input_file
predictions_file = args.predictions_file

# Verificar si los archivos existen
if not os.path.isfile(model_file):
    logger.error(f"El archivo de modelo {model_file} no existe")
    exit(-1)

if not os.path.isfile(input_file):
    logger.error(f"El archivo de entrada {input_file} no existe")
    exit(-1)

try:
    # Cargar el modelo previamente entrenado
    logger.info("Cargando el modelo")
    model = joblib.load(model_file)

    # Cargar el conjunto de datos de entrada desde un archivo CSV
    logger.info("Cargando los datos de entrada")
    input_data = pd.read_csv(input_file)

    # Realizar predicciones
    logger.info("Realizando predicciones")
    predictions = model.predict(input_data)  # Utiliza el modelo para hacer predicciones en los datos de entrada

    # Crear un DataFrame con las predicciones y las columnas adecuadas
    output_df = pd.DataFrame({'Predicciones': predictions})

    # Guardar las predicciones en un archivo CSV
    logger.info(f"Guardando las predicciones en {predictions_file}")
    output_df.to_csv(predictions_file, index=False)
    logger.info("Predicciones guardadas con éxito.")
except Exception as e:
    logger.error(f"Ocurrió un error: {str(e)}")
>>>>>>> 32194d37c6a25127ffbe316cc8754b2696069fe9
