import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('./data/airbnb.csv', sep=',')

# Mostrar las primeras dos filas del DataFrame
print(df.head(13233))