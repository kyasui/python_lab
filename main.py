"""Rock Paper Scissors"""
from random import randint


class Player:
  def __init__(self, is_human=False):
    self.is_human = is_human
  def play(self):
    if self.is_human == False:
      return randint(0,2)
    else:
      recognized_input = False

      while recognized_input == False:
        play = raw_input('ROCK, PAPER or SCISSORS? ')
        play = play.lower()

        if play == 'rock':
          recognized_input = True
          return 0
        elif play == 'paper':
          recognized_input = True
          return 1
        elif play == 'scissors':
          recognized_input = True
          return 2
        else:
          print('Unrecognized play... Try again...')


class Game:
  def __init__(self, player_one, player_two):
    self.player_one = player_one
    self.player_two = player_two
    self.choices = {
      0: 'Rock',
      1: 'Paper',
      2: 'Scissors',
    }
  def start(self):
    winner = False

    while winner == False:
      player_one_score = self.player_one.play()
      player_two_score = self.player_two.play()

      if player_one_score != player_two_score:
        print 'Player One chose ' + self.choices[player_one_score]
        print 'Player Two chose ' + self.choices[player_two_score]
        result = self.determine_winner(self.choices[player_one_score], self.choices[player_two_score])
        print(result)
        winner = True

        playagain = raw_input('Play Again? Y/N ').lower()

        if (playagain == 'y'):
          self.start()
      else:
        print 'Tie, Go Again.'
  def determine_winner(self, player_one_play, player_two_play):
    if player_one_play == 'Rock':
      if player_two_play == 'Paper':
        return 'Player One Loses!'
      elif player_two_play == 'Scissors':
        return 'Player One Wins!'
    elif player_one_play == 'Scissors':
      if player_two_play == 'Rock':
        return 'Player One Loses!'
      elif player_two_play == 'Paper':
        return 'Player One Wins!'
    elif player_one_play == 'Paper':
      if player_two_play == 'Scissors':
        return 'Player One Loses!'
      elif player_two_play == 'Rock':
        return 'Player One Wins!'


if __name__ == '__main__':
  game = Game(Player(is_human=True), Player(is_human=False))
  game.start()