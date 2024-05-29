import random

class BoardGameMaterial:
    """Used to store all board game materials in one class"""
    pass

class Die(BoardGameMaterial):
    def __init__(self):
        # Sätter ett initialt värde för tärningen vid instansiering.
        self.value = random.randint(1, 6)
        
    def __str__(self):
        # Returnerar en strängrepresentation av tärningens värde.
        return "Dice shows " + str(self.value)
    
    @staticmethod
    def DieRoll():
        # Genererar ett slumpmässigt värde för tärningen mellan 1 och 6.
        return random.randint(1, 6)
    
    @staticmethod
    def die_reroll():
        # Kastar om tärningen.
        return Die.DieRoll()
