# Usa una imagen base de Python
FROM python:3.11

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos locales al contenedor
COPY train.py .
COPY predict.py .
COPY model.pkl .
COPY apirest.py .
COPY train.csv .

# Instala las bibliotecas necesarias
RUN pip install Flask scikit-learn pandas joblib

# Exponer el puerto en el que se ejecutará la aplicación Flask
EXPOSE 5000

# Comando por defecto cuando se arranca el contenedor
CMD ["python", "apirest.py"]
