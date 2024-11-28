from fastapi import FastAPI, Body
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
        "year": "1986",
        "rating": 9.5,
        "category": "Anime",# Se agrega la categoria
        "creator": "Akira Toriyama" #Se agrega el autor de la serie
    },
    {
        "id": 2,
        "title": "Dragon Ball Z",
        "overview": "Goku crece y pelea contra su hermano Raditz y luego viaja al planeta Namek a pelear contra Freezer",
        "year": "1989", #Año de creacion de la serie
        "rating": 9.0,
        "category": "Anime",# Se agrega la categoria
        "creator": "Akira Toriyama" #Se agrega el autor de la serie
    }
]

@app.get('/', tags = ['Home'] ) #Definimos una ruta

def message(): #Definimos una funcion de la ruta
    return HTMLResponse('<h1>Hello World<h1>')#Devolmemos un string en la respuesta de la ruta

@app.get ( '/movies', tags=["Movies"]) #definimos una ruta de la clase FastAPI
def get_movies(): #aqui puse get_movies y estaba solo movies
    return movies_list


@app.get('/movies/{id}' , tags=["Movies"]) #anadimos el primer parametro de ruta
def get_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            return item

    return []

@app . get ( '/movies/', tags=["Movies"])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies_lis if item ['category'] == category]


@app.post('/movies', tags=[ 'Movies'])
def create_movie(id: int =Body(), title: str =Body(), overview: str =Body(), year: int =Body(), rating: float =Body(), category: str =Body()):
    movies_list.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies_list

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, title: str =Body(), overview: str =Body(), year: int =Body(), rating: float =Body(), category: str =Body()):
    for item in movies_list:
        if item["id"] == id:
            item['title'] = title,
            item['overview' ] = overview,
            item['year'] = year,
            item['rating'] = rating,
            item['category'] = category,
            return movies_list


@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            movies_list.remove(item)
            return movies_list