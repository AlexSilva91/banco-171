class Conta:
    contas_cadastradas =[]
    def __init__(self,cpf,nome,senha,num_conta,saldo,status):
        self.cpf=cpf
        self.nome=nome
        self.senha=senha
        self.num_conta=num_conta
        self.saldo=saldo
        self.status=status
        Conta.contas_cadastradas.append(self)

    
    def apresentar(self):
        return '\nNome: {}\nCPF: {}\nConta: {}\nSaldo: {:.2f}\nStatus: {}'.format(self.nome, self.cpf,self.num_conta,self.saldo,self.status)
    
    @classmethod
    def listar_contas(cls):
        for conta in cls.contas_cadastradas:
            print(conta.apresentar())

    @classmethod
    def buscar_por_conta(cls, num_conta):
        for conta in cls.contas_cadastradas:
            if conta.num_conta == num_conta:
                return conta
        return None
    
    @classmethod
    def atualizar_saldo_por_conta(cls, conta, senha,deposit):
        c = cls.buscar_por_conta(conta)
        if c.senha == senha:
            if c:
                c.saldo += deposit
                return True  # Atualização bem-sucedida
            return False  # Pessoa não encontrada
    
    @classmethod
    def tranfere_valor_entre_contas(cls, origem, senha, destino, valor):
        conta_origem=cls.buscar_por_conta(origem)
        conta_destino=cls.buscar_por_conta(destino)
        if conta_origem.senha == senha:
            if conta_origem and conta_destino:
                if conta_origem.saldo>=valor:
                    conta_destino.saldo+=valor
                    conta_origem.saldo-=valor
                    return True
                else:
                    return False
        else:
            return False
        
