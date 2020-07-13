from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
def game_position():
    print("These are the position numbers,if you want to place your mark on the desired position of board,")
    print("so just remmember these position number ,it will help you")
    print('7'+'|'+'8'+'|'+'9')
    print('4'+'|'+'5'+'|'+'6')
    print('1'+'|'+'2'+'|'+'3')
    
def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input("enter player1 what you want to be X or O:")
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
      
def place_marker(board, marker, position):
    board[position]=marker   

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))   
  
  
import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'player1'
    else:
        return 'player2'

def space_check(board,position):
    return board[position]==' '
  
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False 
    return True
  
def player_choice(board,turn):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input(f"{turn} enter your position from (1-9)"))
    return position

def replay():
    return input("enter y,if you want to play again or enter n").lower()=='y'
    
print("WELCOME TO TIC TAC TOE")
while True:
    clear_output()
    game_position()
    board=[' ']*10
    player1,player2=player_input()
    turn=choose_first()
    print(turn+' will go first')
    
    play=input("Are you ready to play the game then press yes:")
    if play.lower()=='yes':
        game_on=True
    else:
        game_on=False
        
    while game_on:
        if turn=='player1':
            display_board(board)
            position=player_choice(board,turn)
            place_marker(board,player1,position)
            
            if win_check(board,player1):
                display_board(board)
                print("player 1 has won the game")
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game has been tie")
                    break
                else:
                    turn="player2"
        else:
            display_board(board)
            position=player_choice(board,turn)
            place_marker(board,player2,position)
            
            if win_check(board,player2):
                display_board(board)
                print("player 2 has won the game")
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game has been tie")
                    break
                else:
                    turn="player1"
    if not replay():
        break
print()        
print("Thank you for playing my game:)")
