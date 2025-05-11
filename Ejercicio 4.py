import pandas as pd
import matplotlib.pyplot as plt

path_file = 'Data/Copy.csv'

df_movies = pd.read_csv(path_file)

df_genres_exploded = df_movies.assign(
  genre=df_movies['genre'].str.split(',')
).explode('genre')
df_genres_exploded['genre'] = df_genres_exploded['genre'].str.strip()

promedio = df_genres_exploded.groupby("genre")['audience_rating'].mean()

top_10 = promedio.sort_values(ascending =False).head(10)

plt.figure(figsize=(8, 8))
top_10.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.ylabel('')
plt.title('Top 10 peliculas con mayor promedio de valoración')
plt.show()