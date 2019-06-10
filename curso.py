

class curso:
    valor = 865.23
    numMinAluno = 0.0

    def __int__(self):
        self.titulo = ''
        self.descricao = ''
        self.sala = ''

    def cadastrarCurso(self, desconto):
        self.titulo = input('Titulo do curso: ')
        self.descricao = input('Descrição do curso: ')
        self.sala = input('Sala: ')
        self.desconto = desconto
        self.valor = self.valor - self.desconto
    def exibirCurso(self):
        print(f'Curso: {self.titulo}')
        print(f'Descriçãp: {self.descricao}')
        print(f'Valor: {self.valor}')
        print(f'Sala: {self.sala}')

    def calcNumMinAluno(self, nivel):
        if nivel == 'I':
            self.numMinAluno = 6500.00 / 865.23
        elif nivel == 'II':
            self.numMinAluno = 8325.50 / 865.23
        elif nivel == 'III':
            self.numMinAluno = 12568.43 / 865.23


        return self.numMinAluno



