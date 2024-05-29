from yahtzee import YahtzeeGame
from die import Die
import pytest

def test_is_yahtzee_when_all_dice_match():
    # Skapar ett Yahtzee-spel och sätter alla tärningars värde till 6.
    yahtzee = YahtzeeGame()
    yahtzee.dice = [Die() for _ in range(5)]
    for die in yahtzee.dice:
        die.value = 6
    # Kontrollerar om det är Yahtzee.
    assert yahtzee.is_yahtzee() == True

def test_is_not_yahtzee_when_dice_do_not_match():
    # Skapar ett Yahtzee-spel och sätter alla tärningars värde till 6, förutom den första tärningen som får värdet 2.
    yahtzee = YahtzeeGame()
    yahtzee.dice = [Die() for _ in range(5)]
    for die in yahtzee.dice:
        die.value = 6
    yahtzee.dice[0].value = 2
    # Kontrollerar att det inte är Yahtzee.
    assert yahtzee.is_yahtzee() == False

