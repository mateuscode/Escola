from curso import curso


class matricula:
    id = 0
    mesMatricula = 0
    anoMatricula = 0
    qnt = 0
    curs = curso()

    def cadMatricula(self, desconto):
        self.id = int(input('ID: '))
        self.mesMatricula = int(input('Mes da Matricula: '))
        self.anoMatricula = int(input('Ano da matricula: '))
        self.curs.cadastrarCurso(desconto)

    def exibirMatricula(self):
        print("\n Matrícula \n")
        print(f'ID: {self.id}')
        print(f'Mês da Matricula: {self.mesMatricula}')
        print(f'Ano da Matricula: {self.anoMatricula}')
        self.curs.exibirCurso()