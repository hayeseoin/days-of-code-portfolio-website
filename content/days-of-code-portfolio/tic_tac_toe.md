---
title: Tic Tac Toe
tags:
  - Scripting
github: https://github.com/hayeseoin/days-of-code-84.git
---
# Tic Tac Toe

A terminal, text based versino of Tic Tac Toe.

It's been a while since I did the opening modules of the course where we made terminal games, so this was more challenging than expected. 

I made a list of lists for the board, and mapped each to a digit between 1 and 9 with a dictionary of tuples. Initially I had been inputting the rows and columns seperately, but this was not user friendly. The pieces are also mapped with a dictionary. 

I wrapped everything in a class called Game(). It was good to work with a class, as I'm not as comfortable creating classes as I am functions. 

I wondered how to check the win condition. Then I realised I could just define all of the win conditions, as there are only 8 of them, and then check each one at the end of every turn. 

---
    #!python
    import os

    class Game:
        def __init__(self) -> None:
            self.board: list[list[int]] = [
        [0,0,0],[0,0,0],[0,0,0]
        ]
            self.mappings: dict = {
                1:[0,0],2:[0,1],3:[0,2],
                4:[1,0],5:[1,1],6:[1,2],
                7:[2,0],8:[2,1],9:[2,2],
            }

            self.pieces = {0: ' ', 1:'x', 2:'o'}
            self.turn_count: int = 0
            self.is_won = False
            self.winning_piece = None
            
        def play(self, message = 'Game on!') -> None:
            os.system('clear')
            print(message)
            self.build_board()
            self.play_piece()
            self.check_win()
            self.check_draw()

        def play_piece(self) -> None:
            if not self.turn_count % 2:
                piece = 1
            else:
                piece = 2
            print(f"It's {self.pieces[piece]}'s turn.")

            self.place = input('Where are you placing your piece?: ')
            try:
                placement = int(self.place)
                position = self.mappings[placement]
            except ValueError:
                self.play("Please enter a valid key.")
            except KeyError:
                self.play('Key out of range')
    
            if placement not in range(1,10):
                self.play('Please choose valid position.')

            if self.board[position[0]][position[1]] != 0:
                self.play('This piece has already been played.')

            self.board[position[0]][position[1]] = piece
            self.turn_count += 1

        def build_board(self) -> None:
            rows = [i for i in self.board]
            map = 1
            for row in rows:
                row_pieces = [self.pieces[i] for i in row]
                print('|'.join(row_pieces) + '    ' + f'{map}|{map+1}|{map+2}')
                map += 3
            
        def check_draw(self) -> None:
            if self.turn_count >= 9:
                os.system('clear')
                print("It's a draw!")
                self.build_board()
                print("Too bad!")
                self.is_won = True
                input()
                os.system('clear')
        

        def check_win(self) -> None:
            self.win_conditions = [
                self.board[0],
                self.board[1],
                self.board[2],
                [self.board[0][0], self.board[1][0],self.board[2][0]],
                [self.board[0][1], self.board[1][1],self.board[2][1]],
                [self.board[0][2], self.board[1][2],self.board[2][2]],
                [self.board[0][0], self.board[1][1],self.board[2][2]],
                [self.board[0][2], self.board[1][1],self.board[2][0]],
            ]
            for position in self.win_conditions:
                if position[0] == position[1] and position[1] == position[2]:
                    if position[0] != 0:
                        self.is_won = True
                        self.winning_piece = position[0]
                        self.declare_winner()
        
        def declare_winner(self) -> None:
            print(f"{self.pieces[self.winning_piece]} wins!")
            input()
            os.system('clear')

    def main():
        game = Game()
        while not game.is_won:
            game.play()

    if __name__ == "__main__":
        main()
