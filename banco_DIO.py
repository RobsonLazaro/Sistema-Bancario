menu = """
        DIGITE ALGUMA DAS OPÇÕES:

[d] - REALIZAR DEPÓSITO
[s] - REALIZAR SAQUE
[e] - VIZUALIZAR EXTRATO
[q] - SAIR

    BANCO DIO AGRADECE SUA FIDELIDADE!

>="""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("--Depósito--")
        valor = float(input("Digite o valor que você deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito no valor de R${valor:.2f}\n"
        else:
            print("Você não pode depositar esse valor, tente novamente! ")

    elif opcao == "s":
        print("--Saque--")

        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor que você deseja sacar: "))

            if valor <= limite:

                if valor <= saldo:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"Saque no valor de R${valor:.2f}\n"
                else:
                    print("Você não tem saldo disponivel para saque!")

            else:
                print("Você tentou sacar um valor maior que o limite!")

        else:
            print("Limite de saque diário atingido!")

    elif opcao == "e":
        print("--Extrato--")
        print(extrato)
        print(f"Seu saldo é de R${saldo}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
