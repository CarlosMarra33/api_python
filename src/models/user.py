from src.models.endereco import Endereco


class User:
    def __init__(self, name="", email="", password="", cpf="", cep=""):
        self.name = name
        self.email = email
        self.cpf = cpf
        self.cep = cep
        self.endereco = []

    def addendereco(self, endereco=Endereco()):
        self.endereco.append(endereco)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_cep(self):
        return self.cep

    def set_cep(self, cep):
        self.cep = cep

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco=Endereco()):
        self.endereco = endereco

    def print(self):
        for x in self.endereco:
            print(x)
