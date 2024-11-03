# Sistema Bancário em Python - Banco Marcos Rabelo

Este repositório contém duas versões do projeto de Sistema Bancário em Python, desenvolvido para simular operações bancárias com funcionalidades básicas e avançadas.

## Projeto 1: Sistema Bancário Básico

Este projeto é uma implementação inicial de um sistema bancário simples. Ele simula as principais operações de um banco, com funcionalidades e restrições básicas para depósitos, saques e extratos.

### Funcionalidades Implementadas
- **Depósito**: Permite ao usuário realizar depósitos, com validação para valores positivos.
- **Saque**: Limite de R$ 500,00 por saque, com até 3 saques diários, respeitando o saldo disponível.
- **Extrato**: Exibe todas as movimentações e o saldo atual.
- **Limites de Operações**: Até 3 saques por dia e limite de R$ 500,00 por saque.

### Exemplo de Menu - Projeto 1
==================================================

            Banco Marcos Rabelo

[d] Depositar

[s] Sacar (Limite: R$ 500 por saque)

[e] Extrato

[q] Sair


* Você pode realizar até 3 saques diários.
  

==================================================

=> 



### Tecnologias e Conceitos
- **Linguagem**: Python
- **Conceitos**: Controle de fluxo, validação de entrada e operações financeiras simples.

---

## Projeto 2: Melhorias com Suporte a Múltiplas Contas

Nesta versão, o sistema foi aprimorado para gerenciar múltiplas contas por usuário, permitindo um controle mais detalhado de cada conta. As transações são registradas individualmente por conta, com extratos detalhados.

### Funcionalidades Adicionais
- **Múltiplas Contas por Usuário**: Permite que cada usuário possua várias contas.
- **Registro por Conta**: Cada conta possui um histórico individual com saldo, agência, número da conta, CPF e transações (depósitos e saques).
- **Extrato Detalhado**: Exibe o saldo e o histórico de cada conta separadamente.

### Exemplo de Menu - Projeto 2

            MENU INICIAL CADASTRO DE USUARIO E CONTA

==================================================

                Banco Marcos Rabelo

    [u] Cadastro de Novo Usuário
    
    [c] Cadastro de Conta
    
    [l] Listar Contas e Usuarios
    
    [a] Acesso ao Sistema
    
    [q] Sair

==================================================

                        MENU PRINCIPAL

==================================================

                Banco Marcos Rabelo

    [d] Depositar
    
    [s] Sacar (Limite: R$ 500 por saque)
    
    [e] Extrato
    
    [q] Sair

    * Você pode realizar até 3 saques diários.

    ==================================================

 
### Tecnologias e Conceitos
- **Linguagem**: Python
- **Conceitos**: Estruturas de dados para gerenciar múltiplas contas, controle de fluxo aprimorado e operações financeiras detalhadas.

---

## Objetivo do Projeto
Esses projetos foram desenvolvidos como parte de um desafio da DIO (Digital Innovation One), com o objetivo de praticar lógica de programação e controle de fluxo em Python. As melhorias na segunda versão tornam o sistema mais realista e funcional, permitindo a experiência de um sistema bancário com múltiplas contas.

---

Este README fornece uma visão geral das funcionalidades e dos menus de cada versão, destacando a evolução do sistema bancário no repositório.

