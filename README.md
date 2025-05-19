# 💳 Sistema Bancário em Python (Versão POO)

Este projeto é uma versão orientada a objetos de um sistema bancário simples, desenvolvido em Python como parte de um exercício de aprendizado. Ele permite criar clientes, abrir contas, realizar depósitos, saques e consultar o extrato bancário.

## 📚 Objetivos

- Aplicar os conceitos de Programação Orientada a Objetos (POO)
- Modelar o sistema conforme o diagrama UML fornecido
- Criar uma estrutura modular e reutilizável
- Substituir dicionários por classes e objetos

---

## 🧱 Estrutura do Projeto

### Classes implementadas:

- **PessoaFisica**: Representa um cliente com CPF, nome e data de nascimento
- **Cliente**: Superclasse de PessoaFisica, armazena endereço e lista de contas
- **Conta**: Representa uma conta bancária com saldo, número e histórico
- **ContaCorrente**: Subclasse de Conta, com limite de saque e número de saques diários
- **Historico**: Armazena todas as transações realizadas
- **Transacao (interface)**: Abstração para operações bancárias
  - **Deposito**: Implementa transação de depósito
  - **Saque**: Implementa transação de saque

---

## ⚙️ Funcionalidades

- [x] Criar usuário (cliente)
- [x] Criar conta corrente
- [x] Realizar depósito
- [x] Realizar saque com regras de limite
- [x] Consultar extrato bancário com histórico
- [x] Validação de CPF único
- [x] Limitação de saques diários

---

## 🖥️ Menu do Sistema
```
=============== MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[q] Sair
```

---
## ▶️ Como Executar

1. **Clone o repositório** (caso aplicável):

```bash
git clone https://github.com/alissonguarnier/sistema-bancario-python.git
cd sistema-bancario-python.git
```

## 🧪 Exemplo de Uso

```
# Criar novo usuário
[nu]
Informe o CPF: 12345678900
Informe o nome: João da Silva
...

# Criar conta para o CPF informado
[nc]
Informe o CPF do cliente: 12345678900

# Realizar depósito
[d]
Informe o CPF do titular: 12345678900
Informe o valor do depósito: 200.00

# Realizar saque
[s]
Informe o CPF do titular: 12345678900
Informe o valor do saque: 50.00

# Ver extrato
[e]
```

## 📌 Regras de Negócio

- Cada cliente pode ter múltiplas contas
- Cada conta tem limite de 3 saques diários de até R$ 500,00 por operação
- Não é possível cadastrar dois clientes com o mesmo CPF
- O histórico armazena data, tipo e valor de cada transação

## 📁 Estrutura dos Arquivos
```
bancario-alissonguarnier-varsao3.py   # Código principal
bancario-alissonguarnier-varsao2.py   # Código antigo
bancario-alissonguarnier.py           # Primeiro Código
README.md                             # Documentação
```

## 🧑‍💻 Autor
Desenvolvido por Alisson Guarniêr como parte de uma atividade prática do Bootcamp de python da Dio.

## 📜 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](ainda não tem) para detalhes.

