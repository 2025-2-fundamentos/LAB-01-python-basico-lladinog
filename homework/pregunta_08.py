"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from pprint import pprint


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    lines = []
    with open ("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
    
    columns = list(map(lambda line: line.split('\t'), lines))
    column1_2 = list(map(lambda column: (column[0], int(column[1])), columns))
    column1_2.sort(key = lambda x: x[1])
    
    resultado = []
    for letra, valor in column1_2:
        if resultado and resultado[-1][0] == valor :
            resultado[-1][1].append(letra)
        else:
            resultado.append((valor, list(letra) ))
    
    resultado_sin_repes = list(map(lambda x: (x[0], sorted(list(set(x[1])))), resultado))

    return resultado_sin_repes

pregunta_08()
