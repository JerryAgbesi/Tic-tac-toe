#  ----- Global variables -----

   #game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
#if the game is still going on
game_continues = True

#who wins? who tied
winner = None

# who is the current player?
current_player = "x"

def display():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
def play_game():

#display board
  display()

  while game_continues:

     handle_turn( current_player)

     check_game()

     flip_player()
      #game has ended
     if winner == "x" or winner == "o" :
      print( winner + " won.")
     elif winner == None:
      print("tie.")



def handle_turn(player):
    global valid
    print(player + "'s turn")
    position = input("input a position from 1 to 9:")
    if position not in ["1","2","3","4","5","6","7","8","9"]:
     position = input(" invalid input ,input a position from 1 to 9:")
    position = int(position) - 1
    if board[position] != "-":
     print("That space is occupied, input somewhere else")
    board[position] = player
    display()


def check_game():
    check_win()
    check_tie()


def  check_rows():
    global game_continues
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
             game_continues = False
    if row_1:
            return board[0]
    elif row_2:
            return board[3]
    elif row_3:
            return board[6]
    return

def check_columns():
     global game_continues
     column_1 = board[0] == board[3] == board[6] != "-"
     column_2 = board[1] == board[4] == board[7] != "-"
     column_3 = board[2] == board[5] == board[8] != "-"
     if column_1 or column_2 or column_3:
              game_continues = False
     if column_1:
         return board[0]
     elif column_2:
             return board[1]
     elif column_3:
             return board[2]
     return

def check_diagonals():
  global game_continues
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"

  if diagonal_1 or diagonal_2 :
         game_continues = False
  if diagonal_1:
          return board[0]
  elif diagonal_2:
        return board[2]


  return

def check_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_tie():
    global game_continues
    if "-" not in board:
     game_continues = False
     return

def flip_player():
    global current_player
    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"

    return


play_game()