import itertools 
### Ascii art for introduction
introduction =  "\n\
______________________________________________________________________________________________________________________________\n\
 _    _        _                                 _            _____  _____  _____   _____   ___   _____   _____  _____  _____ \n\
| |  | |      | |                               | |          |_   _||_   _|/  __ \ |_   _| / _ \ /  __ \ |_   _||  _  ||  ___|\n\
| |  | |  ___ | |  ___   ___   _ __ ___    ___  | |_   ___     | |    | |  | /  \/   | |  / /_\ \| /  \/   | |  | | | || |__  \n\
| |/\| | / _ \| | / __| / _ \ | '_ ` _ \  / _ \ | __| / _ \    | |    | |  | |       | |  |  _  || |       | |  | | | ||  __| \n\
\  /\  /|  __/| || (__ | (_) || | | | | ||  __/ | |_ | (_) |   | |   _| |_ | \__/\   | |  | | | || \__/\   | |  \ \_/ /| |___ \n\
 \/  \/  \___||_| \___| \___/ |_| |_| |_| \___|  \__| \___/    \_/   \___/  \____/   \_/  \_| |_/ \____/   \_/   \___/ \____/ \n\
 _____                     _              _   _                                                                               \n\
/  __ \                   | |            | | | |                                                                              \n\
| /  \/ _ __   ___   __ _ | |_   ___   __| | | |__   _   _                                                                    \n\
| |    | '__| / _ \ / _` || __| / _ \ / _` | | '_ \ | | | |                                                                   \n\
| \__/\| |   |  __/| (_| || |_ |  __/| (_| | | |_) || |_| |                                                                   \n\
 \____/|_|    \___| \__,_| \__| \___| \__,_| |_.__/  \__, |                                                                   \n\
___  ___ _  _     _     _   _____        _      _     __/ |                _                                                  \n\
|  \/  |(_)| |   | |   (_) /  ___|      (_)    | |   |___/                | |                                                 \n\
| .  . | _ | | __| | __ _  \ `--.   ___  _   __| |  ___  _ __   ___   ___ | |__   _ __   _   _  _ __                          \n\
| |\/| || || |/ /| |/ /| |  `--. \ / _ \| | / _` | / _ \| '_ \ / __| / __|| '_ \ | '_ \ | | | || '__|                         \n\
| |  | || ||   < |   < | | /\__/ /|  __/| || (_| ||  __/| | | |\__ \| (__ | | | || | | || |_| || |                            \n\
\_|  |_/|_||_|\_\|_|\_\|_| \____/  \___||_| \__,_| \___||_| |_||___/ \___||_| |_||_| |_| \__,_||_|                            \n\
                                                                                                                              \n\
#Ascii art generated with: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20 \n\
______________________________________________________________________________________________________________________________\n \n\
	ヽ༼ຈل͜ຈ༽ﾉ	FINALLY A FANTASTIC GAME TO PLAY IN YOUR COMMAND LINE   \n\n\
                                                                                                                              "    

### Ascii art for an invalid choice out of bounds
out_of_bounds = " \n\
 _____ _           _                        _            __   _                           _      \n\
/  __ \ |         (_)                      | |          / _| | |                         | |     \n\
| /  \/ |__   ___  _  ___ ___    ___  _   _| |_    ___ | |_  | |__   ___  _   _ _ __   __| |___  \n\
| |   | '_ \ / _ \| |/ __/ _ \  / _ \| | | | __|  / _ \|  _| | '_ \ / _ \| | | | '_ \ / _` / __| \n\
| \__/\ | | | (_) | | (_|  __/ | (_) | |_| | |_  | (_) | |   | |_) | (_) | |_| | | | | (_| \__ \ \n\
 \____/_| |_|\___/|_|\___\___|  \___/ \__,_|\__|  \___/|_|   |_.__/ \___/ \__,_|_| |_|\__,_|___/ \n\
                                                                                                 \n\
                                                                                                 \n\
______                                      _                      _             _           _ _ \n\
| ___ \                                    | |                    (_)           | |         | | |\n\
| |_/ / __ ___   __ _ _ __ __ _ _ __ ___   | |_ ___ _ __ _ __ ___  _ _ __   __ _| |_ ___  __| | |\n\
|  __/ '__/ _ \ / _` | '__/ _` | '_ ` _ \  | __/ _ \ '__| '_ ` _ \| | '_ \ / _` | __/ _ \/ _` | |\n\
| |  | | | (_) | (_| | | | (_| | | | | | | | ||  __/ |  | | | | | | | | | | (_| | ||  __/ (_| |_|\n\
\_|  |_|  \___/ \__, |_|  \__,_|_| |_| |_|  \__\___|_|  |_| |_| |_|_|_| |_|\__,_|\__\___|\__,_(_)\n\
                 __/ |                                                                           \n\
                |___/                                                                            \n\
\n\
                                        \n\
Of course you will find this edge case. Consider this my easter egg ;) \n\
"
### Ascii art for player 1 winner
player_one_winner = "\n\
______ _                         __    _                 _    _  _____ _   _ _ \n\
| ___ \ |                       /  |  | |               | |  | ||  _  | \ | | |\n\
| |_/ / | __ _ _   _  ___ _ __  `| |  | |__   __ _ ___  | |  | || | | |  \| | |\n\
|  __/| |/ _` | | | |/ _ \ '__|  | |  | '_ \ / _` / __| | |/\| || | | | . ` | |\n\
| |   | | (_| | |_| |  __/ |    _| |_ | | | | (_| \__ \ \  /\  /\ \_/ / |\  |_|\n\
\_|   |_|\__,_|\__, |\___|_|    \___/ |_| |_|\__,_|___/  \/  \/  \___/\_| \_(_)\n\
                __/ |                                                          \n\
               |___/                                                           \n\
"
### Ascii art for player 2 winner
player_two_winner = "\n\
______ _                         _____   _                 _    _  _____ _   _ _ \n\
| ___ \ |                       / __  \ | |               | |  | ||  _  | \ | | |\n\
| |_/ / | __ _ _   _  ___ _ __  `' / /' | |__   __ _ ___  | |  | || | | |  \| | |\n\
|  __/| |/ _` | | | |/ _ \ '__|   / /   | '_ \ / _` / __| | |/\| || | | | . ` | |\n\
| |   | | (_| | |_| |  __/ |    ./ /___ | | | | (_| \__ \ \  /\  /\ \_/ / |\  |_|\n\
\_|   |_|\__,_|\__, |\___|_|    \_____/ |_| |_|\__,_|___/  \/  \/  \___/\_| \_(_)\n\
                __/ |                                                            \n\
               |___/                                                             \n\
"
### Ascii art for a tie where the board is full
player_no_winner = "\n\
 _____ _   _               _   _      \n\
|_   _| | ( )             | | (_)     \n\
  | | | |_|/ ___    __ _  | |_ _  ___ \n\
  | | | __| / __|  / _` | | __| |/ _ \ \n\
 _| |_| |_  \__ \ | (_| | | |_| |  __/\n\
 \___/ \__| |___/  \__,_|  \__|_|\___|\n\
                                      \n\
"

