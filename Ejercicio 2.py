import pandas as pd
import matplotlib.pyplot as plt

# 8. ¿Cuántas películas hay en total? Mostrar en consola
# 10. ¿Cuántas películas fueron calificadas como "Certified Fresh", "Fresh" y "Rotten"? usa value counts sobre la columna tomatometer_status

path_file = 'Data/Rotten Tomatoes Movies.csv'
df_movies = pd.read_csv(path_file)

print(len(df_movies))
print(df_movies.shape)

df_categorias = df_movies['tomatometer_status'].value_counts()
print(df_categorias)

plt.figure(figsize = (10,10))
df_categorias.plot(kind = 'pie', autopct = '%1.1f%%', startangle = 140)
plt.title('Distribution of Tomatoes Status')
plt.ylabel('')
plt.show()