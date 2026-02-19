def string_formated(a):
    if len(a) < 2:
        return a # Retorna igual si tiene 0 o 1 caracteres
    else:
        return a[0].upper() + a[1:].lower()

entrance = input("write something: ")

print(string_formated(entrance))