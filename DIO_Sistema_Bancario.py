menu = '''>>>>  Banco DIO  <<<<

    [1] Sacar
    [2] Depositar
    [3] Extrato
    [0] Sair
    
>>> '''

saldo = 0
limite = 500
extrato = []
num_saques = 0
lim_saque = 3

while True:
    opcao = int(input(menu))
    
    if opcao == 1:
        print('>>> Saque <<<')
        print(f'\nSaldo: R$ {saldo:.2f}')
        saque = int(input('\nQual valor deseja sacar: '))

        if num_saques == lim_saque:
            print('Limite diário de saques excedido')
        elif saque > saldo:
            print('Saldo insuficiente')
        elif saque <= saldo:
            if saque > limite:
                print('Limite de R$ 500.00 por saque excedido')
            elif saque <= limite:
                print('Sacando...\n')
                saldo -= saque
                num_saques += 1
                extrato.append(f'\033[0;31m- R$ {saque:.2f}\033[m')
                print(f'Saldo: R$ {saldo:.2f}')

    elif opcao == 2:
        print('>>> Depósito <<<')
        deposito = int(input('Qual valor deseja depositar: '))
        saldo += deposito
        extrato.append(f'\033[0;32m+ R$ {deposito:.2f}\033[m')
        print(f'Saldo: R$ {saldo:.2f}')

    elif opcao == 3:
        print('>>> Extrato Bancário <<<\n')
        for i in extrato:
            print(i)
        print(f'\nSaldo: R$ {saldo:.2f}')

    elif opcao == 0:
        print()
        print('=-' * 15)
        print('Obrigada pela preferência.')
        break

    else:
        print('Opção inálida')
