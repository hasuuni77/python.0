from die import Die

class YahtzeeGame:
    def __init__(self):
        self.keep_playing = True
        self.start_game()

    def start_game(self):
        # Välkomstmeddelande när spelet startar.
        print("Welcome to Yahtzee!")
        while self.keep_playing:
            self.play_round()

    def play_round(self):
        # Skapar fem nya tärningar för en ny omgång.
        self.dice = [Die() for _ in range(5)]
        for turn in range(3):
            print(f"\nStarting turn: {turn + 1} of 3, rolling dice")
            self.roll_dice()
            self.show_dice()
            if self.is_yahtzee():
                print(f"\nCongratulations! You got YAHTZEE with {self.dice[0].value}'s!")
                break
            if turn < 2:
                if not self.ask_to_roll_again():
                    break
            else:
                if not self.ask_to_play_again():
                    break

    def roll_dice(self):
        # Kastar alla tärningar.
        for die in self.dice:
            die.value = Die.DieRoll()

    def show_dice(self):
        # Visar värdena på tärningarna efter kastet.
        for i, die in enumerate(self.dice):
            print(f"{i}: {die}")

    def is_yahtzee(self):
        # Kontrollerar om alla tärningar har samma värde.
        first_value = self.dice[0].value
        if all(die.value == first_value for die in self.dice):
            print("Yahtzee!")
            return True
        else:
            print("Not a Yahtzee.")
            return False

    def ask_to_roll_again(self):
        # Frågar spelaren om de vill kasta tärningarna igen.
        response = input("Want to throw again? (y for yes, anything else for no): ").lower()
        return response == 'y'

    def ask_to_play_again(self):
        # Frågar spelaren om de vill spela en ny omgång.
        response = input("Game over! Want to play again? (y for yes, anything else for no): ").lower()
        if response != 'y':
            self.keep_playing = False
        return response == 'y'

def main():
    # Skapar en instans av YahtzeeGame när programmet körs.
    YahtzeeGame()

if __name__ == '__main__':
    main()
