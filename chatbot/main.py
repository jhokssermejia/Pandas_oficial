# Importa la clase principal para crear aplicaciones en FastAPI.
from fastapi import FastAPI

# Importa la clase base de Pydantic para la validación y estructuración de datos.
from pydantic import BaseModel

# Importa el vectorizador, una herramienta para convertir texto en representaciones numéricas basadas en la importancia de las palabras en un conjunto de documentos.
from sklearn.feature_extraction.text import TfidfVectorizer

# Importa el clasificador Naive Bayes, un modelo de aprendizaje supervisado útil para clasificar datos textuales.
from sklearn.naive_bayes import MultinomialNB

# Importa una función para crear modelos de aprendizaje (como Naive Bayes).
from sklearn.pipeline import make_pipeline

# Importa la clase `List` para especificar tipos de datos más complejos en las anotaciones de tipo.
from typing import List

# Importa NLTK para análisis de emociones/intenciones.
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Descargar los recursos necesarios de NLTK
nltk.download('vader_lexicon')

# Inicializar el analizador de sentimientos de NLTK
sia = SentimentIntensityAnalyzer()

# Datos y etiquetas de categorías
data = [
    {"categoria": "Saludo", "frase": "hola"},
    {"categoria": "Saludo", "frase": "¿cómo estás?"},
    {"categoria": "Saludo", "frase": "buenos días"},
    {"categoria": "Saludo", "frase": "buenas tardes"},
    {"categoria": "Saludo", "frase": "buenas noches"},
    {"categoria": "Saludo", "frase": "¡Qué gusto verte!"},
    {"categoria": "Saludo", "frase": "¡Hola a todos!"},
    {"categoria": "Saludo", "frase": "Un placer saludarte"},
    {"categoria": "Saludo", "frase": "¿Qué tal?"},
    {"categoria": "Saludo", "frase": "¡Saludos cordiales!"},

    {"categoria": "Despedida", "frase": "adiós"},
    {"categoria": "Despedida", "frase": "hasta luego"},
    {"categoria": "Despedida", "frase": "nos vemos"},
    {"categoria": "Despedida", "frase": "me despido"},
    {"categoria": "Despedida", "frase": "hasta pronto"},
    {"categoria": "Despedida", "frase": "cuídense mucho"},
    {"categoria": "Despedida", "frase": "que tengas un buen día"},
    {"categoria": "Despedida", "frase": "nos hablamos luego"},
    {"categoria": "Despedida", "frase": "hasta mañana"},

    {"categoria": "Información de contacto", "frase": "¿Cómo puedo contactarlos?"},
    {"categoria": "Información de contacto", "frase": "¿Cuál es el número de teléfono?"},
    {"categoria": "Información de contacto", "frase": "¿Tienen algún correo electrónico?"},
    {"categoria": "Información de contacto", "frase": "¿Dónde están ubicados?"},
    {"categoria": "Información de contacto", "frase": "¿Cómo puedo llegar a sus oficinas?"},
    {"categoria": "Información de contacto", "frase": "¿Cuál es su página web?"},
    {"categoria": "Información de contacto", "frase": "¿Puedo enviarles un mensaje por redes sociales?"},
    {"categoria": "Información de contacto", "frase": "¿Tienen algún número de WhatsApp?"},
    {"categoria": "Información de contacto", "frase": "¿Puedo agendar una llamada?"},

    {"categoria": "Horario de atención", "frase": "¿Cuál es el horario de atención?"},
    {"categoria": "Horario de atención", "frase": "¿En qué días están abiertos?"},
    {"categoria": "Horario de atención", "frase": "¿Están abiertos los fines de semana?"},
    {"categoria": "Horario de atención", "frase": "¿A qué hora abren?"},
    {"categoria": "Horario de atención", "frase": "¿A qué hora cierran?"},
    {"categoria": "Horario de atención", "frase": "¿Están abiertos en días festivos?"},
    {"categoria": "Horario de atención", "frase": "¿Tienen horario especial en vacaciones?"},
    {"categoria": "Horario de atención", "frase": "¿Cuándo es su próximo día no laborable?"},
    {"categoria": "Horario de atención", "frase": "¿Cuánto tiempo permanecen abiertos?"},

    {"categoria": "Precios", "frase": "¿Cuánto cuesta el producto?"},
    {"categoria": "Precios", "frase": "¿Cuál es el precio del servicio?"},
    {"categoria": "Precios", "frase": "¿Tienen algún descuento?"},
    {"categoria": "Precios", "frase": "¿Cuánto cuesta la suscripción mensual?"},
    {"categoria": "Precios", "frase": "¿Cuál es el costo de envío?"},
    {"categoria": "Precios", "frase": "¿Tienen precios promocionales?"},
    {"categoria": "Precios", "frase": "¿Puedo pagar a plazos?"},
    {"categoria": "Precios", "frase": "¿Cuál es el precio para grupos?"},
    {"categoria": "Precios", "frase": "¿Tienen precios diferentes para empresas?"},

    {"categoria": "Política de devolución", "frase": "¿Cuál es la política de devoluciones?"},
    {"categoria": "Política de devolución", "frase": "¿Puedo devolver el producto?"},
    {"categoria": "Política de devolución", "frase": "¿Cuánto tiempo tengo para hacer una devolución?"},
    {"categoria": "Política de devolución", "frase": "¿Necesito el recibo para una devolución?"},
    {"categoria": "Política de devolución", "frase": "¿Es posible cambiar un producto?"},
    {"categoria": "Política de devolución", "frase": "¿Aceptan devoluciones sin empaque original?"},
    {"categoria": "Política de devolución", "frase": "¿Tienen una política de reembolso?"},
    {"categoria": "Política de devolución", "frase": "¿Cuánto tiempo tardan en procesar una devolución?"},
    {"categoria": "Política de devolución", "frase": "¿Puedo cambiar un producto defectuoso?"},

    {"categoria": "Soporte técnico", "frase": "Tengo un problema técnico"},
    {"categoria": "Soporte técnico", "frase": "¿Cómo puedo solucionar un error?"},
    {"categoria": "Soporte técnico", "frase": "¿Tienen soporte técnico?"},
    {"categoria": "Soporte técnico", "frase": "Mi aplicación no funciona"},#
    {"categoria": "Soporte técnico", "frase": "¿Pueden ayudarme con un problema en mi cuenta?"},
    {"categoria": "Soporte técnico", "frase": "¿Cómo actualizo mi software?"},
    {"categoria": "Soporte técnico", "frase": "¿Qué hacer si mi dispositivo no responde?"},
    {"categoria": "Soporte técnico", "frase": "¿Dónde puedo reportar un bug?"},
    {"categoria": "Soporte técnico", "frase": "¿Tienen un chat de soporte?"},

    {"categoria": "Agradecimiento", "frase": "Muy buen servicio"},
    {"categoria": "Agradecimiento", "frase": "Todo perfecto, gracias"},#
    {"categoria": "Agradecimiento", "frase": "Excelente atención"},
    {"categoria": "Agradecimiento", "frase": "¡Muy satisfecho con el producto!"},
    {"categoria": "Agradecimiento", "frase": "Recomendaré su servicio"},
    {"categoria": "Agradecimiento", "frase": "Gracias por la rápida respuesta"},
    {"categoria": "Agradecimiento", "frase": "El equipo es muy amable"},
    {"categoria": "Agradecimiento", "frase": "Estoy muy feliz con mi compra"},
    {"categoria": "Agradecimiento", "frase": "Gracias por su dedicación"},
    {"categoria": "Agradecimiento", "frase": "Muy profesional todo el proceso"},

    {"categoria": "Sugerencia", "frase": "Sería genial tener más horarios disponibles"},
    {"categoria": "Sugerencia", "frase": "Podrían agregar más opciones de pago"},
    {"categoria": "Sugerencia", "frase": "Consideren mejorar los tiempos de respuesta"},
    {"categoria": "Sugerencia", "frase": "Un chat en línea sería muy útil"},
    {"categoria": "Sugerencia", "frase": "Añadan más productos a su catálogo"}
]


