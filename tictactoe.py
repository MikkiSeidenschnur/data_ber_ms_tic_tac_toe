import itertools 

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



current_game_board = [0,0,0,0,0,0,0,0,0]
player1_win_conditions = []
player2_win_conditions = []
magic_board = [2, 7, 6,
               9, 5, 1,
               4, 3, 8]                                                                        

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
### we've updated value to something that is easier handled
def choice_getter():
    user_choice_column = 0
    user_choice_row = 0
    user_choice_column = input("Please choose the column (a, b or c) based on the board shown: ").lower() 
    user_choice_row = input("Please choose the row (1, 2 or 3) based on the board shown: ").lower()
    user_choice = [user_choice_column, user_choice_row]
    return user_choice

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

###2. Create the list with the current status of the game
def board_updater(user_choice, symbol):
    current_game_board[user_choice-1] = symbol
    return current_game_board

## which_player
## choice_validator
def is_choice_valid(choice):
    if current_game_board[choice-1] != 0:
        print("Invalid choice")
        return False
    if choice < 1 or choice > 9:
        print("Invalid choice")
        return False
    return True

### Let's make the board
def no_none_value(value):
    if value == "X":
        return f"{value}"
    elif value == "O":
        return f"{value}"
    elif value == 0:
        return "-"

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

def magic_board_converter(board):
    current_magic_board = []
    for place in range(len(board)):
        if board[place] == 1:
            current_magic_board.append(magic_board[place])
        else:
            current_magic_board.append(0)
    return current_magic_board

def findsubsets(s, n): 
    return list(itertools.combinations(s, n)) 

def win_checker(board):
    n = 3
    subsets = []
    subsets = findsubsets(board, n)
    for subset in subsets:
        if 0 not in subset:
            if sum(subset) == 15:
                print("We have a winner")
                return True

def game_instantiater():
    print(introduction)
    player1_winner = False
    player2_winner = False
    is_win_condition_not_met = False
    current_game_status = [0,0,0,0,0,0,0,0,0]
    player1 = create_player("X", "Player 1")
    player2 = create_player("O", "Player 2")

    tic_tac_toe_board()
    while not is_win_condition_not_met and 0 in current_game_board:
        player1_winner = run_safe_turn(player1)
        if player1_winner == "win":
            return True
        player2_winner = run_safe_turn(player2)
        if player2_winner == "win":
            return True

def run_safe_turn(player):
    turn_status = 0
    while turn_status == "error" or turn_status == 0:

        turn_status = run_turn_for_player(player)

        if turn_status == "win":
            announce_winner(player)
            return "win"
        elif turn_status == "error":
            print("Error encountered, replaying turn")
    
    return "next"

def announce_winner(player):
    if player["name"] == "Player 1":
        print(player_one_winner)
    if player["name"] == "Player 2":
        print(player_two_winner)

def create_player(symbol, name):
    return {
                "symbol": symbol, 
                "name": name,
            }

def run_turn_for_player(player):
    choice = choice_getter()
    choice_converted = spot_converter(choice)
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

game_instantiater()