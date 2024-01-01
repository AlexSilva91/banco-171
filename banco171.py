from conta import Conta
from operacoes import op_contas

def exibir_menu():
    print('\n*********BANCO-171***********')
    print('* 0 - Sair')
    print('* 1 - Abrir conta')
    print('* 2 - Depósito')
    print('* 3 - TED')
    print('* 4 - Listar contas')
    print('* 5 - Créditar juros em conta')
    print('*********BANCO-171***********\n')

def processar_escolha(escolha):
    if escolha == 0:
        print('\nSaindo...')
    elif escolha==1:
        op_contas.cadastrar_conta()
    elif escolha==2:
        op_contas.deposit()
    elif escolha==3:
        op_contas.TED()
    elif escolha==4:
        op_contas.listar_contas()
    elif escolha==5:
        op_contas.render_juros_sob_saldo()
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