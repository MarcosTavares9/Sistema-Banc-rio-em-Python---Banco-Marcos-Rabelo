# MENU PRINCIPAL
def menu():
    return """
    ==================================================
                Banco Marcos Rabelo

    [d] Depositar
    [s] Sacar (Limite: R$ 500 por saque)
    [e] Extrato
    [q] Sair

    * Você pode realizar até 3 saques diários.

    ==================================================
    => """

def menu_cadastro():
    return """
    ==================================================
                Banco Marcos Rabelo

    [u] Cadastro de Novo Usuário
    [c] Cadastro de Conta
    [l] Listar Contas e Usuarios
    [a] Acesso ao Sistema
    [q] Sair

    ==================================================
    => """

# REALIZAR SAQUES
def saque(conta, valor, numero_de_saques, LIMITE_SAQUES, limite):
    print("=".center(50, "="))
    if numero_de_saques < LIMITE_SAQUES:
        if valor > 0 and valor <= limite:
            if valor <= conta['saldo']:
                conta['saldo'] -= valor
                conta['extrato'].append(f"Saque: R$ {valor:.2f}")
                numero_de_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
        print("Você já realizou o limite de 3 saques diários.")
    print("=".center(50, "="))
    return numero_de_saques

# REALIZAR DEPÓSITOS
def depositos(conta, valor):
    print("Deposito".center(50, "="))
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'].append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    print("=".center(50, "="))

# VERIFICAR EXTRATOS
def registros(conta):
    print("Extrato".center(50, "="))
    print(f"Conta: {conta['numero_conta']}")
    print(f"Agência: {conta['agencia']}")
    print(f"CPF: {conta['cpf']}")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}\n")
    print("Transações:")
    if not conta['extrato']:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in conta['extrato']:
            print(transacao)
    print("=".center(50, "="))

# CADASTRAR NOVO USUÁRIO
def verificacao(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: Usuário com este CPF já está cadastrado.")
            return True
    return False

def cadastro_usuario(nome, data_nascimento, cpf, endereco):
    if verificacao(cpf):
        return
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# CRIAR NOVA CONTA
def criar_conta(usuario, cpf):
    global numero_sequencial_conta

    agencia = "0001"
    numero_conta = numero_sequencial_conta
    numero_sequencial_conta += 1

    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuario,
        'cpf': cpf,
        'saldo': 0.00,
        'extrato': []
    }

    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}")

# FUNÇÃO PARA ENCONTRAR CONTA PELO NÚMERO DA CONTA
def encontrar_conta(numero_conta):
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            return conta
    print("Conta não encontrada.")
    return None

# LISTAR CONTAS E USUÁRIOS
def lista_conta_usuario(usuarios, contas):
    if not usuarios:
        print("Nenhum Usuário Cadastrado")
    else:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}")
            print(f"Data de Nascimento: {usuario['data_nascimento']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Endereço: {usuario['endereco']}")
            print("-" * 50)

    if not contas:
        print("Nenhuma Conta Cadastrada")
    else:        
        print("\nContas cadastradas:")
        for conta in contas:
            print(f"Agência: {conta['agencia']}")
            print(f"Número da Conta: {conta['numero_conta']}")
            print(f"Titular da Conta: {conta['usuario']['nome']}")
            print("-" * 50)

# VARIÁVEIS GLOBAIS
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
numero_sequencial_conta = 1

# MENU DE CADASTRO E ACESSO
while True:
    opcao = input(menu_cadastro()).lower()
    
    if opcao == 'u':
        print("Cadastro de Novo Usuário".center(50, "="))
        while True:
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
            cpf = input("CPF (apenas números): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            cadastro_usuario(nome, data_nascimento, cpf, endereco)

            continuar = input("Deseja cadastrar outro usuário? (s/n): ").lower()
            if continuar == 'n':
                break

    elif opcao == 'c':
        cpf = input("Digite o CPF do usuário para criar uma conta: ")
        usuario_encontrado = next((user for user in usuarios if user['cpf'] == cpf), None)
        if usuario_encontrado:
            criar_conta(usuario_encontrado, cpf)
        else:
            print("Usuário não encontrado. Verifique o CPF ou cadastre o usuário primeiro.")

    elif opcao == 'l':
        lista_conta_usuario(usuarios, contas)

    elif opcao == 'a':
        numero_conta = int(input("Digite o número da conta para acessar: "))
        conta = encontrar_conta(numero_conta)

        if conta:
            print(f"Bem-vindo ao Banco, {conta['usuario']['nome']}!")
            numero_de_saques = 0
            
            while True:
                opcao = input(menu()).lower()

                if opcao == 'd':
                    valor = float(input("Informe o valor do Depósito: R$ "))
                    depositos(conta, valor)

                elif opcao == 's':
                    valor = float(input("Informe o valor do Saque: R$ "))
                    numero_de_saques = saque(conta, valor, numero_de_saques, LIMITE_SAQUES, limite)

                elif opcao == 'e':
                    registros(conta)

                elif opcao == 'q':
                    print("Saindo da operação".center(50, "="))
                    break

                else:
                    print("Operação inválida, por favor selecione novamente a operação desejada.")

        else:
            print("Conta não encontrada. Verifique o número da conta ou cadastre a conta primeiro.")

    elif opcao == 'q':
        print("Saindo da operação".center(50, "="))
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
