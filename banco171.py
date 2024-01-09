from conta import Conta
from operacoes import op_contas

def exibir_menu():
    print('\n*********BANCO-171***********')
    print('* 0 - Sair')
    print('* 1 - Abrir conta')
    print('* 2 - Acessar conta')
    print('* 3 - Listar contas')
    print('*********BANCO-171***********\n')

def exibir_menu_conta(conta):
    print('\n***************{}*************\n'.format(conta))
    print('* 0 - Sair')
    print('* 1 - Depósito')
    print('* 2 - TED')
    print('* 3 - Extrato')
    print('* 4 - Créditar juros em conta')
    print('* 5 - Cancelar conta')
    print('******************************\n')

def processar_escolha(escolha):
    if escolha == 0:
        print('\nFinalizando...')
    elif escolha==1:
        op_contas.cadastrar_conta()
    elif escolha==2:
        menu_conta()
    elif escolha==3:
        op_contas.listar_contas()
    else:
        print('\nOpção inválida! Tente novamente.\n')

def menu_conta():
    conta = op_contas.buscar_por_conta()
    if conta is not None:
        while True:
            exibir_menu_conta(conta.num_conta)
            escolha = int(input('Qual operação deseja realizar: '))
            processar_escolha_menuConta(escolha)
            if escolha==0:
                break
            elif escolha==5:
                break
    else:
        print('Conta inválida! Tente novamente...')

def processar_escolha_menuConta(escolha):
    if escolha == 0:
        print('\nSaindo...')
    elif escolha==1:
        op_contas.deposit()
    elif escolha==2:
        op_contas.TED()
    elif escolha==3:
        op_contas.buscar_conta()
    elif escolha==4:
        op_contas.render_juros_sob_saldo()
    elif escolha==5:
        op_contas.cancelar_conta()
    else:
        print('\nOpção inválida! Tente novamente.\n')

def main():
    while True:
        exibir_menu()
        escolha = int(input('Qual operação deseja realizar: '))
        processar_escolha(escolha)
        if escolha==0:
            break

if __name__=="__main__":
    main()