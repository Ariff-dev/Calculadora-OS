from colorama import Fore
from operaciones.sumar import sumar
from operaciones.resta import resta
from operaciones.multiplicacion import multiplicacion
from operaciones.dividir import dividir
from operaciones.suma_avanzada import suma_avanzada, numbers  # Asegúrate de usar el nombre correcto de la función

def questionValues():
    """Solicita dos números al usuario y los devuelve como una tupla."""
    number = int(input("Tu número 1:  "))
    number2 = int(input("Tu número 2:  "))
    return number, number2

while True:
    print(Fore.RED + "------------------------------------------------------------------------")
    print(Fore.RED + "-------------Bienvenido a la calculadora --------------")
    print(Fore.RED + "------------------------------------------------------------------------")

    print(Fore.GREEN + "¿Qué deseas hacer?")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma avanzada")
    print("6. Salir")


    try:
        option = int(input(Fore.CYAN + "Escribe el número de tu opción: "))
    except ValueError:
        print(Fore.YELLOW + "Por favor, ingresa un número válido.")
        continue

    if option > 5 or option < 1:
        print(Fore.YELLOW + "El número no está en las opciones")
        continue
    
    if option != 5:
        number, number2 = questionValues()
    else:
        # Para la opción 5, no se solicitan números aquí, se usan los números de collect_numbers
        numbers = numbers()

    if option == 1:
        res = sumar(number, number2)
        print(Fore.GREEN + f"Resultado: {res}")
    elif option == 2:
        res = resta(number, number2)
        print(Fore.GREEN + f"Resultado: {res}")
    elif option == 3:
        res = multiplicacion(number, number2)
        print(Fore.GREEN + f"Resultado: {res}")
    elif option == 4:
        try:
            res = dividir(number, number2)
            print(Fore.GREEN + f"Resultado: {res}")
        except ValueError as e:
            print(Fore.RED + str(e))
    elif option == 5:
        res = suma_avanzada(numbers)
        print(Fore.GREEN + f"Resultado: {res}")
    elif option == 6:
        break

    process = input("¿Continuar usando? yes/no: ").strip().lower()
    if process != 'yes':
        break
