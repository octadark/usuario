class usuario:
    def __init__(self, name):
        self.name = name
        self.amount = 0
    def hacer_deposito(self, amount):
        self.amount += amount
    def hacer_retiro(self, amount):
        self.amount -= amount
    def transferir_dinero(self, amount, usuario):
        self.amount -= amount
        usuario.amount += amount
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance:{self.amount}")

adrien = usuario("Adrien")
adrien.hacer_deposito(100)
adrien.hacer_deposito(200)
adrien.hacer_deposito(50)
adrien.hacer_retiro(45)
adrien.mostrar_balance_usuario()

nibbles = usuario("Mr Nibbles")
nibbles.hacer_deposito(500)
nibbles.hacer_deposito(500)
nibbles.hacer_deposito(300)
nibbles.hacer_retiro(100)
nibbles.mostrar_balance_usuario()

benny_bob = usuario("Benny Bob")
benny_bob.hacer_deposito(1500)
benny_bob.hacer_retiro(1000)
benny_bob.hacer_retiro(5000)
benny_bob.hacer_retiro(3000)
benny_bob.mostrar_balance_usuario()

nibbles.transferir_dinero(400, adrien)