# Implementação de Depósito, Extrato e Saque

menu = """
        == Menu ==
    Opção 1 -> Depósito
    Opção 2 -> Saque
    Opção 3 -> Extrato
    Opção 4 -> Sair
"""

print(menu)

opcao = 0
saldo = 0
saque = 0
numero_depositos = 0
quantidade_saques = 0

# Maximo de 3 saques por dia, no valor maximo de 500 reais

# Se o cliente não possuir saldo, exibir mensagem dizendo "Saldo insuficiente" para sacar

# Exibir no extrato, todos os saques

# Extrato deve conter, quantidade de depósitos e saques da conta alem de, exibir saldo total da conta

# Valores devem ser exibidos com formato R$ xxx.xx - 1500.45 = R$ 1500.45

while opcao != 4:
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        valor_depositado = float(input("Quantia a ser depositada: R$ "))
        if valor_depositado <= 0:
            print("Valor a invalido para depositar!")
        else:
           
            numero_depositos += 1
            saldo += valor_depositado
    elif opcao == 2:
        if saldo == 0:
            print("Saldo insuficiente!")
        else:
            if quantidade_saques == 3:
                print("Limite diario de saques atingido!")
            else:
                valor_saque = float(input("Valor a ser sacado: R$ "))
                if valor_saque > saldo:
                    print("Saldo insuficiente!")
                else:
                    quantidade_saques += 1
                    saque += valor_saque
    elif opcao == 3:
        saldo_atual = saldo - saque
        print(
            f"""
Saldo da conta: R$ {saldo_atual:,.2f}
Quantidade de depositos: {numero_depositos}
Quantidade de saques: {quantidade_saques}
            """
        )
    elif opcao == 4:
        print("Operacoes Encerradas.")
        break
    
    else:
        print('Operacao Invalida.')