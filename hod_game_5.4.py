import random

 # This is a code for the game tic tac toe
 # Written by:Hod A.
 # Date: 5 April 2020

class Board:
    """
    controlling game board dictionary
    """

    def __init__(self):
        """
        initialize game board with dictionary of Num Pad numbers positions.
        """
        self.game_board = {
            1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '
        }

    def print_board(self):#משתנה self
        """
        printing game board by Num Pad format

        """
        print(self.game_board[7] + ' | ' + self.game_board[8] + ' | ' + self.game_board[9])
        print('---------')
        print(self.game_board[4] + ' | ' + self.game_board[5] + ' | ' + self.game_board[6])
        print('---------')
        print(self.game_board[1] + ' | ' + self.game_board[2] + ' | ' + self.game_board[3])
        print()

    def insert_move(self, position, player_sign):
        """
        inserting move by position and sign to the game board
        :param position: int
        :param player_sign: str
        """
        self.game_board[position] = player_sign

    def is_possible_moves(self, position):
        """
        checking if move position is free on board
        :param position: int
        :return: bool
        """
        if self.game_board[position] == ' ':
            return True
        else:
            return False


class Player:
    def __init__(self, sign, name='', is_computer=False):
        """
        initialize player object of type human or computer
        :param sign: str
        :param name: str
        :param is_computer: bool
        """
        self.name = name
        self.sign = sign
        self.is_computer = is_computer
        self.score = 0

    def get_name(self):
        """
        ask user for name
        """
        name = input(f'Type player name for {self.sign}: ')
        self.name = name.capitalize()

    @staticmethod
    def comp_player(board):
        """
        computer algorithm for making moves
        :param board: dict
        :return: int
        """
        possible_moves = []
        for (index, sign) in board.items():
            if sign == ' ':
                possible_moves.append(index)

        for player_sign in ['O', 'X']:
            for move in possible_moves:
                board_copy = board.copy()
                board_copy[move] = player_sign
                if Move.is_winner(board_copy, player_sign) is True:
                    return move

        corners_open = []
        for move in possible_moves:
            if move in [1, 3, 7, 9]:
                corners_open.append(move)

        if len(corners_open) > 0:
            selected_corner = random.choice(corners_open)
            return selected_corner

        if 5 in possible_moves:
            return 5

        edges_open = []
        for move in possible_moves:
            if move in [2, 4, 6, 8]:
                edges_open.append(move)

        if len(edges_open) > 0:
            selected_edge = random.choice(edges_open)
            return selected_edge


class Move:
    @staticmethod
    def choose_move(player_name):
        """
        asking for user to choose his next move
        :param player_name: str
        :return: int
        """
        while True:
            try:
                move = int(input(f'{player_name} choose move from 1-9:'))
                if 1 <= move <= 9:
                    return move
                else:
                    print('Please enter valid move (1-9) !')
            except:
                print('Invalid input, try again (1-9) !')

    @staticmethod
    def is_winner(board, player_sign):
        """
        checking if there is a combination of winning on board
        :param board: dict
        :param player_sign: str
        :return: bool
        """
        if board[1] == player_sign and board[2] == player_sign and board[3] == player_sign:
            return True
        if board[4] == player_sign and board[5] == player_sign and board[6] == player_sign:
            return True
        if board[7] == player_sign and board[8] == player_sign and board[9] == player_sign:
            return True
        if board[7] == player_sign and board[5] == player_sign and board[3] == player_sign:
            return True
        if board[1] == player_sign and board[5] == player_sign and board[9] == player_sign:
            return True
        if board[1] == player_sign and board[4] == player_sign and board[7] == player_sign:
            return True
        if board[2] == player_sign and board[5] == player_sign and board[8] == player_sign:
            return True
        if board[3] == player_sign and board[6] == player_sign and board[9] == player_sign:
            return True
        else:
            return False

    @staticmethod
    def choose_random_move():
        """
        choosing random move on board for computer first move
        :return: int
        """
        moves = range(1, 10)
        return random.choice(moves)


