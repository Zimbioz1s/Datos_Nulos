#Importamos librerías requeridas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Carga desde un archivo .xlsx sin indice
df=pd.read_csv("Ventas_totales.csv")
df.head()

#  Para salon ventas con 6 valores nulos decidí que lo mejor era rellenar esos valores nulos con el promedio de los otros valores de la columna. Esto debido a que son ventas y para mantener un promedio de lo que generalmente se vende en salon ventas 
df['salon_ventas'] = df['salon_ventas'].fillna(round(df['salon_ventas'].mean(),1))


df['tarjetas_debito'] = df['tarjetas_debito'].fillna(round(df['tarjetas_debito'].median(),1)) #Para tarjetas de debito con 1 valor nulo decidí rellenar con la mediana de los valores de la columna


df['tarjetas_credito'] = df['tarjetas_credito'].fillna(round(df['tarjetas_credito'].median(),1)) #Para tarjetas de credito con 1 valor nulo decidí rellenar con la mediana de los valores de la columna


df['otros_medios']=df['otros_medios'].fillna(6922148.759) #Para otros medios con 1 valor nulo decidí rellenar con el promedio de los otros valores de la columna. Esto debido a que son ventas y para mantener un promedio de lo que generalmente se vende en otros medios

df['subtotal_ventas_alimentos_bebidas'] =df['subtotal_ventas_alimentos_bebidas'].fillna(method='ffill') #Para subtotal ventas alimentos bebidas con 1 valor nulo decidí rellenar con el valor anterior de la columna

df['bebidas'] =df['bebidas'].fillna(round(df['bebidas'].median(),1)) # Para bebidas con 1 valor nulo decidí rellenar con la mediana de los valores de la columna

df['almacen'] =df['almacen'].fillna(method='bfill') # Para almacen con 1 valor nulo decidí rellenar con el valor siguiente de la columna

df['panaderia'] =df['panaderia'].fillna(0) # Para panaderia con 1 valor nulo decidí rellenar con 0 ya que no se vendió nada en ese día

df['lacteos'] =df['lacteos'].fillna(0) # Para lacteos con 1 valor nulo decidí rellenar con 0 ya que no se vendió nada en ese día

df['carnes'] =df['carnes'].fillna(round(df['carnes'].median(),1)) # Para carnes con 1 valor nulo decidí rellenar con la mediana de los valores de la columna

df['verduleria_fruteria'] =df['verduleria_fruteria'].fillna(method='bfill') # Para verduleria fruteria con 1 valor nulo decidí rellenar con el valor siguiente de la columna 

df['alimentos_preparados_rotiseria'] =df['alimentos_preparados_rotiseria'].fillna(method='ffill') # Para alimentos preparados rotiseria con 1 valor nulo decidí rellenar con el valor anterior de la columna

df['indumentaria_calzado_textiles_hogar'] =df['indumentaria_calzado_textiles_hogar'].fillna(round(df['indumentaria_calzado_textiles_hogar'].mean(),1)) # Para indumentaria calzado textiles hogar con 1 valor nulo decidí rellenar con el promedio de los otros valores de la columna

df['electronicos_articulos_hogar'] =df['electronicos_articulos_hogar'].fillna(round(df['electronicos_articulos_hogar'].median(),1)) # Para electronicos articulos hogar con 1 valor nulo decidí rellenar con la mediana de los valores de la columna

df['otros'] =df['otros'].fillna(round(df['otros'].mean(),1)) # Para otros con 1 valor nulo decidí rellenar con el promedio de los otros valores de la columna

#Convertir DataFrame a CSV
df.to_csv('Ventas_totales_limpio.csv')