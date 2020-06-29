import os
os.system("clear")

class Board():
	
    def __init__(self):
        self.box = [" "," "," "," "," "," "," "," "," "," "]
    
    def display(self):
        print(" %s | %s | %s " %(self.box[1],self.box[2],self.box[3]))
        print("-----------")
        print(" %s | %s | %s " %(self.box[4],self.box[5],self.box[6]))
        print("-----------")
        print(" %s | %s | %s " %(self.box[7],self.box[8],self.box[9]))

    def update_box(self, box_no, player):
        if self.box[box_no] == " ":
            self.box[box_no] = player
    
    def is_winner(self, player):
        if self.box[1] == player and self.box[2] == player and self.box[3] == player:
            return True
        if self.box[4] == player and self.box[5] == player and self.box[6] == player:
            return True
        if self.box[7] == player and self.box[8] == player and self.box[9] == player:
            return True
        if self.box[1] == player and self.box[4] == player and self.box[7] == player:
            return True
        if self.box[2] == player and self.box[5] == player and self.box[8] == player:
            return True
        if self.box[3] == player and self.box[6] == player and self.box[9] == player:
            return True
        if self.box[1] == player and self.box[5] == player and self.box[9] == player:
            return True
        if self.box[3] == player and self.box[5] == player and self.box[7] == player:
            return True
        return False

    def is_tie(self):
        used_box = 0
        for cell in self.box:
            if cell != " ":
                used_box += 1

        if used_box == 9:
            return True
        else:
            return False

    def reset(self):
        self.box = [" "," "," "," "," "," "," "," "," "," "]

board = Board()

def head():
    print ("TIC TAC TOE\n")


def refresh():
    #clear the screen
    os.system("clear")

    #print the title
    head()

    #print the board
    board.display()
    
if __name__ == "__main__":
	
	board = Board()

	while True:
		refresh()

		#get x input
		x_choice = int(input("\nX) Please choose 1-9: "))

		#update board
		board.update_box(x_choice,"X")

		#refresh screen
		refresh()

		#check for x win
		if board.is_winner("X"):
			print("\nX wins")
			play_again = str(input("\nDo you like to play again? (Y/N) :")).upper()
			if play_again == "Y":
				board.reset()
				continue
			else:
				break
		
		#check for tie
		if board.is_tie():
			print("\nTie Game")
			play_again = str(input("\nDo you like to play again? (Y/N) :")).upper()
			if play_again == "Y":
				board.reset()
				continue
			else:
				break

		#get o input
		o_choice = int(input("\nO) Please choose 1-9: "))

		#update board
		board.update_box(o_choice,"O")

		#check for o win
		if board.is_winner("O"):
			print("\nO wins")
			play_again = str(input("\nDo you like to play again? (Y/N) :")).upper()
			if play_again == "Y":
				board.reset()
				continue
			else:
				break

		#check for tie
		if board.is_tie():
			print("\nTie Game")
			play_again = str(input("\nDo you like to play again? (Y/N) :")).upper()
			if play_again == "Y":
				board.reset()
				continue
			else:
				break
