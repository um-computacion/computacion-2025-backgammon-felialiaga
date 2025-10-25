Prompt 1: al hacer un print de los elementos de un array me los muestra uno abajo del otro, como puedo hacer para que los muestre uno a lado del otro
Respuesta 1:
    arr = [1, 2, 3, 4, 5]

    for x in arr:
        print(x, end=" ")   # agrega espacio en vez de salto de línea

Respuesta 2:
    arr = ["uno", "dos", "tres"]
    print(" ".join(arr))  # uno dos tres



Prompt 2: Le pregunte a la IA como podia hacer para invertir una columna 
Respuesta:
    for i in top:
        faltan = max_len - len(i)
        if faltan > 0:
            i[:0] = ["|"] * faltan 


Prompt 3: Al trabajar con los modulos me daba error
Respuesta:
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))


Prompt 4: quiero hacer un acumulador, pero tengo 6 listas, donde en cada lista tengo 'x' o 'o', y me gustaria filtrar cada lista para sumar solo las 'x' o solo las 'o'
Respuesta: 🧠 .count('x') cuenta cuántas veces aparece 'x' en esa lista.

Prompt 5: Tengo una lista que tiene 6 listas adentro, yo lo que quiero es verificar que las listas detras de una cierta posicion esten vacias. 
Respuesta:
    posicion = 2
    vacias = all(len(lista) == 0 for lista in listas[posicion:])
    print(vacias)