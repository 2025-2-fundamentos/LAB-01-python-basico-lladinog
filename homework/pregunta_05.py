"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    lines = []
    with open ("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
    
    columns = list(map(lambda line: line.split('\t'), lines))
    columns1_2 = sorted(list(map(lambda column: (column[0], int(column[1])), columns)))

    result = []
    for key, value in columns1_2:
        if result and result[-1][0] == key:
            if value > result[-1][1]:
                result[-1] = (key, value, result[-1][2])
            elif value < result[-1][2]:
                result[-1] = (key, result[-1][1], value)
        else:
            result.append((key, value, value))
    
    return result

pregunta_05()
