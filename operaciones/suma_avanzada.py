
def numbers():
    numbers_array = []
    while True:
    
        quest_number = int(input("Dame tu número: "))
        numbers_array.append(quest_number)
        process_number = input("Quieres otro número? yes/no:  ").strip().lower()
        if process_number !=  "yes":
            return numbers_array


def suma_avanzada(numbers):
    return sum(numbers)