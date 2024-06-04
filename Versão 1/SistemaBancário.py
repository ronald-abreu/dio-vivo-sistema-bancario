import textwrap


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF: \n")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado \n")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
                Agência: \t{conta['agencia']}
                C/C: \t\t{conta['numero_conta']}
                Titular: \t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def criar_usuario(usuarios):
    cpf = input("CPF: \n")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já existente con esse CPF.\n")
        return
    
    nome = input("Nome: \n")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): \n")
    endereco = input("Endereço: \n")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario criado")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def depositar(valor, saldo, extrato, /):

    while valor <= 0:
        print("Valor inválido")
        valor = float(input("Valor: "))

    saldo += valor
    extrato += f"\033[1;32m + {valor:.2f}  \033[m\n"
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saques:
        print("Limite de saque diário esgotado")


    elif excedeu_limite:
        print("Valor maior que 500")
    
    elif excedeu_saldo:
        print("Saldo insuficiente")

    elif valor > 0:
        saldo -= valor
        extrato += f"\033[1;31m - {valor:.2f} \033[m\n"
        numero_saques += 1

    else:
        print("Valor Inválido")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("<================= EXTRATO BANCÁRIO =================>")
    print(extrato + f"\n  Saldo = \033[1;32;40m R$ {saldo:.2f} \033[m \n")
    print("<====================================================>")

def menu():
    menu = """\n
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Nova Conta
    [5] - Listar Contas
    [6] - Novo Usuário
    [7] - Sair

    => """
    return input(textwrap.dedent(menu))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numeros_saques = 0
    usuarios = []
    contas = []
    

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Valor: "))

            saldo, extrato = depositar(valor, saldo, extrato)
            

        elif opcao == "2":
            valor = float(input("Valor: "))

            saldo, extrato, numeros_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numeros_saques,
                limite_saques=LIMITE_SAQUES)
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)
        
        elif opcao == "7":
            break

        else:
            print("Opção inválida")

main()


