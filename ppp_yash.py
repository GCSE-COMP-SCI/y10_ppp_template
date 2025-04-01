# MAIN MENU
def main_menu():
    print("MAIN MENU")
    call_instruct = input("Press 'I' to read the instructions OR to start the game press the spacebar.")
    instructions = ('''1. This game is known as Ultimate Tic Tac Toe. Player 1 can choose anywhere to start 
    2. Player 2 can make a move in any cell of the miniboard that corresponds to the square chosen by Player 1. 
    3. For example, if a move is made in bTR(Board-Top-Right) and the cell chosen on the miniboard is mBM(Miniboard-Bottom-Middle), Player 2 is obligated to make their move in bBM(Board-Bottom-Middle).''')

    if call_instruct == 'I':
        print(instructions)
        start_game_after_instruct = input("Press the spacebar to start the game")
    elif call_instruct == ' ':
        print("")
        
        
    

# Set up an empty board.  
    # To form a square of 9 empty 'mini-boards' with a following 9 cells inside each miniboard.  (List of cells in grid)  
    
    # Assign a position for each cell in a miniboard. 
        # (mTL = miniboard Top-left, mTM - miniboard Top-middle, mTR - miniboard Top-right) 
        # (When a PLAYER chooses their square and to confirm whether a PLAYER has won a miniboard) 
        
    # Assign a position for each miniboard in a board. 
        # (BTL = board Top-left, bTM - board Top-middle, bTR - board Top-right) 
        # (When a PLAYER can choose any square and to confirm whether a PLAYER has won.) 
         
# Prompt PLAYER 1 to make a move in any mini board. (Print function) 
    # Assign PLAYER 1 the symbol, ‘O’.  (Assignment) 
    # Assign PLAYER 2 the symbol, ‘X’.  (Assignment) 
    # Execute the move based on the position given. (Print function at: position given) 

# BEGIN LOOP

# The square chosen corresponds to the cell in the board the next PLAYER will have to make a move in next.  (IF, ELIF, ELSE)(List of cells used again) 
    # Swap to next PLAYER’s turn 
    # Prompt PLAYER  to make a move. (Print function) 
    # Execute the move based on the position given. (Print function at: position given)

# This is repeated until a cell is won... (WHILE loops) 
    # By forming 3 consecutive symbols (assigned to the respective PLAYER) in the miniboard.
        # Vertical, horizontal, diagonal (List of possible positions for winning) 
        # The program can recognise a cell in the board as won by: 
            # Checking if there are 3 consecutive symbols after every turn. (IF, ELIF, ELSE)(BOOLEANS)(List of possible positions for winning) 
    # Filling the entire cell with the won symbol and changing the colour to correspond.
    # If the cell chosen in the miniboard corresponds to a cell on the board that has already been won: 
        # The next PLAYER can make a move in a place of their choosing. (IF, ELIF, ELSE) 

# The game ends when a player has made their consecutive line of 3 symbols 
# Or in the event of a draw, where neither PLAYER makes their consecutive line of 3 symbols on the board.  

# (PROCESS CAN BE EXECUTED USING SUBROUTINES, WHERE THE FUNCTIONS AND PROCEDURES CAN SIMPLY BE CALLED)