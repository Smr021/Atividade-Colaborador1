
class Endereco:
    def __init__(self,logradouro:str,numero:str,complemento:str,cep:str,cidade:str) -> None:
        self.logradouro = self._verificar_logradouro(logradouro)
        self.numero = self._verificar_numero(numero)
        self.complemento = self._verificar_complemento(complemento)
        self.cep = self._verificar_cep(cep)
        self.cidade = self._verificar_cidade(cidade)

        
        
#'''Método para verificar o logradouro, numero, complemento, cep e cidade'''

    def _verificar_logradouro(self,valor):
        self._verificar_logradouro_tipo_invalido(valor)
        self._verificar_logradouro_vazio_invalido(valor)

        self.logradouro = valor
        return self.logradouro

    def _verificar_numero(self,valor):
        self._verificar_numero_vazio_invalido(valor)

        self.numero = valor
        return self.numero

    def _verificar_complemento(self,valor):
        self._verificar_complemento_tipo_invalido(valor)
        self._verificar_complemento_vazio_invalido(valor)

        self.complemento = valor
        return self.complemento

    def _verificar_cep(self,valor):
        self._verificar_cep_vazio_invalido(valor)

        self.cep = valor
        return self.cep

    def _verificar_cidade(self,valor):
        self._verificar_cidade_tipo_invalido(valor)
        self._verificar_cidade_vazio_invalido(valor)

        self.cidade = valor
        return self.cidade

#Metodos auxiliares.

    def _verificar_logradouro_tipo_invalido(self,valor):
        """"Método auxiliar para verificação do logradouro do tipo invalido."""
        if not isinstance (valor, str):
            raise TypeError("O logradouro deve ser um texto.")
        
    def _verificar_logradouro_vazio_invalido(self,valor):
        """Método auxiliar para verificação do logradouro  do tipo vazio."""
        if not valor.strip():
            raise TypeError("O logradouro não pode estar vazio.")

    def _verificar_numero_vazio_invalido(self,valor):
        """Método auxiliar para verificaçaõ do número do tipo vazio."""
        if not valor.strip():
            raise TypeError("O campo no número não pode estar vazio.") 

    def _verificar_complemento_tipo_invalido(self,valor):
        """Método auxiliar para verificação do complemento do tipo invalido."""
        if not isinstance (valor, str):
            raise TypeError("O complemento deve ser um texto.")

    def _verificar_complemento_vazio_invalido(self,valor):
        """Método auxiliar para verificação do complemento  do tipo vazio."""
        if not valor.strip():
            raise TypeError("O complemento não pode estar vazio.")

    def _verificar_cep_vazio_invalido(self,valor):
        """Método auxiliar para verificação do cep do tipo vazio."""                 
        if not valor.strip():
            raise TypeError("O cep não pode estar vazio.")
        
    def _verificar_cidade_tipo_invalido(self,valor):
        """Método auxiliar para verificação cidade do tipo invalido."""
        if not isinstance (valor, str):
            raise TypeError("O campo de cidade deve ter um texto.")  

    def _verificar_cidade_vazio_invalido(self,valor):
        """Método auxiliar para verificação cidade do tipo vazio """
        if not valor.strip(): 
            raise TypeError("O campo de cidade não pode estar vazia")
    