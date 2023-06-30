saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("="*10, "Sistema Bancário", "="*10)
    print("1 - Realizar depósito")
    print("2 - Realizar saque")
    print("3 - Extrato da conta")
    print("0 - Sair do sistema")

    op = int(input("Digite a operação: "))

    if op == 1:
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += "Depósito de R$ %.2f\n" % valor

            print("Depósito realizado com sucesso!")

        else:
            print("Valor inválido!")
        
    elif op == 2:
        valor = float(input("Digite o valor a ser sacado: "))

        excedeu_saldo = valor >= saldo
        excedeu_limite = valor >= limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Valor de saque excedido!")
        elif excedeu_saques:
            print("Limite de saques excedido!")
        else:
            if valor > 0:
                saldo -= valor
                extrato += "Saque de R$ %.2f\n" % valor
                numero_saques += 1

                print("Saque realizado com sucesso!")
            else:
                print("Valor inválido!")
    elif op == 3:
        print("-"*15, "Extrato", "-"*15)
        if extrato == "":
            print("Não foram realizadas movimentações!")
        else:
            print(extrato)
        print("Saldo: R$ %.2f" % saldo)
        print("-"*40)
    elif op == 0:
        print("Saindo do sistema...")
        break
    else:
        print("Operação inválida!")
