print("------Ejercicio 3 Clase 2------")

password = "contraseña".lower()

usuario = input("\nPor favor ingrese la contraseña: ")

if usuario == password.lower():
    print("\nLa contraseña introducida es igual a la almacenada.")
else:
    print("\nLa contraseña introducida no es igual a la almacenada.")