from conta import Conta

def exibir_menu():
    print('*********BANCO-171***********')
    print('* 0 - Sair')
    print('* 1 - Abrir conta')
    print('* 2 - Depósito')
    print('* 3 - TED')
    print('* 4 - Listar contas')
    print('*********BANCO-171***********')

def cadastrar_conta():
    print('Abrindo conta....\n*******************************')
    cpf=int(input('Digite o CPF: '))
    nome=input('Digite seu nome: ')
    senha=int(input('Defina sua senha: '))
    num_conta=int(input('Número da conta: '))
    saldo=float(input('Valor do depósito inicial: '))
    status='ativo'
    
    conta=Conta(cpf,nome,senha,num_conta,saldo,status)

    print('*******************************')
    print('\nConta aberta com sucesso!')
    print('*******************************')

def processar_escolha(escolha):
    if escolha == 0:
        print('\nSaindo...')
    elif escolha==1:
        cadastrar_conta()
    elif escolha==2:
        cont=int(input('\nConta: '))
        deposit=float(input('\nValor de depósito: '))
        if Conta.atualizar_saldo_por_conta(cont, deposit):
            print('\n******Depósito realizado com sucesso!******')
    elif escolha==3:
        cont_origem=int(input('\nConta de Origem: '))
        cont_destino=int(input('\nConta de Destino: '))
        valor=float(input('\nValor a transferir: '))
        if Conta.tranfere_valor_entre_contas(cont_origem,cont_destino,valor):
            print('00000000000000000000000000000\nTransferência realizada com sucesso!\n00000000000000000000000000000')
        else:
            print('00000000000000000000000000000\nImpossível realizar transferência!\n00000000000000000000000000000')
    elif escolha==4:
        Conta.listar_contas()
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