from src.models.endereco import Endereco
class User():
    def __init__(self, name='', email='', password='', cpf='', cep=''):
        self._name = name
        self._email = email
        self._cpf = cpf
        self._cep = cep
        self._endereco = []
    
    def add_endereco(self, endereco=Endereco()):
        self._endereco.append(endereco)


    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_email(self):
        return self._email
    def set_email(self, email):
        self._email = email
    def get_cpf(self):
        return self._cpf
    def set_cpf(self, cpf):
        self._cpf = cpf
    def get_cep(self):
        return self._cep
    def set_cep(self,cep):
        self._cep = cep
    def get_endereco(self):
        return self._endereco
    def set_endereco(self, endereco=Endereco()):
        self._endereco = endereco


    def print(self):
        for x in self._endereco:
            print(x)