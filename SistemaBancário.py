saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3


def depositar(saldo):
    deposito = float(input("Valor: "))

    while deposito <= 0:
        if deposito <= 0:
            print("Valor inválido")
        deposito = float(input("Valor: "))

    saldo += deposito
    return deposito, saldo

def sacar(saldo):
    saque = float(input("Valor: "))

    while saque > saldo or saque > 500 or saque <= 0:

        if saque > saldo:
            print("Saldo insuficiente")
        elif saque <=0:
            print("Valor inválido")
        elif saque > 500:
            print("Valor maior que 500")

        saque = float(input("Valor: "))

    saldo -= saque
    return saque, saldo


def exibir_extrato(saldo):
    print("<================= EXTRATO BANCÁRIO =================>")
    print(extrato + f"\n  Saldo = \033[1;32;40m R$ {saldo:.2f} \033[m \n")
    print("<====================================================>")

menu = """
        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Sair

=> """

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito, saldo = depositar(saldo)
        extrato = extrato + f"\033[1;32m + {deposito:.2f}  \033[m\n"

    elif opcao == "2":
        if numeros_saques < 3:
            saque, saldo = sacar(saldo)
            numeros_saques += 1
            extrato = extrato + f"\033[1;31m - {saque:.2f} \033[m\n"
        else:
            print("Limite de saques excedido")

    
    elif opcao == "3":
        exibir_extrato(saldo)
    
    elif opcao == "4":
        break

    else:
        print("Opção inválida")

