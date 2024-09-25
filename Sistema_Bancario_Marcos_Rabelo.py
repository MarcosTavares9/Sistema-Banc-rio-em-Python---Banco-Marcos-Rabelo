menu = """
==================================================
            Banco Marcos Rabelo

[d] Depositar
[s] Sacar (Limite: R$ 500 por saque)
[e] Extrato
[q] Sair

* Você pode realizar até 3 saques diários.

==================================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3
conte = 0

while True: 

    opcao = input(menu).lower()

    if opcao =='d':
        print("Deposito".center(50,"="))
        try:
            valor = float(input("Informe o valor do Deposito: R$ "))

            if valor > 0 :
                saldo += valor
                extrato += f"Deposito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! o valor informado é invalido")
            print("=".center(50,"="))    
        except ValueError:
            print("Operação falhou! Você deve informar um número válido.")

    elif opcao =='s':
        print("Sacar".center(50,"="))
        numero_de_saques += 1

        if numero_de_saques <= LIMITE_SAQUES:
            try:
                valor = float(input("informe o valor do Saque: R$ "))

                if valor > 0 and valor <= 500:
                    if valor<=saldo:
                        saldo -= valor
                        extrato += f"Saque: R$ {valor:.2f}\n"
                    else:
                        
                        print("Saldo insuficiente!")
                        numero_de_saques -= 1
                else:
                    print("Operação falhou! o valor informado é invalido")
                    numero_de_saques -=1
            except ValueError:
                print("Operação falhou! Você deve informar um número válido.")
                numero_de_saques -=1
        else:
            print("Foi efetuado os 3 Saques diarios")
        print("=".center(50,"="))
    elif opcao =='e':
        print("Extrato".center(50,"="))
        
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)

        print(f"Saldo: R$ {saldo:.2f}\n")
        print("=".center(50,"="))
    elif opcao =='q':
        print("Saindo da operação".center(50,"="))
        break
    else:
        print("Operção invalida, por favor selecione novamente a operação desejada.")
    
