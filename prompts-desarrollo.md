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