print("****Bienvenido a su calculadora virtual*****")
numero1 = int(input("Ingrese un número "))
print("*" * 6, "Escoja el tipo de operación",
"*" * 6)
counter = 0
new_number = 0 + numero1
while counter <= 10:
  operacion = int(input("""Ingresa tu opción:
  1. Suma
  2. Resta
  3. Multiplicación
  4. Division
  5. Salir
  Ingresa aqui => """))  
  if operacion == 1:
    new_number = new_number + int(input("Ingrese otro numero "))
    print("El resultado de su operación es ", new_number)
    validation = input("Quieres continuar? (y/n) ")
    if validation == "y":
      continue
    else:
      break    
    counter += 1
  elif operacion == 2:
    new_number = new_number - int(input("Ingrese otro numero "))
    print("El resultado de su operación es ", new_number)
    validation = input("Quieres continuar? (y/n) ")
    if validation == "y":
        continue
    else:
      break  
    counter += 1
  elif operacion == 3:
    new_number = new_number * int(input("Ingrese otro numero "))
    print("El resultado de su operación es ", new_number)
    validation = input("Quieres continuar? (y/n)")
    if validation == "y":
        continue
    else:
      break 
    counter += 1
  elif operacion == 4:
    new_number = new_number / int(input("Ingrese otro numero "))
    print("El resultado de su operación es ", new_number)
    validation = input("Quieres continuar? (y/n) ")
    if validation == "y":
        continue
    else:
      break 
    counter += 1
  elif operacion == 5:
    break
  else:
    print("Seleccione una opción correcte, recuerde que debe ingresar el número de su operación")
  
  