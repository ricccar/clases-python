# Crear un contador de errores en un servidor
# Nos va a llegar una lista tal que así:
"""
logs = ["ERROR", "INFO", "WARNING", "ERROR", "ERROR", "INFO"]
 
tenemos que contabilizar cuantos errores de cada tipo hemos tenido
 
(pista, lo idea es guardar esto en un diccionario!)
"""
logs = ["ERROR", "INFO", "WARNING", "ERROR", "ERROR", "INFO"]
# saber el número de elementos y listarlos.
# lista_aux = list(range(len(logs)))
# print(lista_aux)

# crear el diccionario con las dos listas
# errores = dict(zip(lista_aux, logs))
# print(errores)

error_buscado = input(
    "Introduce el tipo de error buscado de esta lista, ERROR, INFO, WARNING: \n")

numero_errores_tipo = logs.count(error_buscado)
print(
    f'El número de errores del tipo {error_buscado} es {numero_errores_tipo}')



