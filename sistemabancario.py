#import datetime as dt
import textwrap

def menu():
    print("=" * 100)
    menu = """
                BEM VINDO AO BANCO LU
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova Conta
        [nu] Novo Usuário
        [lc] Listar Contas
        [q] Sair

    Por favor, selecione: """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            print(f"\nDepósito realizado com sucesso no valor de R$ {valor:.2f}\n")
            saldo += valor
            extrato += f"Depósito: \t\t+R${valor:.2f}\n"
    else:
        print("Operação falhou! Deposite valores maiores que zero\n")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite_diario, ):
    if limite_diario < 3:
        if valor > saldo:
            print("Saldo insuficiente.\n")

        elif valor > 500:
            print("Limite excedido. É permitido o valor de R$500.00 por saque\n")

        else:
            print(f"\nSaque realizado no valor de: R${saldo:.2f} \n")
            saldo -= valor
            print(f"Saldo atual: \t\tR${saldo:.2f} \n")
            extrato += f"Saque: \t\t-R${valor:.2f}\n"
            limite_diario += 1
    else: 
        print("Limite de saques diários excedido.\n")
    return saldo, extrato

def exibir_extrato(saldo, / , * ,extrato):
    if not extrato:
                print("\nAinda não houveram movimentações. Não deixe sua conta inativa!!")
    else:
        print("\n\n===EXTRATO===\n\n")
        print(extrato)
        print(f"\nSaldo atual: R${saldo:.2f}\n")
        print("====================\n")

def criar_usuario(usuarios):
    cpf = input ("\nInforme o CPF (apenas números): ")
    usuario=filtrar_usuario(cpf,usuarios)

    if usuario:
          print("\n# CPF já cadastrado #")
          return
     
    nome = input("\nInforme o nome completo: ")
    data_nascimento = input("\nInforme a data de nascimento (dd-mm-aaaa): ")
    endereco = input("\nInforme o endereço (logradouro, nº - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data nascimento": data_nascimento,"cpf": cpf, "endereço": endereco})

    print("\n+++ Usuário criado com sucesso! +++")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
          
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n+++ Conta criada com sucesso! +++")
        return{"agencia":agencia, "numero conta":numero_conta, "usuario":usuario}
    
    print("# Usuário não encontrado #")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C: \t\t{conta['numero conta']}
            Titular: \t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    Agencia = "0001"
    usuarios = []
    contas = []
    saldo= 0
    limite_diario= 0 ##Antes de qualquer operação
    extrato = "" ##String vazia!!!!
    

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("\nInforme o valor a ser depositado: "))

            saldo, extrato = depositar(saldo,valor,extrato)

        elif opcao == "s":
            valor = float(input("\nInforme o valor a ser sacado: "))

            saldo, extrato = saque(
                saldo=saldo, 
                valor=valor,
                extrato=extrato,
                limite_diario=limite_diario)

            
        elif opcao =="e":
            exibir_extrato(saldo,extrato=extrato)
            

        elif opcao == "q":
            print("Obrigado por utilizar nossos serviços! ♥")
            break
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = criar_conta(Agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas) 


        else:
            print("Selecione uma opção válida")
    return


main()
