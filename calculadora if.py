
try:
    print("En caso de querer calcular porcentajes, ingresa primero el numero y luego el porcentaje que quieres calcular.")
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese un segundo numero (O porcentaje): "))
    
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Porcentaje")
    print("6. Salir")
    
    operacion = int(input("Ingrese la opcion que desee: "))

    if operacion == 1:
        resultado = numero1 + numero2
        print(f"El resultado es: {resultado}")
    elif operacion == 2:
        resultado = numero1 - numero2
        print(f"El resultado es: {resultado}")
    elif operacion == 3:
        resultado = numero1 * numero2
        print(f"El resultado es: {resultado}")
    elif operacion == 5:
        resultado = numero1 * numero2
        resultado = resultado / 100
        print(f"El {numero2}% de {numero1} es: {resultado}")
    elif operacion == 6:
        print("Adios!")
    try:
        if operacion == 4:
            resultado = numero1 / numero2
            if resultado == 0.0:
                print("Ingrese un numero que no sea cero")
            elif resultado != 0.0:
                print(f"El resultado es: {resultado}")
            
    except ZeroDivisionError:
        print("Ingrese un numero que no sea cero")
except ValueError:
    print("Ingrese un dato numerico")


