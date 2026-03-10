def name_day(number):

    """write a program that returns the name day."""

    match number:
        case 1: return "Lunes"
        case 2: return "Martes"
        case 3: return "Miercoles"
        case 4: return "Jueves"
        case 5: return "Viernes"
        case 6: return "Sabado"
        case 7: return "Domingo"
        case _: return "No se puede definir el día"

try:
    userNumber=int(input("Enter your number: "))
    print(name_day(userNumber))
    
except ValueError:
    print("Error: this is not a number")
