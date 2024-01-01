from conta import Conta
from conta import Conta

class op_contas:

    @classmethod
    def cadastrar_conta(self):
        print('\nAbrindo conta....\n*******************************\n')
        cpf=int(input('Digite o CPF: '))
        nome=input('Digite seu nome: ')
        senha=int(input('Defina sua senha: '))
        num_conta=int(input('Número da conta: '))
        saldo=float(input('Valor do depósito inicial: '))
        status='ativo'
    
        conta=Conta(cpf,nome,senha,num_conta,saldo,status)

        print('\n*******************************')
        print('Conta aberta com sucesso!')
        print('*******************************')

    @classmethod
    def deposit(self):
        cont=int(input('\nConta: '))
        deposit=float(input('\nValor de depósito: '))
        if Conta.atualizar_saldo_por_conta(cont, deposit):
            print('\n******Depósito realizado com sucesso!******')

    @classmethod
    def TED(self):
        cont_origem=int(input('\nConta de Origem: '))
        cont_destino=int(input('\nConta de Destino: '))
        valor=float(input('\nValor a transferir: '))
        if Conta.tranfere_valor_entre_contas(cont_origem,cont_destino,valor):
            print('\n00000000000000000000000000000\nTransferência realizada com sucesso!\n00000000000000000000000000000')
        else:
            print('\n00000000000000000000000000000\nImpossível realizar transferência!\n00000000000000000000000000000')

    @classmethod
    def listar_contas(self):
        return Conta.listar_contas()


    @classmethod
    def render_juros_sob_saldo(self):
        num_conta=int(input('Conta: '))
        conta = Conta.buscar_por_conta(num_conta)
        if conta:
            if conta.saldo>0:
                novo_valor=conta.saldo*0.005
                conta.saldo+=novo_valor
                print('\nJuros créditados em conta!')
        else:
            print('\nConta inexistente!\n')
