
from enums import CartaEfeito, CartaNumerica
from modelos import Carta

class Baralho():
    def __init__(self):
        self.cartas = [
            Carta.criar(tipo) for tipo in (list(CartaNumerica) + list(CartaEfeito))
        ]

    def mostrar_cartas(self):
        return [str(carta) for carta in self.cartas]
    
    def obter_carta_por_tipo(self, tipo):
        for carta in self.cartas:
            if carta.tipo == tipo:
                return carta
        raise ValueError("Carta não encontrada no baralho.")
    
    def usar_carta(self, carta):
        if carta in self.cartas:            
            self.cartas.remove(carta)
        else:
            raise ValueError("Carta não está no baralho.")