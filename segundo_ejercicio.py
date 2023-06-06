import tkinter as tk

"""
    Se tiene un arreglo myArray que contiene bloques de números. Los bloques pueden ser de
    cualquier largo, los números contenidos están en el rango de 1 a 9 y se separan por un cero
    para definir los bloques. Se deben ordenar los números de los bloques individualmente de
    menor a mayor e imprimir las secuencias separando los bloques por un espacio. Por ejemplo,
    para el arreglo: (1,3,2,0,7,8,1,3,0,6,7,1) la respuesta esperada es:
    123 1378 167
    El arreglo y su longitud están definidos en la sección de código predefinido. Asumir que este
    código predefinido puede variar (valores y longitud del arreglo) y se debe tener en cuenta lo
    siguiente al programar:
    - El número de bloques es variable.
    - Un cero marca el final de un bloque y el inicio de otro. El inicio del arreglo se asume como el
    inicio de un bloque y el final de un arreglo se asume como el final de un bloque (Por lo tanto un
    cero al inicio o al final del arreglo de hecho implicarían un bloque sin elementos)
    - Un bloque puede no contener elementos, en cuyo caso se imprimirá una x. Por ejemplo, para
    (2,1,0,0,3,4) se imprimiría.
    12 X 34
"""


def ordenar_bloques(myArray):
    bloques = []
    bloque_actual = []

    for num in myArray:
        if num == 0:
            if bloque_actual:
                bloques.append(sorted(bloque_actual))
                bloque_actual = []
            else:
                bloques.append("X")
        else:
            bloque_actual.append(num)

    if bloque_actual:
        bloques.append(sorted(bloque_actual))

    resultado = " ".join(["".join(map(str, bloque)) if bloque != "X" else "X" for bloque in bloques])
    return resultado


def ordenar_bloques_interfaz():
    entrada = entrada_texto.get()
    entrada = entrada.replace("[", "").replace("]", "")
    myArray = [int(num) for num in entrada.split(",")]
    resultado = ordenar_bloques(myArray)
    resultado_texto.config(text=resultado)


ventana = tk.Tk()
ventana.title("Ordenar Bloques")
ventana.geometry("600x200")

entrada_etiqueta = tk.Label(
    ventana,
    text=(
        "Ingrese el arreglo (separe los números por comas y con llaves, ejemplo [1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1]):"
    ),
)
entrada_etiqueta.pack(side="top")

entrada_texto = tk.Entry(ventana)
entrada_texto.pack(pady=10)

boton_resultado = tk.Button(ventana, text="Resultado", command=ordenar_bloques_interfaz)
boton_resultado.pack(pady=10)

resultado_texto = tk.Label(ventana, text="")
resultado_texto.pack(side="bottom")

ventana.mainloop()

# # Ejemplo de uso 1
# myArray = [1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1]
# resultado = ordenar_bloques(myArray)
# print(resultado)

# # Ejemplo de uso 2
# myArray = [2, 1, 0, 0, 3, 4]
# resultado = ordenar_bloques(myArray)
# print(resultado)