### Setting the current game board to 0 on all spots
current_game_board = [0,0,0,0,0,0,0,0,0]
### Creating a magic board 
### (see link for explanation: https://fowlie.github.io/2018/08/24/winning-algorithm-for-tic-tac-toe-using-a-3x3-magic-square/)
magic_board = [2, 7, 6,
               9, 5, 1,
               4, 3, 8]                                                                        

### Function for printing the tic_tac_toe board seen when game is run
### with the current_game_board to update the fields
def tic_tac_toe_board():
    print(f"   a     b     c\n\
      |     |     \n\
1  {no_none_value(current_game_board[0])}  |  {no_none_value(current_game_board[1])}  |  {no_none_value(current_game_board[2])}  \n\
 _____|_____|_____\n\
      |     |     \n\
2  {no_none_value(current_game_board[3])}  |  {no_none_value(current_game_board[4])}  |  {no_none_value(current_game_board[5])}  \n\
 _____|_____|_____\n\
      |     |     \n\
3  {no_none_value(current_game_board[6])}  |  {no_none_value(current_game_board[7])}  |  {no_none_value(current_game_board[8])}  \n\
      |     |     ")


### User chooses based on interface, 
### a value for a column (a-c) or row (1-3) and 
### returns it as a list of choices later to be converted to a single number
def choice_getter():
    user_choice_column = 0
    user_choice_row = 0
    user_choice_column = input("Please choose the column (a, b or c) based on the board shown: ").lower() 
    user_choice_row = input("Please choose the row (1, 2 or 3) based on the board shown: ").lower()
    user_choice = [user_choice_column, user_choice_row]
    return user_choice

### Take the user_choice from the `choice_getter()` and return a single int from 1 - 9
### on the board from top left to bottom right
def spot_converter(user_choice):
    if user_choice == ["a","1"]:
        user_choice_converted = 1
    elif user_choice == ["b","1"]:
        user_choice_converted = 2
    elif user_choice == ["c","1"]:
        user_choice_converted = 3
    elif user_choice == ["a","2"]:
        user_choice_converted = 4
    elif user_choice == ["b","2"]:
        user_choice_converted = 5
    elif user_choice == ["c","2"]:
        user_choice_converted = 6
    elif user_choice == ["a","3"]:
        user_choice_converted = 7
    elif user_choice == ["b","3"]:
        user_choice_converted = 8
    elif user_choice == ["c","3"]:
        user_choice_converted = 9
    else:
        print(out_of_bounds)
    return user_choice_converted

### `board_updater()` creates the list with the current status of the game
### with the user_choice and symbol of the player ("X" or "O")
def board_updater(user_choice, symbol):
    current_game_board[user_choice-1] = symbol
    return current_game_board

## `is_choice_valid()` returns true if the choice is valid.
## it checks whether the choice is in an empty spot
def is_choice_valid(choice):
    if current_game_board[choice-1] != 0:
        print("Invalid choice")
        return False
    if choice < 1 or choice > 9:
        print("Invalid choice")
        return False
    return True

