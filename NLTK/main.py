
#PRIMER EJERCICIO DE TOKENIZACIÓN
'''from nltk.tokenize import word_tokenize


sentence = "NLTK es una biblioteca de procesamiento de lenguaje natural."
tokens = word_tokenize(sentence)
print(tokens)'''


#SEGUNDO EJERCICIO DE DERIVACIÓN
'''from nltk.stem import PorterStemmer

words = ["running", "plays", "jumped"]
stemmer = PorterStemmer()
stems = [stemmer.stem(word) for word in words]
print(stems)'''

#TERCER EJERCICIO DE ETIQUETADO
'''from nltk import pos_tag
from nltk.tokenize import word_tokenize

sentence = "NLTK es una biblioteca de procesamiento de lenguaje natural."
tokens = word_tokenize(sentence)
tagged_words = pos_tag(tokens)
print(tagged_words)'''

#CUARTO EJERCICIO
'''import nltk
import random

# Ejemplo de conjunto de datos de textos etiquetados
data = [
    ("I love this movie", "positive"),
    ("This movie is terrible", "negative"),
    ("This movie is great", "positive"),
    ("I dislike this movie", "negative"),
    ("This film is amazing", "positive"),
    ("I can't stand watching this movie", "negative"),
    ("The acting in this movie is phenomenal", "positive"),
    ("I regret wasting my time on this film", "negative"),
    ("I thoroughly enjoyed this movie", "positive"),
    ("This movie lacks depth and substance", "negative"),
    ("The plot of this movie was captivating", "positive"),
    ("I found the characters in this film to be very engaging", "positive"),
    ("The special effects in this movie were impressive", "positive"),
    ("The storyline was predictable and unoriginal", "negative"),
    ("I was disappointed by the lack of character development", "negative"),
    ("The cinematography in this film was stunning", "positive"),
    ("The dialogue felt forced and unnatural", "negative"),
    ("The pacing of the movie was too slow for my liking", "negative"),
    ("I was pleasantly surprised by how much I enjoyed this film", "positive"),
    ("The ending left me feeling unsatisfied and confused", "negative"),
    ("This movie exceeded my expectations", "positive"),
    ("The performances by the actors were lackluster", "negative")

]

# Preprocesamiento de datos: tokenización y extracción de características
def preprocess(text):
    tokens = nltk.word_tokenize(text)
    return {word: True for word in tokens}

#Aplicamos el preprocesamiento a los datos
featuresets = [(preprocess(text), label) for (text, label) in data]

#Dividimos los datos en conjunto de entrenamiento y prueba
train_set, test_set = featuresets[:16], featuresets[16:]

classifier = nltk.NaiveBayesClassifier.train(train_set)

# Evaluamos el clasificador en el conjunto de prueba
accuracy = nltk. classify. accuracy(classifier, test_set)
print("Accuracy:", accuracy)

# Clasificamos un nuevo texto
new_text = "This movie is amazing"
new_text_features = preprocess(new_text)
predicted_label = classifier.classify(new_text_features)
print("Predicted label:", predicted_label)'''

#EJERCICIO 5
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag, word_tokenize

# Inicializar el lematizador
lemmatizer = WordNetLemmatizer()

# Función para obtener la etiqueta de parte de discurso adecuada
def get_wordnet_pos(word):
    tag = pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

# Texto de ejemplo
text = "The striped bats are hanging on their feet for best"

# Tokenizar el texto
tokens = word_tokenize(text)

# Aplicar lematización a cada palabra con su etiqueta de POS
lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in tokens]

# Mostrar el resultado
print("Texto original:", text)
print("Texto lematizado:", " ".join(lemmatized_words))
