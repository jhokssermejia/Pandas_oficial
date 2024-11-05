#Importamos la libreria de pandas, fundamental para el análisis de datos
import pandas as pd 

#Define la ruta del archivo CSV
#Si el archivo está en la misma carpeta entonces solo se pone el nombre

path = 'Sesion_2/Online_Retail.csv'
retail_data = pd.read_csv(path, encoding = 'latin1')
print(type(retail_data))
print(retail_data.head())


