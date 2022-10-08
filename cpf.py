class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Iválido!")
       
    def valida_cpf(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False