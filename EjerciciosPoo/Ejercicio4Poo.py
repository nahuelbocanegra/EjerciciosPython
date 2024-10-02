"""4. Cuenta Bancaria. Crea una clase CuentaBancaria con los siguientes atributos
obligatorios: número de cuenta, nombre y apellido. El saldo debe comenzar con
100.000. Agrega e implementa métodos para: 1- depositar (debe aceptar un valor
entero y sumarlo al saldo), 2- retirar (debe aceptar un valor entero y restarlo al saldo
sólo si hay dinero suficiente para retirar en la cuenta) y 3- ver saldo. Además, escribe
una aplicación de consola que permita al usuario depositar, retirar o ver saldo hasta
que decida detenerse. Al finalizar deberá mostrar los datos de la cuenta y el saldo."""

class CuentaBancaria:
    def __init__( self,num_cuenta, nombre ,apellido) -> None:
        
            self.num_cuenta=num_cuenta        
            self.nombre=nombre
            self.nombre=apellido
            self.saldo=100000
    
    def depositar(self,deposito):
          if deposito > 0:
                self.saldo += deposito
                return "deposito exitoso"
    
    def retirar(self,retiro):
          if self.saldo <= 0:
                return "fondo insuficiente"
          self.saldo-=retiro
          return "retiro exitoso"
    
    def ver_saldo(self):
          return "su saldo es de {}".format(self.saldo)          