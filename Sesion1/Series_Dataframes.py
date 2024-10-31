#Importamos la librería pandas y la llamamos pd
import pandas as pd 

#Creamos una serie de pandas como lista con etiquetas
#Los valores son nombres de jugadores del PSG
#El índice especifica el número de camisetas de esos jugadores

psg_players = pd.Series(
    ['Navas',
     'Mbappe', 
     'Neymar', 
     'Messi'] #Lista de jugadores
#    index = [1,7,10,15]
)

#creamos diccionario con los números de camisitas con los nombres de los jugadores

psg_dict = {
    1: 'Navas', 
    7: 'Mbappe', 
    10: 'Neymar', 
    15: 'Messi'
}

#Creamos la serie de pandas usando el diccionario
psg_players_dict = pd.Series(psg_dict)

#Imprimimos la serie
print(psg_players_dict)

#Imprimimos la pocision de la serie creada en su yave (7)
print(psg_players_dict[7])

#para imprimir valores de una pocisión a otra:
print(psg_players_dict[0:3])

#Diccionario con datos de jugadores
dict = {
    'Jugador':  ['Navas', 'Mbappe', 'Neymar', 'Messi'],
    'Altura': [183.0, 170.0, 170.0, 165.0],
    'Goles': [2, 200, 150, 200]
}

df = pd.DataFrame(dict, index = [1, 7, 10, 15])

print(df)
