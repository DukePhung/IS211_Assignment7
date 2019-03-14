import random


def addPlayers(players):

    for num in range(players):
        name = 'player' + str(num+1)
        player_list.append(name)


class Dice:
    def roll_dice(self):
        return random.randint(1, 6)

    def add_score(self, turntotal):
        self.score += turntotal


class Player(Dice):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __repr__(self):
        return '{} has a total score of {}.'.format(self.name, str(self.score))


num = int(input('Please enter the number of players: '))
player_list = []  # list to hold players as a string.
object_player = []  # this list is used to hold players object after instantiation
addPlayers(num)

for items in player_list:
    players = Player(items)
    object_player.append(players)

winner = True

while winner:

    for players in object_player:  # iterating through list of instantiated players of the Player class
        choice = 'r'
        turn_total = 0
        print(players)
        while choice != 'h':
            die = Dice()
            face_number = die.roll_dice()
            if face_number == 1:
                print('{} rolled a 1 and lost the turn.'.format(players.name))
                turn_total = 0
                break

            elif 1 < face_number <= 6:
                turn_total += face_number
                print('{} rolled a {}, and turn total is {}'.format(players.name, face_number, turn_total))

                choice = input("Enter 'r' to roll or 'h' to hold: ")

        players.add_score(turn_total)
        print(players, '\n')

        if players.score >= 100:
            print(players.name, 'has won the game with a score of', players.score)
            winner = False
            break
