"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from pprint import pprint


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    lines = []
    with open ("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
    
    columns = list(map(lambda line: line.split('\t'), lines))
    columns1_5 = list(map(lambda column: (column[0], list(map(lambda x: int(x.split(':')[1]) ,column[4].replace("\n", "").split(',')))), columns))
    sorted_columns = sorted(columns1_5)
    
    dict = {}
    for key, value in sorted_columns:
        for x in value:
            if key not in dict:
                dict[key] = x
            else:
                dict[key] += x
    
    return dict

pregunta_12()
