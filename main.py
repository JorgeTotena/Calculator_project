import math
def number():
  print("****Bienvenido a su calculadora virtual*****")
  numero1 = int(input("Ingrese un número "))
  print("*" * 6, "Escoja el tipo de operación",
  "*" * 6)
  return numero1

first_number = number()
print(first_number)

def operation():  
  counter = 0
  new_number = 0 + first_number 
  while counter <= 10:
    operacion = int(input("""Ingresa tu opción:
    1. Suma
    2. Resta
    3. Multiplicación
    4. Division
    5. Potencia
    6. Raiz cuadrada
    7. Salir
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
      new_number = new_number // int(input("Ingrese otro numero "))
      print("El resultado de su operación es ", new_number)
      validation = input("Quieres continuar? (y/n) ")
      if validation == "y":
          continue
      else:
       break   
    elif operacion == 5:
      new_number = new_number ** int(input("Ingrese otro numero "))
      print("El resultado de su operación es ", new_number)
      validation = input("Quieres continuar? (y/n) ")
      if validation == "y":
       continue
      else:
       break 
      counter += 1
    elif operacion == 6:
      new_number = math.sqrt(new_number)
      print("El resultado de su operación es ", new_number)
      validation = input("Quieres continuar? (y/n) ")
      if validation == "y":
       continue
      else:
       break 
      counter += 1
      
    elif operacion == 7:
      break
    else:
      print("Seleccione una opción correcta, recuerde que debe ingresar el número de su operación")
    
operation()
