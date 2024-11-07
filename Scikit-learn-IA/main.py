#PRIMER EJERCICIO
'''from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#carga el conjunto de datos
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size = 0.2, random_state = 42)


#Crea el modelo
clf = KNeighborsClassifier(n_neighbors = 3)


#Entrena el modelo
clf.fit(X_train, y_train)

#Hace la prediccion
y_pred = clf.predict(X_test)

#Hace el calculo
accuracy = accuracy_score(y_test, y_pred)
print('Presición del clasificador: ', accuracy)'''

#SEGUNDO EJERCICIO
'''from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


#Carga de datos
California = fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(California.data,California.target,test_size = 0.2, random_state = 42)


#Crea el modelo de Regresion
model = LinearRegression()

#Entrena el modelo
model.fit(X_train, y_train)

#Predice los precios
y_pred = model.predict(X_test)

#Calcula el error cuadratico
mse = mean_squared_error(y_test, y_pred)
print('Error cuadrático medio : ', mse)'''

#TERCER EJERCICIO
'''from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
# cargar de datos
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size = 0.2, random_state = 42)

print('Numero de muestras en el conjunto de entrenamiento: ', len(X_train))
print('Numero de muestras en el conjunto de prueba: ', len(X_test))'''

#CUARTO EJERCICIO
from sklearn.datasets import load_iris
from sklearn. model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data,
iris.target,
test_size=0.2,
random_state=42)

# Crear el clasificador de vecinos mas cercanos
clf = KNeighborsClassifier(n_neighbors=3)
# Entrenar el clasificador
clf.fit(X_train, y_train)
# Predecir las etiquetas para los datos de prueba
y_pred = clf.predict(X_test)
# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print('Precisión del clasificador:', accuracy)
# Predicciones del modelo
y_pred = clf.predict(X_test)
# Calcular métricas de evaluación del modelo
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted' )
print("Precision:", accuracy)
print("Precisión promedio ponderada:", precision)
print("Recall promedio ponderado:", recall)
print("F1-score promedio ponderado:", f1)