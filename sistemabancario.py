menu = """
        BEM VINDO AO BANCO LU
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

Por favor, selecione: """

saldo= 0
limite_diario= 0 ##Antes de qualquer operação
extrato = "" ##String vazia!!!!

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("\nInforme o valor a ser depositado: "))

        if valor > 0:
            print(f"\nDepósito realizado com sucesso no valor de R$ {valor:.2f}\n")
            saldo += valor
            extrato += f"Depósito: +R${valor:.2f}\n"
        else:
            print("Operação falhou! Deposite valores maiores que zero\n")

    elif opcao == "s":
        valor = float(input("\nInforme o valor a ser sacado: "))

        if limite_diario < 3:
            if valor > saldo:
             print("Saldo insuficiente.\n")

            elif valor > 500:
                print("Limite excedido. É permitido o valor de R$500.00 por saque\n")

            else:
                print(f"\nSaque realizado no valor de: R${saldo:.2f} \n")
                saldo -= valor
                print(f"Saldo atual: R${saldo:.2f} \n")
                extrato += f"Saque: -R${valor:.2f}\n"
                limite_diario += 1
        else:
            print("Limite de saques diários excedido.\n")
    elif opcao =="e":
        if not extrato:
            print("\nAinda não houveram movimentações. Não deixe sua conta inativa!!")
        else:
            print("\n\n===EXTRATO===\n\n")
            print(extrato)
            print(f"\nSaldo atual: R${saldo:.2f}\n")
            print("====================\n")

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços! ♥")
        break
    else:
        print("Selecione uma opção válida")