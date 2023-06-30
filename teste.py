menu = """

======= Menu =======

[d] Depositar
[s] Sacar
[e] Extrato
[SD] Saque Disponível
[w] Sair
====================

"""

saldo = 0
limite = 500
extrato =""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))


        if valor > 0:
            saldo += valor
            extrato += f"Depósito no valor de R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor} efetuado com sucesso!!!")
            print(f"Seu saldo atual é de R$ {saldo}.")

    
        else:
            print(" Operação inválida! Por favor, tente com outro valor.")

    elif opcao  == "sd":
        print(numero_saques)


    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado: "))

        saldo_excedido = valor > saldo

        limite_excedido = valor > limite

        saque_excedido = numero_saques >= LIMITE_SAQUES


        if saldo_excedido:
            print("Saldo insuficiente! Tente Novamente!")

        elif limite_excedido:
            print("Limite excedido! Tente Novamente!")

        elif saque_excedido:
            print("Saque excedido! Tente Novamente!")

        elif saldo > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}"
            numero_saques += 1

        else:
            print("Operação inválida! Tente Novamente!")

    elif opcao == "e":
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==================================")


    elif opcao == "w":
        break
    
    else:
        print("Operação inválida, selecione novamente a operação desejada.")
        