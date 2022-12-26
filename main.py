print("****Bienvenido a su calculadora virtual*****")
numero1 = int(input("Ingrese un número "))
print("*" * 6, "Escoja el tipo de operación",
"*" * 6)
print("""1. Suma
2. Resta
3. División
4. Multiplicación
5. Salir""")
operacion = int(input("Ingresa tu opción "))
while operacion >= 1 and operacion <= 5:
  if operacion == 1:
    numero2 = int(input("Ingrese otro numero "))
    resultado = numero1 + numero2 
    print(resultado)
    operacion = int(input('''Ingrese otra operación
    1. Suma
    2. Resta
    3. División
    4. Multiplicación
    5. Salir
    '''))
    resultado = resultado + numero2
    print(resultado)
  elif operacion == 2:
    numero2 = int(input("Ingrese otro numero "))
    resultado = numero1 - numero2 
    print(resultado)
  elif operacion == 3:
    numero2 = int(input("Ingrese otro numero "))
    resultado = numero1 / numero2 
    print(resultado)
  elif operacion == 4:
    numero2 = int(input("Ingrese otro numero "))
    resultado = numero1 * numero2 
    print(resultado)
  
    
  
  