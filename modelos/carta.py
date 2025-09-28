from enums import CartaEfeito, CartaNumerica

class Carta:
    def __init__(self, tipo):
        raise RuntimeError("Use o metodo 'criar' para instanciar uma carta.")
    
    def __new__(cls, *args, **kwargs):
        raise TypeError("Use o metodo 'criar' para instanciar uma carta.")

    @classmethod
    def criar(cls, tipo):
        if not isinstance(tipo, (CartaNumerica, CartaEfeito)):
            raise ValueError("Tipo não aceito de carta.")
        instancia = object.__new__(cls)
        instancia.tipo = tipo
        return instancia


    def aplicar(self, valor=None):
        if isinstance(self.tipo, CartaNumerica):
            return self.tipo.value
        elif isinstance(self.tipo, CartaEfeito):
            if valor is None:
                raise ValueError("Efeito precisa de um valor")
            if self.tipo == CartaEfeito.SOMA:
                return valor * 2
            elif self.tipo == CartaEfeito.SUBTRAIR:
                return abs(valor)
            elif self.tipo == CartaEfeito.MULTIPLICA:
                return valor * valor
            elif self.tipo == CartaEfeito.DIVIDE:
                if valor == 0:
                    raise ValueError("Não é possível dividir por zero.")
                return valor / 2
            
    def __str__(self):
        return f'Carta({self.tipo.name})'

