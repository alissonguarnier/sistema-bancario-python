# 💰 Sistema Bancário Simples em Python

Este é um sistema bancário básico desenvolvido em Python, como parte de um exercício para prática de lógica de programação. O sistema permite realizar **depósitos**, **saques** e **visualizar o extrato** da conta. Ele foi desenvolvido para simular uma conta bancária de um único usuário, sem a necessidade de autenticação ou dados de agência/conta.

## 📋 Funcionalidades

- [x] **Depósito**
  - Permite depositar valores positivos.
  - Os valores são somados ao saldo e registrados no extrato.

- [x] **Saque**
  - Permite realizar até 3 saques diários.
  - Cada saque tem um limite máximo de R$ 500,00.
  - Verifica se há saldo suficiente antes da operação.
  - Registra o saque no extrato.

- [x] **Extrato**
  - Exibe todas as movimentações (depósitos e saques).
  - Mostra o saldo atual da conta.
  - Caso não haja movimentações, exibe uma mensagem informativa.

## 📌 Regras de Negócio

1. O sistema é feito para **um único usuário**.
2. Só é possível **depositar valores positivos**.
3. Cada **saque**:
   - Tem limite de R$ 500,00 por operação.
   - Só pode ser feito até **3 vezes por dia**.
   - Só é permitido se houver saldo suficiente.
4. O **extrato** mostra as movimentações no formato:
