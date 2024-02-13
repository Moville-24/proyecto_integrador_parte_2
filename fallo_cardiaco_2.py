from datasets import load_dataset
import numpy as np
import pandas as pd

# Cargamos el dataset dado en plataforma
dataset = load_dataset("mstz/heart_failure")

# accedemos a todos los registos indexando por esa partición train
data = dataset["train"]

# Convertir la estructura Dataset en un DataFrame  
df = pd.DataFrame(data)

# Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron (is_dead=1) y otro con el complemento. 
df_fallecidos =  df[df['is_dead'] == 1] # Filtramos solo aquellos que murieron (columna is_dead= 1)
df_sobrevivientes = df[df['is_dead'] == 0]# Filtramos solo aquellos que sobrevivieron

# Calcular los promedios de las edades de cada dataset e imprimir
promedio_edad_fallecidos = df_fallecidos['age'].mean()
promedio_edad_sobrevivientes = df_sobrevivientes['age'].mean()

# Como siempre convertir tipo de valores float los pasamos a enteros si necesitamos el resultado de está forma
promedio_edad_fallecidos_redondeado = round(promedio_edad_fallecidos)
promedio_edad_sobrevivientes_redondeado = round(promedio_edad_sobrevivientes)

# Se imrpimen los valores de promedio de edad
print(f"\nEl promedio de edad de fallecidos son: {promedio_edad_fallecidos_redondeado} personas\n")
print(f"El promedio de edad que sobrevivieron fueron : {promedio_edad_sobrevivientes_redondeado} personas")
