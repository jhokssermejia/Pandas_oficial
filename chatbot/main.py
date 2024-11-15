from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from typing import List

# Datos y etiquetas de categorías
data = [
    {"category": "Saludo", "phrase": "hola"},
    {"category": "Saludo", "phrase": "¿cómo estás?"},
    {"category": "Saludo", "phrase": "buenos días"},
    {"category": "Saludo", "phrase": "buenas tardes"},
    {"category": "Saludo", "phrase": "buenas noches"},
    {"category": "Despedida", "phrase": "adiós"},
    {"category": "Despedida", "phrase": "hasta luego"},
    {"category": "Despedida", "phrase": "nos vemos"},
    {"category": "Despedida", "phrase": "me despido"},
    {"category": "Información de contacto", "phrase": "¿Cómo puedo contactarlos?"},
    {"category": "Información de contacto", "phrase": "¿Cuál es el número de teléfono?"},
    {"category": "Información de contacto", "phrase": "¿Tienen algún correo electrónico?"},
    {"category": "Información de contacto", "phrase": "¿Dónde están ubicados?"},
    {"category": "Información de contacto", "phrase": "¿Cómo puedo llegar a sus oficinas?"},
    {"category": "Horario de atención", "phrase": "¿Cuál es el horario de atención?"},
    {"category": "Horario de atención", "phrase": "¿En qué días están abiertos?"},
    {"category": "Horario de atención", "phrase": "¿Están abiertos los fines de semana?"},
    {"category": "Horario de atención", "phrase": "¿A qué hora abren?"},
    {"category": "Horario de atención", "phrase": "¿A qué hora cierran?"},
    {"category": "Precios", "phrase": "¿Cuánto cuesta el producto?"},
    {"category": "Precios", "phrase": "¿Cuál es el precio del servicio?"},
    {"category": "Precios", "phrase": "¿Tienen algún descuento?"},
    {"category": "Precios", "phrase": "¿Cuánto cuesta la suscripción mensual?"},
    {"category": "Precios", "phrase": "¿Cuál es el costo de envío?"},
    {"category": "Política de devolución", "phrase": "¿Cuál es la política de devoluciones?"},
    {"category": "Política de devolución", "phrase": "¿Puedo devolver el producto?"},
    {"category": "Política de devolución", "phrase": "¿Cuánto tiempo tengo para hacer una devolución?"},
    {"category": "Política de devolución", "phrase": "¿Necesito el recibo para una devolución?"},
    {"category": "Política de devolución", "phrase": "¿Es posible cambiar un producto?"},
    {"category": "Soporte técnico", "phrase": "Tengo un problema técnico"},
    {"category": "Soporte técnico", "phrase": "¿Cómo puedo solucionar un error?"},
    {"category": "Soporte técnico", "phrase": "¿Tienen soporte técnico?"},
    {"category": "Soporte técnico", "phrase": "Mi aplicación no funciona"},
    {"category": "Soporte técnico", "phrase": "¿Pueden ayudarme con un problema en mi cuenta?"},
]

# Extraer las frases y las categorías para entrenamiento
phrases = [item["phrase"] for item in data]
categories = [item["category"] for item in data]

# Crear y entrenar el clasificador Naive Bayes en un pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(phrases, categories)


# Aplicación FastAPI
app = FastAPI()

# Modelo de solicitud de mensaje
class MessageRequest(BaseModel):
    message: str

# Ruta para el chatbot
@app.post("/chat")
async def chat(request: MessageRequest):
    user_message = request.message
    predicted_category = model.predict([user_message])[0]
    
    # Respuestas predefinidas basadas en la categoría predicha
    responses = {
        "Saludo": "¡Hola! ¿En qué puedo ayudarte?",
        "Despedida": "¡Adiós! Que tengas un excelente día.",
        "Información de contacto": "Puedes contactarnos al 123-456-7890 o por email en contacto@ejemplo.com.",
        "Horario de atención": "Nuestro horario de atención es de lunes a viernes de 9:00 a 18:00.",
        "Precios": "Para más detalles sobre precios, visita nuestro sitio web o contacta a ventas.",
        "Política de devolución": "Ofrecemos devoluciones dentro de los 30 días con el recibo original.",
        "Soporte técnico": "Para asistencia técnica, visita nuestro centro de ayuda o llama al soporte.",
    }

    # Obtener la respuesta basada en la categoría predicha
    response_text = responses.get(predicted_category, "Lo siento, no entiendo tu pregunta. ¿Puedes reformularla?")
    return {"category": predicted_category, "response": response_text}

# Ruta de prueba para verificar que el servidor está activo
@app.get("/")
async def root():
    return {"message": "Chatbot activo y esperando mensajes"}
