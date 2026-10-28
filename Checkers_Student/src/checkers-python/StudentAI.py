from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.
class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2
    def get_move(self,move):              # WAIT it says not to modify existing functions, but this is a random chooser?
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        index = randint(0,len(moves)-1)
        inner_index =  randint(0,len(moves[index])-1)
        move = moves[index][inner_index]
        self.board.make_move(move,self.color)
        return move

    # Functions to add:
    # - evaluate(self): looks at the current board state & returns score representing how good the position is for AI -- decide on heuristic
    # - minimax(self, board, depth, is_maximizing) — Minimax Search: recursively explore possible future moves up to a certain depth
    # - [maybe later] alpha_beta_pruning(self, board, depth, alpha, beta, is_maximizing) — optimization on top of Minimax
    
    # In get_move()... I think... :
    # Loop through all possible moves, simulate each one on a copy of the board, run minimax on each, and return the move with the best score