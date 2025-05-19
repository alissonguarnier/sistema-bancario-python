# Sistema Bancário - Versão 2

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("❌ Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("❌ Operação falhou! Valor excede o limite por saque.")
    elif numero_saques >= limite_saques:
        print("❌ Operação falhou! Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("❌ Operação falhou! Valor inválido.")
    
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("❌ Operação falhou! Valor inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()

    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("❌ Já existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("✅ Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
        contas.append(conta)
        print("✅ Conta criada com sucesso!")
    else:
        print("❌ Usuário não encontrado. Crie um usuário primeiro.")

def listar_contas(contas):
    for conta in contas:
        print("=" * 30)
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
        print("=" * 30)

# Programa principal

menu = """
=============== MENU ===============

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = "0001"

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        criar_conta(AGENCIA, numero_conta, usuarios, contas)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        print("👋 Obrigado por usar o sistema bancário. Até mais!")
        break

    else:
        print("❌ Operação inválida. Tente novamente.")
