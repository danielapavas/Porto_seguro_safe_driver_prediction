from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

app = Flask(__name__)

# Cargar el modelo previamente entrenado
model = joblib.load('model.pkl')

# Endpoint para predicciones
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener datos del cuerpo de la solicitud
        data = request.get_json()

        # Convertir los datos en un DataFrame
        input_data = pd.DataFrame(data)

        # Realizar la predicción
        predictions = model.predict(input_data)

        # Devolver las predicciones en formato JSON
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

# Endpoint para entrenamiento
@app.route('/train', methods=['GET'])
def train():
    try:
        # Cargar datos de entrenamiento estándar
        train_data = pd.read_csv('train.csv')
        Xtr, ytr = train_data.iloc[:, :-1], train_data.iloc[:, -1]

        # Crear y entrenar un nuevo modelo
        new_model = RandomForestClassifier()
        new_model.fit(Xtr, ytr)

        # Guardar el nuevo modelo
        joblib.dump(new_model, 'new_model.pkl')

        return jsonify({'message': 'Entrenamiento completado y nuevo modelo guardado.'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
