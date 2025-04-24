import pandas as pd
import matplotlib.pyplot as plt

# 1. Importar las librerías necesarias
# 2. Leer el archivo CSV
# 3. Mostrar las primeras filas del DataFrame para revisar su contenido
# 4. Verificar los nombres de las columnas
# 5. Convertir la columna 'in_theaters_date' al tipo datetime
# 6. Verificar que la conversión fue exitosa (dtypes)

# 7. Mostrar si hubo valores no convertidos (NaT)

path_file = "Data/Rotten Tomatoes Movies.csv"
data = pd.read_csv(path_file)

print(data.head(5))
print(data.dtypes)
data["in_theaters_date"] = pd.to_datetime(data["in_theaters_date"], errors="coerce")
print(data.info())

missing_dates = data['in_theaters_date'].isna().sum()
print(f"\nPelículas con fechas no reconocidas: {missing_dates}")