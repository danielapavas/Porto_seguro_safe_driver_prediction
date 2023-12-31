# Proyecto Porto Seguro Safe Driver Prediction

## Desarrollado por:
* DANIELA ANDREA PAVAS BEDOYA, CC 1192741700, Ingeniería de Sistemas


## Datos
Los datos del proyecto se toman de la competición [Porto Seguro Safe Driver Prediction](https://www.kaggle.com/competitions/porto-seguro-safe-driver-prediction/overview). Los pasos para hacerlos disponibles en google collab son los siguientes:  

1. Estando logueado en la cuenta de Kaggle, irse a Settings y dar click en "Create New Token":  

![image](https://github.com/danielapavas/Porto_seguro_safe_driver_prediction/assets/75345956/c82f4e8d-c7a4-4135-a875-6a512d50012f)


Después de dar click, se descargará un archivo llamado Kaggle.json

2. En el notebook de google Collab ejecutar las siguientes lineas de comando:
```
  !pip install kaggle
  
  from google.colab import files 
  files.upload()
```
Luego dar click en el boton "Elegir archivos" para cargar el archivo .json

![image](https://user-images.githubusercontent.com/55060788/233894298-1c75936e-c9ab-4c9d-8264-da97fa2920e0.png)


3. Por ultimo ejecutar las siguientes lineas de codigo:

```
  ! mkdir ~/.kaggle
  ! cp kaggle.json ~/.kaggle/
  ! chmod 600 ~/.kaggle/kaggle.json
  !kaggle competitions download -c porto-seguro-safe-driver-prediction
  !unzip porto-seguro-safe-driver-prediction.zip
```

4. Ejecutar el Contenedor desde la terminal en fase-2

```
  docker build -t my_model_image .
  docker run my_model_image
```

5. Ejecutar el Contenedor desde la terminal en fase-3

```
  docker build -t my_model_image .
  docker run -p 5000:5000 my_model_image
```
Luego se puede acceder a la apirest en:
```
  http://localhost:5000
```
Y para acceder a los endpoints en:
```
  http://localhost:5000/predict
  http://localhost:5000/train
```

Nota: Debido a que los archivos de test.csv y train.csv son demasiado pesados no se pudieron subir a este repositorio, sin embargo para para la ejecución local estos archivos se encontraban en la carpeta "data"


  
