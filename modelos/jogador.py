from modelos.baralho import Baralho
from enums import CartaNumerica, CartaEfeito

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.baralaho = Baralho()

    def jogar_carta_numerica(self):
        carta = self.baralaho.obter_carta_por_tipo(CartaNumerica)       
        return carta.aplicar()
    
    def aplicar_efeito(self, valor):
        carta = self.baralaho.obter_carta_por_tipo(CartaEfeito)        
        return carta.aplicar(valor)