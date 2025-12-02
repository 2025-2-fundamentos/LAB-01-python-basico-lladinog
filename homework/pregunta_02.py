"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    lines = []
    with open ("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
    
    columns = list(map(lambda line: line.split('\t'), lines))
    column1 = list(map(lambda x: x[0], columns))
    column1_sorted = sorted(column1)
    
    result = []
    for x in column1_sorted:
        if result and result[-1][0] == x:
            result[-1] = (x, result[-1][1] + 1) 
        else:
            result.append((x, 1))
    
    return result

pregunta_02()
