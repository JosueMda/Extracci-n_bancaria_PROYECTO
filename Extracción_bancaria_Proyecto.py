# Proyecto para simular "extracciones bancarias" realizado para practicar Programación Orientada a Objetos POO, herencia y funciones

class Persona:
  def __init__(self,nombre,apellido):
    self.nombre = nombre
    self.apellido=apellido

class Cliente (Persona):
  def __init__(self,nombre,apellido,numero_cuenta, balance=0):
    super().__init__(nombre,apellido)
    self.numero_cuenta = numero_cuenta
    self.balance = balance

  def __str__(self):
    return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}"

  def depositar(self,deposito):
    self.balance+=deposito
    print("Deposito aceptado")

  def retirar(self, retiro):
    if self.balance >= retiro:
      print("Retiro Exitoso")
    else:
      print("Saldo insuficiente")

def crear_cliente ():
  nombre_cl = input("Ingrese su nombre: ")
  apellido_cl = input("Ingrese su apellido: ")
  numcuenta_cl = input("Ingrese su numero de cuenta: ")
  cliente = Cliente(nombre_cl,apellido_cl,numcuenta_cl)
  return cliente

def inicio ():
  mi_cliente = crear_cliente()
  print(mi_cliente)
  opcion = 0
  while opcion != "S":
    print("Elije (D) para Depositar, (R) para Retirar o (S) para Salir")
    opcion = input()
    if opcion == "D":
      montoadep = int (input("Ingrese el monto que desea depositar: "))
      mi_cliente.depositar(montoadep)
    elif opcion == "R":
      montoaret = int(input("Ingrese el monto que desea retirar: "))
      mi_cliente.retirar(montoaret)
    print(mi_cliente)
  print("Gracias por su operacion")

inicio()
      