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
        senha =int(input('\nDigite sua senha: '))
        if Conta.atualizar_saldo_por_conta(cont, senha, deposit):
            print('\n******Depósito realizado com sucesso!******')
        else:
            print('\n******Erro! Impossível realizar depósito conta ou senha inválida!******')

    @classmethod
    def TED(self):
        cont_origem=int(input('\nConta de Origem: '))
        cont_destino=int(input('\nConta de Destino: '))
        senha =int(input('\nDigite sua senha: '))
        valor=float(input('\nValor a transferir: '))
        if Conta.tranfere_valor_entre_contas(cont_origem, senha,cont_destino,valor):
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
                novo_valor=conta.saldo*0.07
                setattr(conta,"saldo",conta.saldo+novo_valor)
                print('\nJuros créditados em conta!')
        else:
            print('\nConta inexistente!\n')

    @classmethod
    def buscar_conta(self):
        num_conta=int(input('Conta: '))
        conta = Conta.buscar_por_conta(num_conta)
        if conta:
            print('\nNome: {}\nCPF: {}\nConta: {}\nSaldo: {:.2f}\nStatus: {}'.format(conta.nome,conta.cpf,conta.num_conta,conta.saldo,conta.status))
        else:
            print('\nConta não localizada!')
        
