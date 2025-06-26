# Haga un programa que permita generar un menú de gestión de entradas para el
# Teatro CafeConLeche con la función “Cats” y sus distintos musicales. El menú
# principal debe permitir mostrar 4 opciones:
# TOTEM AUTOATENCIÓN CAFECONLECHE
# 1.- Comprar entrada a Cats.
# 2.- Cambio de función.
# 3.- Mostrar stock de funciones.
# 4.- Salir.
# Todas las opciones del menú deben estar implementadas mediante funciones separadas del código principal (main).
# Al ingresar a la opción 1.- Comprar entrada, se debe permitir ingresar nombre de
# comprador y selección de función por separado. Para que la compra sea exitosa
# se debe cumplir lo siguiente:
# a) El nombre de comprador no debe estar repetido,
# b) La selección de la función debe permitir seleccionar entradas para una de las dos
# funciones.
# Función 1: Cats Día Viernes.
# Función 2: Cats Día Sábado.
# c) Debe haber un máximo de 150 entradas para la función 1, y 180 entradas para la
# función 2.
# En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
# 2
# Al ingresar la opción 2.- Cambio de función, el menú debe permitir el cambio de
# función mediante el nombre. Si el comprador existe, preguntar si desea cambiar de
# función, en caso afirmativo y si hay stock disponible, cambiar a la otra función disponible.
# Al ingresar la opción 3.- Mostrar totales, el menú debe permitir mostrar el total
# entradas disponibles junto con el total de entradas
# Al ingresar la opción 4.- Salir, el programa debe terminar mostrando:
# Programa terminado...
# Si se ingresa una opción distinta (que no sea 1, 2, 3 o 4), debe mostrarse:
# Debe ingresar una opción válida!!
# Importante: Cada ingreso de dato debe estar validado correctamente y al ingresar
# un dato no válido debe solicitar nuevamente el dato, hasta que el usuario ingrese
# correctamente la información

# Menu principal
def main():
    print("Bienvenido al Teatro CafeConLeche")
    while True:
        print ("Menú de Gestión de Entradas:")
        print("1.- Comprar entrada a Cats.")
        print("2.- Cambio de función.")
        print("3.- Mostrar stock de funciones.")
        print("4.- Salir.")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == '1':
            comprar_entrada()
        elif opcion == '2':
            cambio_funcion()
        elif opcion == '3':
            mostrar_stock()
        elif opcion == '4':
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")
            
# Funcion comprar entrada
def comprar_entrada():
    nombre = input("Ingrese el nombre del comprador: ")
    if not validar_nombre(nombre):
        print("El nombre ya está registrado. Intente nuevamente.")
        return
    
    funcion = seleccionar_funcion()
    if funcion is None:
        print("Selección de función inválida. Intente nuevamente.")
        return
    
    if registrar_entrada(nombre, funcion):
        print(f"Entrada registrada exitosamente para {nombre} en la función {funcion}.")
    else:
        print("No hay stock disponible para la función seleccionada.")

#Funcion Validar nombre
def validar_nombre(nombre):
    return True 

# Variables globales para el stock y los compradores
stock_funcion = {
    "Cats Día Viernes": 150,
    "Cats Día Sábado": 180
}
compradores = {}

# Funcion registrar entrada
def registrar_entrada(nombre, funcion):
    if nombre in compradores:
        return False
    if stock_funcion[funcion] > 0:
        compradores[nombre] = funcion
        stock_funcion[funcion] -= 1
        return True
    return False

# Funcion seleccionar nueva funcion
def seleccionar_funcion():
    print("Seleccione la función:")
    print("1.- Cats Día Viernes")
    print("2.- Cats Día Sábado")
    while True:
        seleccion = input("Ingrese 1 o 2: ")
        if seleccion == '1':
            return "Cats Día Viernes"
        elif seleccion == '2':
            return "Cats Día Sábado"
        else:
            print("Selección inválida. Intente nuevamente.")

# Funcion cambio de funcion
def cambio_funcion():
    nombre = input("Ingrese el nombre del comprador para cambiar de función: ")
    if nombre not in compradores:
        print("El comprador no existe. Intente nuevamente.")
        return
    
    funcion_actual = compradores[nombre]
    print(f"Función actual: {funcion_actual}")
    
    nueva_funcion = seleccionar_funcion()
    if nueva_funcion == funcion_actual:
        print("No se puede cambiar a la misma función.")
        return
    
    if stock_funcion[nueva_funcion] > 0:
        stock_funcion[funcion_actual] += 1  # Devolver entrada a la función actual
        compradores[nombre] = nueva_funcion
        stock_funcion[nueva_funcion] -= 1  # Registrar nueva entrada
        print(f"Cambio de función exitoso para {nombre} a {nueva_funcion}.")
    else:
        print("No hay stock disponible para la nueva función seleccionada.")

# Funcion mostrar stock
def mostrar_stock():
    print("Stock de funciones:")
    for funcion, stock in stock_funcion.items():
        print(f"{funcion}: {stock} entradas disponibles")
    total_entradas = sum(stock_funcion.values())
    print(f"Total de entradas disponibles: {total_entradas}")
    
if __name__ == "__main__":
    main()


