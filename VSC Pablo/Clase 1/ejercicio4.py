print ("------Ejercicio 4 Clase 1------")

def calcular_nota (materias,notas):
    promedio =  sum(notas) / len(notas)

# Encontrar la materia con la nota mas baja

    nota_baja = notas[0]
    materia_baja = materias[0]

    for i in range(1, len(notas)):
        if notas[i] < nota_baja:
            nota_baja = notas[i]
            materia_baja = materias[i]
        
    return promedio, materia_baja, nota_baja

materias = [""] * 4
notas = [0] * 4

for i in range(4):
    materias[i] = input(f"Ingrese el nombre de la materia {i + 1}: ")
    notas[i] = float(input(f"Ingrese la nota de {materias[i]}: "))

promedio, materia_baja, nota_baja = calcular_nota(materias,notas)

print(f"El promedio de las notas es: {promedio}")
print(f"La {materia_baja} es la con la nota más baja {nota_baja}")