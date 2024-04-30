import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

from .Api.serializers import JuegosSerializer


from .models import Juegos


class Recomendacion:
    def __init__(self):
        self.df_juegos = pd.read_csv(r"core\Juegos\data\juegos_genpla.csv")
        self.tfidf = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.tfidf.fit_transform(
            self.df_juegos["Plataformas"] + " " + self.df_juegos["Géneros"]
        )
        self.model = NearestNeighbors(metric="cosine", algorithm="brute")
        self.model.fit(self.tfidf_matrix)

    def get_recommendations(self, title: str):
        model = self.model
        idx = self.df_juegos[self.df_juegos["Titulo"] == title].index[0]
        distances, indices = model.kneighbors(self.tfidf_matrix[idx], n_neighbors=21)
        rec_indices = indices.flatten()
        title_idx_in_rec = np.where(rec_indices == idx)[0]
        rec_indices = np.delete(rec_indices, title_idx_in_rec)
        rec_titles = self.df_juegos.iloc[rec_indices]["Titulo"]
        rec_titles = rec_titles.drop_duplicates()
        return rec_titles[:10].to_dict()

    # Retornar el serializable de cada juegos recomendado
    def get_recommendations_serializable(self, title: str):
        recomendaciones = self.get_recommendations(title)
        juegos_json = []
        print(recomendaciones)
        for index, juego in recomendaciones.items():
            juego_obj = Juegos.objects.get(id=index)
            juego_serializer = JuegosSerializer(juego_obj)
            juegos_json.append(juego_serializer.data)
        return juegos_json


class JuegoGeneroPlataforma:
    def __init__(self):
        self.Juegos = Juegos.objects.all()

    def create_dataframe(self):
        data = {
            "Id": [],  # "Id": "Id", # "Id": "Id",
            "Titulo": [],
            "Plataformas": [],
            "Géneros": [],
        }
        for juego in self.Juegos:
            data["Id"].append(juego.id)
            data["Titulo"].append(juego.titulo)
            data["Plataformas"].append(
                ", ".join([plataforma.nombre for plataforma in juego.plataformas.all()])
            )
            data["Géneros"].append(
                ", ".join([genero.nombre for genero in juego.generos.all()])
            )
        juegos_genpla_df = pd.DataFrame(data)
        juegos_genpla_df.to_csv(r"core\Juegos\data\juegos_genpla.csv", index=False)

        return juegos_genpla_df
