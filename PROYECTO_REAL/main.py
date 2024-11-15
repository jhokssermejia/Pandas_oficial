from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error, accuracy_score, precision_score, recall_score, f1_score

# Inicializar FastAPI
app = FastAPI()

# Cargar y preparar los datos
df = pd.read_csv('data.csv')
X = df.drop(columns='COUNTRY')  # Variables independientes
y = df['COUNTRY']               # Variable dependiente

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inicializar modelos
model = None
classification_metrics = None
regression_metrics = None

# Definir si se quiere usar clasificación o regresión
if y_train.dtype == 'object' or y_train.nunique() < 20:  # Ejemplo de condición para clasificación
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    
    # Realizar predicciones de prueba
    y_pred_class = model.predict(X_test)
    
    # Calcular métricas de evaluación de clasificación
    classification_metrics = {
        'accuracy': accuracy_score(y_test, y_pred_class),
        'precision': precision_score(y_test, y_pred_class, average='weighted'),
        'recall': recall_score(y_test, y_pred_class, average='weighted'),
        'f1_score': f1_score(y_test, y_pred_class, average='weighted')
    }
else:
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Realizar predicciones de prueba
    y_pred_reg = model.predict(X_test)
    
    # Calcular métricas de evaluación de regresión
    regression_metrics = {
        'mse': mean_squared_error(y_test, y_pred_reg)
    }

# Modelo de solicitud
class PredictionRequest(BaseModel):
    features: dict  # Diccionario con las características para la predicción

# Ruta de prueba del servidor
@app.get("/")
async def root():
    return {"message": "Servidor FastAPI activo"}

# Ruta para obtener las métricas de evaluación del modelo
@app.get("/metrics")
async def get_metrics():
    if classification_metrics:
        return {"classification_metrics": classification_metrics}
    elif regression_metrics:
        return {"regression_metrics": regression_metrics}
    else:
        return {"error": "No se encontraron métricas"}

# Ruta para realizar predicciones
@app.post("/predict")
async def predict(request: PredictionRequest):
    # Convertir los datos de entrada a un DataFrame
    input_data = pd.DataFrame([request.features])
    
    # Realizar la predicción
    prediction = model.predict(input_data)[0]  # Obtener el primer resultado
    return {"prediction": prediction}
