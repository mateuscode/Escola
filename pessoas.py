class pessoa:
    nome = ""
    cpf = ""
    rg = ""
    def cadastrarPessoa(self):
        self.nome = input("Nome:")
        self.cpf = input("Cpf:")
        self.rg = input("Rg:")
    def listarPessoa(self):
        print(self.nome)
        print(self.cpf)
        print(self.rg)