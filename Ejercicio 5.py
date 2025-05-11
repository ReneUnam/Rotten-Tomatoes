import pandas as pd
import matplotlib.pyplot as plt


df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")

director_counts = df_movies['directors'].value_counts()

# Obtener los 10 directores más frecuentes
top_10_directors = director_counts.head(10)
top_10_names = top_10_directors.index.tolist()

# Filtrar solo películas de esos 10 directores
df_top_10 = df_movies[df_movies['directors'].isin(top_10_names)]

# Calcular promedio de tomatometer_rating por director
director_avg_rating = df_top_10.groupby('directors')['tomatometer_rating'].mean()

# Ordenar y seleccionar los 10 mejpres en promedio
top_5_avg_rating = director_avg_rating.sort_values(ascending=False).head(10)

# Graficar
plt.figure(figsize=(8, 6))
top_5_avg_rating.plot(kind='bar', color='skyblue')
plt.title('Calificacion promedio (tomatometer) de los 10 directores mas frecuentes')
plt.xlabel('Director')
plt.ylabel('Tomatometer Rating Promedio')
plt.grid(axis ='y', linestyle = '--', alpha = 0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()