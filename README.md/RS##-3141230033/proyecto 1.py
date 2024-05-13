import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def mostrar_menu():
    print("Seleccione una opción:")
    print("A) Rectángulo")
    print("B) Triángulo")
    print("C) Círculo")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada (A/B/C): ").upper()

        if opcion == 'A':
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = calcular_area_rectangulo(base, altura)
            print("El área del rectángulo es:", area)
        elif opcion == 'B':
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print("El área del triángulo es:", area)
        elif opcion == 'C':
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print("El área del círculo es:", area)
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (A/B/C).")
        
        continuar = input("¿Desea calcular el área de otra figura? (SI/N0): ").upper()
        if continuar != 'SI':
            break

if __name__ == "__main__":
    main()
