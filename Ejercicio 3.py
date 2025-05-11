# 11. Promedio de valoración del tomatómetro y la audiencia o publico
# print(f"Promedio de valoración por críticos: {promedio_criticos:.2f}")
# print(f"Promedio de valoración por audiencia: {promedio_audiencia:.2f}")

# 12. Para cada película, calcular la diferencia entre audiencia y críticos
# 13. Histograma de las diferencias de valoración

import pandas as pd
import matplotlib.pyplot as plt

path_file = 'Data/Rotten Tomatoes Movies.csv'
df_movies = pd.read_csv(path_file)

tomato_rating = df_movies['tomatometer_rating'].mean()
audience_rating = df_movies['audience_rating'].mean()
print(f"Promedio de valoración por críticos: {tomato_rating:.2f}")
print(f"Promedio de valoración por audiencia: {audience_rating:.2f}")

df_movies['rating_diff'] = df_movies['audience_rating'] - df_movies['tomatometer_rating']

plt.figure(figsize=(8,10))
plt.hist(df_movies['rating_diff'], bins=30, edgecolor='black', color='seagreen')
plt.title("Distribucion, diferencia entre audiencia y criticos")
plt.xlabel('Diferencia (audiencia - criticos)')
plt.ylabel('Numero de peliculas')
plt.axvline(x=0, color='r', linestyle='--', linewidth=2)
plt.show()