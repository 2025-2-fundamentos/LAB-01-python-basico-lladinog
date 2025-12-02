"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    lines = []
    with open ("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
        
    columns = list(map(lambda line: line.split('\t'), lines))
    columna2 = list(map(lambda column: column[1], columns))
    columna2_int = list(map(lambda x: int(x), columna2))
    return sum(columna2_int)
        
pregunta_01()
