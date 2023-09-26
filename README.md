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
  !kaggle competitions download -c allstate-claims-severity
  !unzip allstate-claims-severity.zip
```
