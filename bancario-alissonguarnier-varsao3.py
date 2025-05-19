from abc import ABC, abstractmethod
from datetime import datetime


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Conta:
    def __init__(self, cliente, numero):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def saldo_conta(self):
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False
        self.saldo += valor
        return True


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if valor > self.limite:
            print("Saque excede o limite por operação.")
            return False
        if self.numero_saques >= self.limite_saques:
            print("Número máximo de saques diários excedido.")
            return False
        if super().sacar(valor):
            self.numero_saques += 1
            return True
        return False


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


# Funções auxiliares para o menu
def localizar_cliente(cpf, clientes):
    for cliente in clientes:
        if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
            return cliente
    return None


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = localizar_cliente(cpf, clientes)

    if cliente:
        print("CPF já cadastrado.")
        return

    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

    novo_cliente = PessoaFisica(nome, data_nasc, cpf, endereco)
    clientes.append(novo_cliente)
    print("Cliente criado com sucesso!")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = localizar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    conta = ContaCorrente(cliente, numero_conta)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print("Conta criada com sucesso!")


def menu():
    return """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [q] Sair
    => """


def main():
    clientes = []
    contas = []

    while True:
        opcao = input(menu())

        if opcao == "d":
            cpf = input("Informe o CPF do titular: ")
            cliente = localizar_cliente(cpf, clientes)

            if not cliente or not cliente.contas:
                print("Cliente não encontrado ou sem conta.")
                continue

            valor = float(input("Informe o valor do depósito: "))
            transacao = Deposito(valor)
            cliente.realizar_transacao(cliente.contas[0], transacao)

        elif opcao == "s":
            cpf = input("Informe o CPF do titular: ")
            cliente = localizar_cliente(cpf, clientes)

            if not cliente or not cliente.contas:
                print("Cliente não encontrado ou sem conta.")
                continue

            valor = float(input("Informe o valor do saque: "))
            transacao = Saque(valor)
            cliente.realizar_transacao(cliente.contas[0], transacao)

        elif opcao == "e":
            cpf = input("Informe o CPF do titular: ")
            cliente = localizar_cliente(cpf, clientes)

            if not cliente or not cliente.contas:
                print("Cliente não encontrado ou sem conta.")
                continue

            conta = cliente.contas[0]
            print("\n========== EXTRATO ==========")
            for transacao in conta.historico.transacoes:
                print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
            print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
            print("==============================")

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "q":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
