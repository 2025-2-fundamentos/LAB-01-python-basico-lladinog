"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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

    dicts_sorted = sorted(dicts)
    pairs = list(map(lambda dict: dict.split(':'), dicts_sorted))
    pairs = list(map(lambda dict: (dict[0], int(dict[1])), pairs))

    result = []
    for key, value in pairs:
        if result and result[-1][0] == key:
            if value < result[-1][1]:
                result[-1] = (key, value, result[-1][2])
            elif value > result[-1][2]:
                result[-1] = (key, result[-1][1], value)
        else:
            result.append((key, value, value))

    return result

pregunta_06()
