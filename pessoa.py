class pessoa:
    __lista = []
    nome = ''
    rg = ''
    cpf = ''
    anonasc = 0
    mesnasc = 0
    dianasc = 0
    sexo = ''

    def cadastrarPessoa(self, nome, rg, cpf, anonasc, mesnasc, dianasc, sexo):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.anonasc = anonasc
        self.mesnasc = mesnasc
        self.dianasc = dianasc
        self.sexo = sexo

    def exibir(self):
        print(f'Nome: {self.nome}')
        print(f'RG:{self.rg}')
        print(f'CPF:{self.cpf}')
        print(f'DATA de Nascimento: {self.dianasc}/{self.mesnasc}/{self.anonasc}')
        print(f'Gênero:{self.sexo}')
