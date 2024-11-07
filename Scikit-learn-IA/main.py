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


from sklearn.datasets import fetch_california_housing
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
print('Error cuadrático medio : ', mse)