import numpy as np 

class Bingo:
    def __init__(self):
        self.boards = None
        self.marks = None
        self.win_board_idx = None
        self.bingo_loser_array = None
        self.numbers = None
        
    def load_bingo_file(self,filename):
        with open(filename) as f:
            # Get bingo numbers on first line
            self.numbers = np.array(list(map(int,f.readline().split(','))))
            # Read bingo boards on remaining lines
            board_string = f.read()
        board_list = board_string[1:-1].split('\n\n') # Split each board into string, separated by double \n
        # Convert board_list to 3d int array
        num_boards = len(board_list)
        self.boards = np.zeros((num_boards,5,5))
        for board_idx,board in enumerate(board_list):
            for line_idx,line in enumerate(board.split('\n')):
                line_vals = np.array(list(map(int,line.split())))
                self.boards[board_idx,line_idx,:] = line_vals
        
    def play(self, win_condition):
        self.marks = np.zeros_like(self.boards,dtype=bool)        
        for bingo_number in self.numbers:
            self.update_boards(bingo_number)
            if self.check_bingo_win(win_condition):
               idx = self.win_board_idx
               winning_board_marks = self.marks[idx]
               winning_board = self.boards[idx]
               # Return final score: unmarked numbers * number just called
               return int(np.sum(winning_board[~winning_board_marks])*bingo_number)
        
    def check_bingo_win(self,win_condition):

        def board_win(board_marks):
             col_vals = np.all(board_marks,axis=0) # column streaks
             row_vals = np.all(board_marks,axis=1) # row streaks
             return (np.any(col_vals) or np.any(row_vals))
        # PART 1 WIN CONDTION
        if win_condition == 'first':
            for board_idx, board_marks in enumerate(self.marks):
                if board_win(board_marks):
                    self.win_board_idx = board_idx
                    return True
        # PART 2 WIN CONDITION
        if win_condition == 'last':
            # Wait for when last remaining player wins
            if np.sum(self.bingo_loser_array) == 1:
                if board_win(self.marks[self.bingo_loser_array,:,:]):
                    # Get number of losing player
                    self.win_board_idx = int(np.argwhere(self.bingo_loser_array))
                    return True
            else:
                # Return True for all the players who havent won
                self.bingo_loser_array = [not(board_win(m)) for m in self.marks]
                return False
        
    def update_boards(self,number):
        # Add locations that match number to prexisting marks
        self.marks = self.marks | (self.boards == number)
        return  self.marks
    
    


#numbers, boards = load_bingo_file('../data/bingo')
bingo = Bingo()
bingo.load_bingo_file('../data/bingo')
# PART 1
print(bingo.play('first'))
# PART 2
print(bingo.play('last'))