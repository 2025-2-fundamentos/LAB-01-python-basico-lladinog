"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from pprint import pprint


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    
    lines = []
    with open ("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
    
    columns = list(map(lambda line: line.split('\t'), lines))
    column5 = list(map(lambda column: column[4].replace("\n", ""), columns))
    dicts_in_columns = list(map(lambda column5: column5.split(','), column5))

    dicts = []
    for column in dicts_in_columns:
        for dict in column:
            dicts.append(dict)

    dicts = sorted(list(map(lambda x: x.split(':')[0], dicts)))

    result = {}
    
    for x in dicts:
        if x not in result:
            result[x] = 1
        else:
            result[x] += 1
    
    return result

pregunta_09()
