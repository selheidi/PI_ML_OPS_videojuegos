<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 09:27:45 2023

@author: Heidi
"""


import pandas as pd
from fastapi import FastAPI
import uvicorn 

app = FastAPI()

play_genre = pd.read_csv('Funcion_1.csv', low_memory=False)
user_for_genre = pd.read_csv('Funcion_2_jup.csv', low_memory=False)

@app.get("/release_year/{genre}", name='Año con mas horas jugadas para el género ingresado')

def PlayTimeGenre(genre: str):
   
    genero_df = play_genre[play_genre['genre'] == genre]

    if genero_df.empty:
        return {"No se encontraron datos para el género": genre}

    
    max_year = genero_df.loc[genero_df['playtime_forever'].idxmax()]['release_year']

    return {"Año de lanzamiento con más horas jugadas para " + genre: int(max_year)}


@app.get("/user_for_genre/{genre}", name='a usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.')

def UserForGenre(genero: str):

    genre_data = user_for_genre[user_for_genre['genre'] == genero]

    if genre_data.empty:
        return {"Usuario con más minutos jugados para " + genero: None, "minutos jugados": []}

    grouped = genre_data.groupby(genre_data['posted'])['playtime_forever'].sum().reset_index()

    max_playtime_user = genre_data.loc[genre_data['playtime_forever'].idxmax()]['user_id']

    return {
        "Usuario con más horas jugadas para " + genero: max_playtime_user,
        "Horas jugadas": [{"Año": year, "minutos": hours} for year, hours in zip(grouped['posted'], grouped['playtime_forever'])]
    }

    
=======
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 09:27:45 2023

@author: Heidi
"""


import pandas as pd
from fastapi import FastAPI
import uvicorn 

app = FastAPI()

play_genre = pd.read_csv('Funcion_1.csv', low_memory=False)
user_for_genre = pd.read_csv('Funcion_2_jup.csv', low_memory=False)

@app.get("/release_year/{genre}", name='año con mas horas jugadas para el género ingresado')

def PlayTimeGenre(genre: str):
   
    genero_df = play_genre[play_genre['genre'] == genre]

    if genero_df.empty:
        return {"No se encontraron datos para el género": genre}

    
    max_year = genero_df.loc[genero_df['playtime_forever'].idxmax()]['release_year']

    return {"Año de lanzamiento con más horas jugadas para " + genre: int(max_year)}


@app.get("/user_for_genre/{genre}", name='a usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.')

def UserForGenre(genero: str):

    genre_data = user_for_genre[user_for_genre['genre'] == genero]

    if genre_data.empty:
        return {"Usuario con más minutos jugados para " + genero: None, "minutos jugados": []}

    grouped = genre_data.groupby(genre_data['posted'])['playtime_forever'].sum().reset_index()

    max_playtime_user = genre_data.loc[genre_data['playtime_forever'].idxmax()]['user_id']

    return {
        "Usuario con más horas jugadas para " + genero: max_playtime_user,
        "Horas jugadas": [{"Año": year, "minutos": hours} for year, hours in zip(grouped['posted'], grouped['playtime_forever'])]
    }

    
>>>>>>> 3d5a899b6b3505dc76ba4fa687287f8f8aafce81
