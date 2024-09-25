# Sistema Bancário em Python - Banco Marcos Rabelo

Este projeto é uma implementação simples de um Sistema Bancário utilizando a linguagem Python. Ele simula as principais operações de um banco, permitindo realizar depósitos, saques e consultar o extrato. O objetivo do sistema é fornecer uma interface básica para operações financeiras, com limites e restrições típicos de um banco real.

## Funcionalidades Implementadas:
- **Depósito**: Permite ao usuário realizar depósitos em sua conta, com validação de entrada para garantir que o valor seja positivo.
- **Saque**: Limite de R$ 500,00 por saque e até 3 saques diários. O sistema verifica se há saldo suficiente antes de processar o saque.
- **Extrato**: Exibe todas as movimentações realizadas, como depósitos e saques, além do saldo atual.
- **Limites de Operações**: Até 3 saques por dia, com um limite de R$ 500,00 por operação de saque.

## Como funciona:
- O menu interativo permite ao usuário escolher entre as opções de depósito, saque, extrato ou sair.
- O código garante que o usuário só possa sacar até o limite permitido por dia e impede que valores inválidos sejam inseridos nas operações.
- Ao final, o usuário pode visualizar um extrato detalhado de todas as movimentações realizadas durante a sessão.

## Exemplo de Menu:
==================================================
            Banco Marcos Rabelo

[d] Depositar
[s] Sacar (Limite: R$ 500 por saque)
[e] Extrato
[q] Sair

* Você pode realizar até 3 saques diários.

==================================================
=> 


## Tecnologias Utilizadas:
- **Linguagem**: Python
- **Conceitos**: Controle de fluxo, validação de entrada, manipulação de strings e operações financeiras simples.

## Objetivo do Projeto:
Este projeto foi desenvolvido como parte de um desafio proposto pela [DIO](https://web.dio.me) (Digital Innovation One), com o intuito de praticar lógica de programação e controle de fluxo em Python. Ele simula operações bancárias e oferece uma oportunidade de aplicar conhecimentos em desenvolvimento de sistemas.

---

