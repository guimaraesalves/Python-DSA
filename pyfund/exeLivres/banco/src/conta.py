class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.limite < valor):
            print('Saldo Insuficiente!')
        else:
            self.saldo -= valor

    def extrato(self):
        print(f'Titular: ${self.titular} - Conta: ${self.conta}')
        print(f'Saldo: ${self.saldo}')


if __name__ == '__main__':
    conta = Conta('123-4', 'João', 1000.0)
    print(conta.numero)
    print(conta.titular)

    print(conta.limite)

    conta.deposita(50.0)
    conta.saca(100)
    print(conta.saldo)


