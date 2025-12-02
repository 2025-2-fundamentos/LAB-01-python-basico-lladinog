"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from pprint import pprint


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
   
    lines = []
    with open ("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
    
    columns = list(map(lambda line: line.split('\t'), lines))
    columns2_4 = list(map(lambda column: (column[3].split(','), int(column[1])), columns))
    
    sequence = []
    for tuple in columns2_4:
        for letter in tuple[0]:
            sequence.append((letter, tuple[1]))
    
    dict = {}
    for letter, value in sequence:
        if letter not in dict:
            dict[letter] = value
            continue
        dict[letter] += value

    return dict

pregunta_11()
