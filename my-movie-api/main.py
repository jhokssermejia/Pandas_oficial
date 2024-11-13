from fastapi import FastAPI #importa la clase FastAPI de la libreria fastapi
from fastapi.responses import HTMLResponse

app = FastAPI() #crea una instancia de la clase FastAPI
app.title = 'Peliculas y Programas de Anime' #Agrega el titulo
app.version = '0.0.1'

movies_list = [
    {
        "id": 1,
        "title": "Dragon Ball",
        "overview": "Goku conoce a Bulma y van en busca de las esferas del Dragon para cumplir sus deseos",
        "year": "1985",
        "rating": 9.5
    },
    {
        "id": 2,
        "title": "Dragon Ball Z",
        "overview": "Goku crece y pelea contra su hermano Raditz y luego viaja al planeta Namek a pelear contra Freezer",
        "year": "1990",
        "rating": 9.0
    }
]

@app.get('/', tags = ['Home'] ) #Definimos una ruta

def message(): #Definimos una funcion de la ruta
    return HTMLResponse('<h1>Hello World<h1>')#Devolmemos un string en la respuesta de la ruta

@app. get ( '/movies', tags=["Movies"]) #definimos una ruta de la clase FastAPI
def get_movies(): #aqui puse get_movies y estaba solo movies
    return movies_list


@app.get('/movies/{id}' , tags=["Movies"])
def get_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            return item

    return []