class Game:
    """
    Main class for managing the game
    """

    def __init__(self):
        self.my_board = Board()
        self.player_1 = None
        self.player_2 = None
        self.to_continue = True

    def get_players(self, game_type):
        """
        get game type 1 or 2 (comp vs human OR human vs human) and create players.
        :param game_type: int
        """
        if game_type == 1:
            self.player_1 = Player(sign='X')
            self.player_2 = Player(name='Computer', sign='O', is_computer=True)
        else:
            self.player_1 = Player(sign='O')
            self.player_2 = Player(sign='X')

    @staticmethod
    def print_results(player1, player2):
        """
        print the results of the game per player.
        :param player1: Player 1 Object
        :param player2: Player 2 Object
        """
        print(f'{player1.name} - {player1.score}\n'
              f'{player2.name} - {player2.score}\n')

    @staticmethod
    def main_menu():
        """
        print menu options and get user selected option
        :return: int
        """
        print()
        print('Select option from menu:')
        print('1. Human Vs Computer ')
        print('2. Human Vs Human ')
        print()

        while True:
            try:
                option = int(input('Type your choice: '))
                if option in [1, 2]:
                    return option
                else:
                    print('Option not in menu, try again (1-2) !')
            except:
                print('Invalid input, try again (1-2) !')

    def take_main_menu_action(self, option_choose):
        """
        take action on user selected option from menu
        :param option_choose: int
        """
        if option_choose == 1:
            self.get_players(game_type=1)
            self.player_1.get_name()

        elif option_choose == 2:
            self.get_players(game_type=2)
            self.player_1.get_name()
            self.player_2.get_name()


    @staticmethod
    def in_game_menu():
        """
        print in-game menu options and get user selected option
        :return: int
        """
        print()
        print('Select option from menu:')
        print('1. Show Results And Continue ')
        print('2. Exit to main menu And New Game')
        print('3. Quit Game ')
        print()

        while True:
            try:
                option = int(input('Type your choice: '))
                if option in [1, 2, 3]:
                    return option
                else:
                    print('Option not in menu, try again (1-3) !')
            except:
                print('Invalid input, try again (1-3) !')

    def take_in_game_menu_action(self, option_choose):
        """
        take action on user selected option from in-game menu
        :param option_choose: int
        """
        if option_choose == 1:
            self.print_results(self.player_1, self.player_2)
            self.my_board = Board()

        elif option_choose == 2:
            print('---------------------------------\n\n')
            self.my_board = Board()
            option_chose = self.main_menu()
            self.take_main_menu_action(option_chose)

        elif option_choose == 3:
            self.to_continue = False

        return

    def choose_random_first_player_to_start(self):
        """
        Flip coin for choosing player to start the game.
        :return: Player Object
        """
        players = [self.player_1, self.player_2]
        return random.choice(players)

    def get_comp_move(self, game_round):
        """
        get computer move.
        :param game_round: int
        :return: int
        """
        if game_round == 1:
            position_move = Move.choose_random_move()
        else:
            position_move = self.player_2.comp_player(self.my_board.game_board)

        print('Computer made a move\n')
        return position_move

    def get_human_move(self, player_name):
        """
        get human move.
        :param player_name: str
        :return: int
        """
        while True:
            position_move = Move.choose_move(player_name)
            if self.my_board.is_possible_moves(position_move) is True:
                break
            else:
                print('Position is taken, choose other!\n')

        return position_move

    def run(self):
        """
        main function for game running.

        """
        print('Welcome to Hod\'s Tic Tac Toc Game :)')
        print('The board is built like the Num Pad. for example, 9 is the upper right cell.\n')

        option_choose = self.main_menu()
        self.take_main_menu_action(option_choose)

        while self.to_continue is True:
            player_turn = self.choose_random_first_player_to_start()
            print(f'Let\'s play, {player_turn.name} begin...\n')

            if player_turn.is_computer is False:
                self.my_board.print_board()

            for game_round in range(1, 10):

                if player_turn.is_computer is True:
                    position_move = self.get_comp_move(game_round)

                else:
                    position_move = self.get_human_move(player_turn.name)

                self.my_board.insert_move(position_move, player_turn.sign)
                self.my_board.print_board()

                if Move.is_winner(self.my_board.game_board, player_turn.sign) is True:
                    print(f'{player_turn.name} is the winner!!!\n')
                    player_turn.score += 2
                    option_choose = self.in_game_menu()
                    self.take_in_game_menu_action(option_choose)
                    print()
                    break

                elif game_round == 9:
                    print('It\'s a tie.\n')
                    self.player_1.score += 1
                    self.player_2.score += 1
                    option_choose = self.in_game_menu()
                    self.take_in_game_menu_action(option_choose)
                    print()


                else:
                    if player_turn == self.player_1:
                        player_turn = self.player_2
                    else:
                        player_turn = self.player_1

        print('Bye :)')


if __name__ == '__main__':
    tic_tac_toe = Game()
    tic_tac_toe.run()