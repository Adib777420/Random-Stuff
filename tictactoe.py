from itertools import combinations 
import random


magic_board = [8,3,4,1,5,9,6,7,2] 

flat_board = [1,2,3,4,5,6,7,8,9] 

def print_board():

    print(f"\n{flat_board[0]} | {flat_board[1]} | {flat_board[2]}")
    print("---------")
    print(f"{flat_board[3]} | {flat_board[4]} | {flat_board[5]}")
    print("---------")
    print(f"{flat_board[6]} | {flat_board[7]} | {flat_board[8]}\n")

def bot():
    target_O = "O"
    target_X = "X" 
    indices_O = [index for index, value in enumerate(flat_board) if value == target_O]
    indices_X = [index for index, value in enumerate(flat_board) if value == target_X]


    if len(indices_X) >= 2:

        for combo in combinations(indices_X, 2):
        
            total = sum(magic_board[index] for index in combo)
            needed_val = 15 - total
        
            if needed_val in magic_board:
                bot_move_index = magic_board.index(needed_val)
                
                if isinstance(flat_board[bot_move_index], int):
                    flat_board[bot_move_index] = "X"
                    return


    CORNERS = {0, 2, 6, 8}
    EDGES = [1, 3, 5, 7]

    if len(indices_O) == 2:
        if set(indices_O).issubset(CORNERS):
            
            available_edges = [idx for idx in EDGES if isinstance(flat_board[idx], int)]
            
            if available_edges:
                bot_move = random.choice(available_edges)
                
                if isinstance(flat_board, list):
                    flat_board[bot_move] = "X"
                    return


    if len(indices_O) >= 2:

        for combo in combinations(indices_O, 2):
        
            total = sum(magic_board[index] for index in combo)
            needed_val = 15 - total
        
            if needed_val in magic_board:
                bot_move_index = magic_board.index(needed_val)
                
                if isinstance(flat_board[bot_move_index], int):
                    flat_board[bot_move_index] = "X"
                    return
                
    if len(indices_O) == 1:

        if indices_O[0] == 4:
            flat_board[0] = "X"
            return
        else:
            flat_board[4] = "X" 
            return

                
    available_moves = [i for i, val in enumerate(flat_board) if isinstance(val, int)]
    if available_moves:
        bot_move_index = random.choice(available_moves)
        flat_board[bot_move_index] = "X"




def check_for_winner():

    target_O = "O"
    target_X = "X"

    indices_O = [index for index, value in enumerate(flat_board) if value == target_O]
    indices_X = [index for index, value in enumerate(flat_board) if value == target_X]

    if len(indices_O) >= 3:
        
        for combo in combinations(indices_O, 3):
        
            total = sum(magic_board[index] for index in combo)
            if total == 15:
                print("You win!")
                return True

    if len(indices_X) >= 3:
        
        for combo in combinations(indices_X, 3):
        
            total = sum(magic_board[index] for index in combo)
            if total == 15:
                print("Bot wins!") 
                return True

    return False


def board_is_full():
    return all(isinstance(val, str) for val in flat_board)


# main func (not unbeatable bot)
print_board()

while True:

    user_input = int(input("Select the box you want to place O in (1-9): "))

    while True:
        index = user_input - 1

        if isinstance(flat_board[index], int):
            flat_board[index] = "O" 
            print_board()  
            

            if not check_for_winner() and not board_is_full():
                print("Bot is thinking...")
                bot()                  
                print_board()  
            break

        else:
            user_input = int(input("This box is taken. Select another box: "))

    if check_for_winner():
        break

    elif board_is_full():
        print("It's a tie!")
        break
        
