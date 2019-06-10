import pickle


class BancoDeDados:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def salvar(self, dados):
        pickle.dump(dados, open(self.arquivo, "ab"))

    def listar(self):
        dados = pickle.load(open(self.arquivo, "rb"))
        return dados

    def atualizar(self, dados):
        pickle.dump(dados, open(self.arquivo, "wb"))