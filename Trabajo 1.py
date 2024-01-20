
# Trabajo en casa 1

#variable de texto
Estudiante = "Karen"
print(Estudiante)

#lista de números pares del 2 al 20
num_pares = [2,4,6,8,10,12,14,16,18,20]
print(num_pares)

#diccionario (dar etiquetas a valores)
mes_cumpleaños = {"nombre_1" : "mes1", "nombre_2" : "mes2", "nombre_3" : "mes3"}
print(mes_cumpleaños)

#######################################################

#NUMÉRICA

vector_enteros= [1]*3
print(vector_enteros)

vector_flotantes = [19.02]*2
print(vector_flotantes)

diccionario_numeros = {"Enteros" : vector_enteros, "flotante" : vector_flotantes}
print(diccionario_numeros)

#CADENAS

cadena_simple = 'Economía!'
cadena_doble = ["Entre ser y no ser", "yo soy xD"]
print(cadena_doble)

#######################################################

#DataFrame (la columna empieza desde el cero)

import pandas as pd

# Crear un DataFrame con la altura y peso de 5 personas
información = {
    'Nombre': ['Milagros', 'Anthony', 'Erick', 'Ambar', 'Paulina'],
    'Altura (cm)': [150, 180, 170, 165, 165],
    'Peso (kg)': [57, 60, 75, 65, 63],
}

df = pd.DataFrame(información)

# Mostrar el DataFrame
print(df)

#lectura de una tabla Excel usando pandas
import pandas as pd
imp_sri = pd.read_excel("ventas_SRI (1).xlsx")
print(imp_sri)