### `no_none_value()` takes makes sure that the board is rendered with either "X", "O" or "-" if spot is=0
def no_none_value(value):
    if value == "X":
        return f"{value}"
    elif value == "O":
        return f"{value}"
    elif value == 0:
        return "-"

### `board_simplifier` takes the current game board and converts 
### all "X"'s into a separate board and all "O"'s into a seperate board
### that returns the a list of the simplified boards as a list (nested list)
def board_simplifier(current_game_status):
    player_1_board = []
    player_2_board = []
    for spot in current_game_status:
        if spot == 'X':
            player_1_board.append(1)
        else:
            player_1_board.append(0)
    for spot in current_game_status:
        if spot == 'O':
            player_2_board.append(1)
        else:
            player_2_board.append(0)
    simplified_player_boards = [player_1_board, player_2_board]
    return simplified_player_boards


### `magic_board_converter()` takes the simplified player board and converts
### it to a magic board that has the values of a magic appended, if the value of a cell == 1
### else it appends a 0
def magic_board_converter(board):
    current_magic_board = []
    for place in range(len(board)):
        if board[place] == 1:
            current_magic_board.append(magic_board[place])
        else:
            current_magic_board.append(0)
    return current_magic_board

### The "itertools.combinations" package is used to create subsets consisting of 3 elements
### of the current magic_board
def findsubsets(s, n): 
    return list(itertools.combinations(s, n)) 

### `win_checker()` takes the input of the current magic board for a specific player
### and if the sum of one of the subsets, that does not contain a 0, is equal to 15, 
### the active player has won the game. This is done returning a True value
### therefore, exciting the function.
def win_checker(board):
    n = 3
    subsets = []
    subsets = findsubsets(board, n)
    for subset in subsets:
        if 0 not in subset:
            if sum(subset) == 15:
                print("We have a winner")
                return True

### The `game_instantiater`is the function that runs the game. It is called in the
### bottom of the code
def game_instantiater():
    ### We print the welcoming introduction ASCII art
    print(introduction)
    ### We set the value of player1_winner, player2_winner and is_win_condition_not_met to be False, so that 
    ### the below while loop keeps running.
    player1_winner = False
    player2_winner = False
    is_win_condition_not_met = False
    current_game_status = [0,0,0,0,0,0,0,0,0]
    player1 = create_player("X", "Player 1")
    player2 = create_player("O", "Player 2")
    ### We print the clean tic tac toe board
    tic_tac_toe_board()
    ### We create a while loop that runs as long as the win condition is not met and there
    ### there is a 0 in the current_game_board. This exits the while loop if the board is full
    ### or there is a winner
    while not is_win_condition_not_met and 0 in current_game_board:
        ### We run the turn of player 1.
        ### If run_safe_turn returns "win" it returns true, and exits the function
        player1_winner = run_safe_turn(player1)
        if player1_winner == "win":
            return True
        ### This if statement returns True, so forth there are no more empty spots on the board
        ### hence the board is full and prints the "It's a tie announcement" 
        if 0 not in current_game_board:
            print(player_no_winner)
            return True
        ### We run the turn of player 2. 
        ### If run_safe_turn returns "win" it returns true, and exits the function
        player2_winner = run_safe_turn(player2)
        if player2_winner == "win":
            return True

### run_safe_turn takes the player if and runs the turn. While the player has not
### chosen a valid cell, it will rerun, until an empty cell has been selected
def run_safe_turn(player):
    turn_status = 0
    while turn_status == "error" or turn_status == 0:

        turn_status = run_turn_for_player(player)

        if turn_status == "win":
            announce_winner(player)
            return "win"
        elif turn_status == "error":
            print("Error encountered, replaying turn")
    ### returns "next if the turn is executed correctly, thus moving to next players turn"
    return "next"

### `announce_winner()` uses the dictionary `create_player` to announce the current player
### as a winner
def announce_winner(player):
    if player["name"] == "Player 1":
        print(player_one_winner)
    if player["name"] == "Player 2":
        print(player_two_winner)

### We use a dictionary as a method to create a player and link "X" to "Player 1" and
### "O" to "Player 2"
def create_player(symbol, name):
    return {
                "symbol": symbol, 
                "name": name,
            }

### `run_turn_for_player()` takes the current player and runs through their turn.
def run_turn_for_player(player):
    ### The choice of the player is asked for
    choice = choice_getter()
    ### The choice converts to a "X" "O" board
    choice_converted = spot_converter(choice)
    ### If is_choice_valid(choice_converted) == True then the board is reprinted
    ### with the updated value, and run through the win checker. If `win_checker()` == True
    ### the current player has won. If the choice is not valid, "error" is returned
    ### and the `run_safe_turn()` reruns the turn until a valid choice has been made.
    if is_choice_valid(choice_converted):
        board = board_updater(choice_converted,player["symbol"])
        tic_tac_toe_board()
        board_simplified_list = board_simplifier(board)
        for magic_board in board_simplified_list:
            converted_magic_board = magic_board_converter(magic_board)
            winner = win_checker(converted_magic_board)
            if winner == True:
                return "win"
    else:
        return "error"

### We instantiate the game to start
game_instantiater()