# Extraer las frases y las categorías para entrenamiento
frases = [item["frase"] for item in data]
categorias = [item["categoria"] for item in data]

# Crear y entrenar el clasificador Naive Bayes en un pipeline
vectorizer = TfidfVectorizer()
x_train = vectorizer.fit_transform(frases)
classifier = MultinomialNB()
classifier.fit(x_train, categorias)

# Aplicación FastAPI
app = FastAPI()

# Modelo de solicitud de mensaje
class MessageRequest(BaseModel):
    message: str

# Ruta para el chatbot
@app.post("/chat")
async def chat(request: MessageRequest):
    mensaje_usuario = request.message

    # Predicción de categoría
    x_test = vectorizer.transform([mensaje_usuario])
    predecir_categoria = classifier.predict(x_test)[0]

    # Análisis de sentimiento usando NLTK
    sentimiento = sia.polarity_scores(mensaje_usuario)

    # Determinar el tono basado en el puntaje de sentimiento
    if sentimiento['compound'] >= 0.2:
        tono = "muy positivo"
    elif 0.05 <= sentimiento['compound'] < 0.2:
        tono = "positivo"
    elif -0.05 < sentimiento['compound'] < 0.05:
        tono = "neutral"
    elif -0.2 < sentimiento['compound'] <= -0.05:
        tono = "negativo"
    else:
        tono = "muy negativo"

    # Respuestas predefinidas basadas en la categoría predicha
    respuestas = {
        "Saludo": "¡Hola! ¿En qué puedo ayudarte?",
        "Despedida": "¡Adiós! Que tengas un excelente día.",
        "Información de contacto": "Puedes contactarnos al 123-456-7890 o por email en contacto@ejemplo.com.",
        "Horario de atención": "Nuestro horario de atención es de lunes a viernes de 9:00 a 18:00.",
        "Precios": "Para más detalles sobre precios, visita nuestro sitio web o contacta a ventas.",
        "Política de devolución": "Ofrecemos devoluciones dentro de los 30 días con el recibo original.",
        "Soporte técnico": "Para asistencia técnica, visita nuestro centro de ayuda o llama al soporte.",
        "Agradecimiento": "Es un gusto atenderte, queremos que te sientas acompañado y satisfecho con nuestros servicios",
        "Sugerencia": "Gracias por tus comentarios, haremos lo posible por mejorar"
    }

    # Obtener la respuesta basada en la categoría predicha
    texto_respuesta = respuestas.get(predecir_categoria, "Lo siento, no entiendo tu pregunta. ¿Puedes reformularla?")

    return {
        "mensaje usuario": mensaje_usuario,
        "categoria": predecir_categoria,
        "respuesta": texto_respuesta,
        "sentimiento": tono        
    }

# Ruta de prueba para verificar que el servidor está activo
@app.get("/")
async def root():
    return {"message": "Chatbot activo y esperando mensajes"}

# Ruta para mostrar el vocabulario y las frecuencias
@app.get("/vocabulario")
async def vocabulario():
    vocab = vectorizer.vocabulary_
    idf = vectorizer.idf_
    vocabulario_frecuencias = {
        palabra: {
            "indice": vocab[palabra],
            "idf": idf[vocab[palabra]]
        }
        for palabra in vocab
    }
    return {
        "vocabulario": vocabulario_frecuencias
        
    }

