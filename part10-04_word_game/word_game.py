# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2

class MostVowels(WordGame):
    def __init__(self, round: int):
        super().__init__(round)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = 'aeiou'
        p1_v = 0
        p2_v = 0
        for letter in player1_word:
            if letter.lower() in vowels:
                p1_v += 1
        for letter in player2_word:
            if letter.lower() in vowels:
                p2_v += 1

        if p1_v > p2_v:
            return 1
        elif p1_v < p2_v:
            return 2

class RockPaperScissors(WordGame):
    def __init__(self, round: int):
        super().__init__(round)

    def round_winner(self, player1_word: str, player2_word: str):
        hand = ['rock', 'paper', 'scissors']
        if player1_word not in hand and player2_word not in hand:
            return
        elif player1_word not in hand:
            return 2
        elif player2_word not in hand:
            return 1
        
        if (player1_word == 'rock' and player2_word == 'scissors') or (player1_word == 'paper' and player2_word == 'rock') or (player1_word == 'scissors' and player2_word == 'paper'):
            return 1
        elif (player2_word == 'rock' and player1_word == 'scissors') or (player2_word == 'paper' and player1_word == 'rock') or (player2_word == 'scissors' and player1_word == 'paper'):
            return 2

if __name__ == "__main__":
    p = RockPaperScissors(1)
    p.play()


    def round_winner(self, player1_word: str, player2_word: str):
        choices = {"rock" : 0, "paper": 1, "scissors": 2}
        if player1_word not in choices.keys() and player2_word not in choices.keys():
            return 0
        if player1_word not in choices.keys():
            return 2
        if player2_word not in choices.keys():
            return 1
        difference = choices[player1_word] - choices[player2_word]
        if difference == 0:
            return 0
        if difference == 1 or difference == -2:
            return 1 
        return 2