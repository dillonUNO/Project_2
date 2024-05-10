from PyQt6.QtWidgets import *
from gui import *
import random

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        '''
        Initializes the conditions for a regulation blackjack game
        '''
        super().__init__()
        self.setupUi(self)
        self.lbl_end_of_game.setHidden(True)
        self.btn_replay.setHidden(True)
        self.btn_hit.clicked.connect(lambda : self.hit())
        self.btn_stay.clicked.connect(lambda : self.stay())
        self.btn_replay.clicked.connect(lambda : self.replay())
        self.J = 10
        self.Q = 10
        self.K = 10
        self.A = 11 or 1
        self.cards = [1, 1, 1, 1, 1, 1, 1, 1,
                      2, 2, 2, 2, 2, 2, 2, 2,
                      3, 3, 3, 3, 3, 3, 3, 3,
                      4, 4, 4, 4, 4, 4, 4, 4,
                      5, 5, 5, 5, 5, 5, 5, 5,
                      6, 6, 6, 6, 6, 6, 6, 6,
                      7, 7, 7, 7, 7, 7, 7, 7,
                      8, 8, 8, 8, 8, 8, 8, 8,
                      9, 9, 9, 9, 9, 9, 9, 9,
                      10, 10, 10, 10, 10, 10, 10, 10,
                      self.A, self.A, self.A, self.A, self.A, self.A, self.A, self.A,
                      self.J, self.J, self.J, self.J, self.J, self.J, self.J, self.J,
                      self.Q, self.Q, self.Q, self.Q, self.Q, self.Q, self.Q, self.Q,
                      self.K, self.K, self.K, self.K, self.K, self.K, self.K, self.K]
        self.you_cards = 2
        self.dealer_cards = 2
        self.player1_cards = 2
        self.player2_cards = 2
        self.player3_cards = 2
        self.player4_cards = 2
        self.player5_cards = 2
        self.player6_cards = 2
        self.you_score = 0
        self.dealer_score = 0
        self.player1_score = 0
        self.player2_score = 0
        self.player3_score = 0
        self.player4_score = 0
        self.player5_score = 0
        self.player6_score = 0
        x = random.choice(self.cards)
        self.you_score += x
        self.lbl_you_score.setText(f'Score: {self.you_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.dealer_score += x
        self.lbl_dealer_score.setText(f'Score: {self.dealer_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player1_score += x
        self.lbl_1_score.setText(f'Score: {self.player1_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player2_score += x
        self.lbl_2_score.setText(f'Score: {self.player2_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player3_score += x
        self.lbl_3_score.setText(f'Score: {self.player3_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player4_score += x
        self.lbl_4_score.setText(f'Score: {self.player4_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player5_score += x
        self.lbl_5_score.setText(f'Score: {self.player5_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player6_score += x
        self.lbl_6_score.setText(f'Score: {self.player6_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.you_score += x
        self.lbl_you_score.setText(f'Score: {self.you_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.dealer_score += x
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player1_score += x
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player2_score += x
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player3_score += x
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player4_score += x
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player5_score += x
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player6_score += x
        self.cards.remove(x)

    def hit(self) -> None:
        '''
        Sets up the conditions for the player, dealer, and NPCs to gain cards
        '''
        x = random.choice(self.cards)
        self.you_cards += 1
        self.you_score += x
        self.lbl_you_cards.setText(f'Card Count: {self.you_cards}')
        self.lbl_you_score.setText(f'Score: {self.you_score}')
        self.cards.remove(x)
        if self.dealer_score < 17:
            x = random.choice(self.cards)
            self.dealer_cards += 1
            self.dealer_score += x
            self.lbl_dealer_cards.setText(f'Card Count: {self.dealer_cards}')
            self.cards.remove(x)
        if self.player1_score < 16:
            x = random.choice(self.cards)
            self.player1_cards += 1
            self.player1_score += x
            self.lbl_1_cards.setText(f'Card Count: {self.player1_cards}')
            self.cards.remove(x)
        if self.player2_score < 17:
            x = random.choice(self.cards)
            self.player2_cards += 1
            self.player2_score += x
            self.lbl_2_cards.setText(f'Card Count: {self.player2_cards}')
            self.cards.remove(x)
        if self.player3_score < 18:
            x = random.choice(self.cards)
            self.player3_cards += 1
            self.player3_score += x
            self.lbl_3_cards.setText(f'Card Count: {self.player3_cards}')
            self.cards.remove(x)
        if self.player4_score < 19:
            x = random.choice(self.cards)
            self.player4_cards += 1
            self.player4_score += x
            self.lbl_4_cards.setText(f'Card Count: {self.player4_cards}')
            self.cards.remove(x)
        if self.player5_score < 20:
            x = random.choice(self.cards)
            self.player5_cards += 1
            self.player5_score += x
            self.lbl_5_cards.setText(f'Card Count: {self.player5_cards}')
            self.cards.remove(x)
        if self.player6_score < 21:
            x = random.choice(self.cards)
            self.player6_cards += 1
            self.player6_score += x
            self.lbl_6_cards.setText(f'Card Count: {self.player6_cards}')
            self.cards.remove(x)
        if self.you_score > 21:
            self.btn_hit.setEnabled(False)

    def stay(self) -> None:
        '''
        Sets up the conditions for the player to stay
        Dealer and NPCs are still able to acquire cards until conditions are met
        '''
        self.btn_hit.setEnabled(False)
        while self.dealer_score < 17:
            x = random.choice(self.cards)
            self.dealer_cards += 1
            self.dealer_score += x
            self.cards.remove(x)
        while self.player1_score < 16:
            x = random.choice(self.cards)
            self.player1_cards += 1
            self.player1_score += x
            self.cards.remove(x)
        while self.player2_score < 17:
            x = random.choice(self.cards)
            self.player2_cards += 1
            self.player2_score += x
            self.cards.remove(x)
        while self.player3_score < 18:
            x = random.choice(self.cards)
            self.player3_cards += 1
            self.player3_score += x
            self.cards.remove(x)
        while self.player4_score < 19:
            x = random.choice(self.cards)
            self.player4_cards += 1
            self.player4_score += x
            self.cards.remove(x)
        while self.player5_score < 20:
            x = random.choice(self.cards)
            self.player5_cards += 1
            self.player5_score += x
            self.cards.remove(x)
        while self.player6_score < 21:
            x = random.choice(self.cards)
            self.player6_cards += 1
            self.player6_score += x
            self.cards.remove(x)
        self.lbl_dealer_score.setText(f'Score: {self.dealer_score}')
        self.lbl_1_score.setText(f'Score: {self.player1_score}')
        self.lbl_2_score.setText(f'Score: {self.player2_score}')
        self.lbl_3_score.setText(f'Score: {self.player3_score}')
        self.lbl_4_score.setText(f'Score: {self.player4_score}')
        self.lbl_5_score.setText(f'Score: {self.player5_score}')
        self.lbl_6_score.setText(f'Score: {self.player6_score}')
        self.lbl_dealer_cards.setText(f'Card Count: {self.dealer_cards}')
        self.lbl_1_cards.setText(f'Card Count: {self.player1_cards}')
        self.lbl_2_cards.setText(f'Card Count: {self.player2_cards}')
        self.lbl_3_cards.setText(f'Card Count: {self.player3_cards}')
        self.lbl_4_cards.setText(f'Card Count: {self.player4_cards}')
        self.lbl_5_cards.setText(f'Card Count: {self.player5_cards}')
        self.lbl_6_cards.setText(f'Card Count: {self.player6_cards}')
        if (self.you_score <= 21) and (self.dealer_score > 21):
            self.lbl_end_of_game.setText(f'You win!')
            self.lbl_end_of_game.setHidden(False)
        elif (self.you_score > self.dealer_score) and (self.you_score <= 21):
            self.lbl_end_of_game.setText(f'You win!')
            self.lbl_end_of_game.setHidden(False)
        elif (self.you_score == self.dealer_score) and (self.you_score <= 21):
            self.lbl_end_of_game.setText(f'Tie.')
            self.lbl_end_of_game.setHidden(False)
        else:
            self.lbl_end_of_game.setText(f'You lose.')
            self.lbl_end_of_game.setHidden(False)
        self.btn_replay.setHidden(False)
    def replay(self) -> None:
        '''
        Resets the blackjack game to initial conditions
        '''
        self.btn_hit.setEnabled(True)
        self.lbl_end_of_game.setHidden(True)
        self.cards = [1, 1, 1, 1, 1, 1, 1, 1,
                      2, 2, 2, 2, 2, 2, 2, 2,
                      3, 3, 3, 3, 3, 3, 3, 3,
                      4, 4, 4, 4, 4, 4, 4, 4,
                      5, 5, 5, 5, 5, 5, 5, 5,
                      6, 6, 6, 6, 6, 6, 6, 6,
                      7, 7, 7, 7, 7, 7, 7, 7,
                      8, 8, 8, 8, 8, 8, 8, 8,
                      9, 9, 9, 9, 9, 9, 9, 9,
                      10, 10, 10, 10, 10, 10, 10, 10,
                      self.A, self.A, self.A, self.A, self.A, self.A, self.A, self.A,
                      self.J, self.J, self.J, self.J, self.J, self.J, self.J, self.J,
                      self.Q, self.Q, self.Q, self.Q, self.Q, self.Q, self.Q, self.Q,
                      self.K, self.K, self.K, self.K, self.K, self.K, self.K, self.K]
        self.you_cards = 2
        self.dealer_cards = 2
        self.player1_cards = 2
        self.player2_cards = 2
        self.player3_cards = 2
        self.player4_cards = 2
        self.player5_cards = 2
        self.player6_cards = 2
        self.you_score = 0
        self.dealer_score = 0
        self.player1_score = 0
        self.player2_score = 0
        self.player3_score = 0
        self.player4_score = 0
        self.player5_score = 0
        self.player6_score = 0
        self.lbl_dealer_cards.setText(f'Card Count: {self.dealer_cards}')
        self.lbl_you_cards.setText(f'Card Count: {self.you_cards}')
        self.lbl_1_cards.setText(f'Card Count: {self.player1_cards}')
        self.lbl_2_cards.setText(f'Card Count: {self.player2_cards}')
        self.lbl_3_cards.setText(f'Card Count: {self.player3_cards}')
        self.lbl_4_cards.setText(f'Card Count: {self.player4_cards}')
        self.lbl_5_cards.setText(f'Card Count: {self.player5_cards}')
        self.lbl_6_cards.setText(f'Card Count: {self.player6_cards}')
        x = random.choice(self.cards)
        self.you_score += x
        self.lbl_you_score.setText(f'Score: {self.you_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.dealer_score += x
        self.lbl_dealer_score.setText(f'Score: {self.dealer_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player1_score += x
        self.lbl_1_score.setText(f'Score: {self.player1_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player2_score += x
        self.lbl_2_score.setText(f'Score: {self.player2_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player3_score += x
        self.lbl_3_score.setText(f'Score: {self.player3_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player4_score += x
        self.lbl_4_score.setText(f'Score: {self.player4_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player5_score += x
        self.lbl_5_score.setText(f'Score: {self.player5_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player6_score += x
        self.lbl_6_score.setText(f'Score: {self.player6_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.you_score += x
        self.lbl_you_score.setText(f'Score: {self.you_score}')
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.dealer_score += x
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player1_score += x
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player2_score += x
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player3_score += x
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player4_score += x
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player5_score += x
        self.cards.remove(x)
        x = random.choice(self.cards)
        self.player6_score += x
        self.cards.remove(x)
        self.btn_replay.setHidden(True)
