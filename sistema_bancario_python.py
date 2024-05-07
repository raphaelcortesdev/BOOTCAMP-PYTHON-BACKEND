import os
LIMITE_SAQUE_DIARIO = 3

menu = """###SISTEMA BANCÁRIO###
 [1] DEPÓSITO
 [2] SAQUE
 [3] EXTRATO
 [4] SAIR
 => """
saldo = 0
limite_saque_valor = 500
extrato = ''
cont_saque = 0

while True:
    
    os.system('cls')
    opcao = int(input(menu))

    if opcao == 1:
        
        deposito = float(input('QUANTO DESEJA DEPOSITAR?\n => R$'))
        while deposito <= 0:
            deposito = float(input('!!DEPÓSITO INVÁLIDO!! DIGITE UM VALOR POSITIVO \n => R$'))
        saldo += deposito
        extrato += 'Depósito = R${:.2f}\n'.format(deposito)
        print('\nOPERAÇÃO REALIZADA.\n')
        os.system('pause')

    if opcao == 2:
        
        print('VOCÊ TEM {} SAQUES DIÁRIOS COM UM VALOR LIMITE DE R${}\n'.format(LIMITE_SAQUE_DIARIO, limite_saque_valor))
        
        if cont_saque < LIMITE_SAQUE_DIARIO:
            saque = float(input('QUANTO DESEJA SACAR?\n => R$'))
            while saque <= 0 or saque > 500:
                saque = float(input('!!SAQUE INVÁLIDO!! DIGITE UM VALOR POSITIVO MENOR QUE R$500\n => R$'))
            
            if saque < saldo:
                print('\nOPERAÇÃO REALIZADA.\n')
                cont_saque += 1
                saldo -= saque
                extrato += 'Saque = R${:.2f}\n'.format(saque)
                os.system('pause')
            else:
                print('!!SALDO INSUFICIENTE!!\nSALDO = R${:.2f}'.format(saldo))
                os.system('pause')
        
        else:
            print('!!LIMITE DE SAQUE DIÁRIO ATINGIDO!!\nTENTE NOVAMENTE AMANHÃ.\n')
            os.system('pause')

    if opcao == 3:

        os.system('cls')
        print('###EXTRATO###')
        print(extrato)
        print('SALDO TOTAL => R${:.2f}'.format(saldo))
        os.system('pause') 

    if opcao == 4:

        print('OBRIGADO POR USAR NOSSA BANCO.\n')
        os.system('pause')
        break

    else:
        print('!!OPÇÃO INVÁLIDA!!')
        os.system('pause')
