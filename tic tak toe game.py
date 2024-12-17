# Hendry Ferose 12-B Tic Tac Tow Game Project (2014) JKKN School

def display_board(board):
    print('\n'*5)
    print(board[7] + '|' + board[8] +'|'+ board[9])
    print(board[4] + '|' + board[5] +'|'+ board[6])
    print(board[1] + '|' + board[2] +'|'+ board[3])



def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1 : Choose your marker between X or O ?").upper()

    if marker == "X":
        return('X','O')
    else:
        return('O','X')

def place_marker(board,marker,position):

    board[position] = marker

def win_check(board, mark):

     return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) )

def space_check(board,position):
   return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False 
    return True

def player_choice(board):
    position = 0 
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check (board,position):
        position = int(input("Choose a position from 1 to 9 :::: => "))
    return position

def replay():
    choice = input("Play again? Say 'Y' for yes or 'N' for No ")
    return choice == 'Y'

 
print ('Welcome to Tic Tac Tow by Henry 12-B CS')

while True:
   #creating board
   the_board = [' ']*10

   player1_marker , player2_marker = player_input()

   
   print("Since Player1 gets to chose Marker.. so Player2 gets fisrt move  ")
   turn = "player2"
   game_on = True

   while game_on:
        
        if turn == "player2":

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 Has Won')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Game Tie")
                    game_on = False
                else:
                    turn = 'player1'
        else:
                
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 Has Won')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Game Tie")
                    game_on = False
                else:
                    turn = 'player2'
       

   if not replay():
       break
   


