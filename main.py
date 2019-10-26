def create_board():
    
    board = {}
    board['turn'] = 0
    board['a1'] = '-'
    board['b1'] = '-'
    board['c1'] = '-'
    board['a2'] = '-'
    board['b2'] = '-'
    board['c2'] = '-'
    board['a3'] = '-'
    board['b3'] = '-'
    board['c3'] = '-'   
    
    board['board'] = '''
   a     b     c
      |     |     
1  {a1}  |  {b1}  |  {c1}  
 _____|_____|_____
      |     |     
2  {a2}  |  {b2}  |  {c2}  
 _____|_____|_____
      |     |     
3  {a3}  |  {b3}  |  {c3}  
      |     |     
      '''
    return board
#     print(board.format(
#         a1 = '-',
#         b1 = '-',
#         c1 = '-',
#         a2 = '-',
#         b2 = '-',
#         c2 = '-',
#         a3 = '-',
#         b3 = '-',
#         c3 = '-')
#          )
    
def display_board(board):
    print(board['board'].format(
        a1 = board['a1'],
        b1 = board['b1'],
        c1 = board['c1'],
        a2 = board['a2'],
        b2 = board['b2'],
        c2 = board['c2'],
        a3 = board['a3'],
        b3 = board['b3'],
        c3 = board['c3']
    ))

def make_move(board):
    turn = board['turn']
    marker = 'O'
    if turn % 2 == 0:
        marker = 'X'
    flag = True
    while flag:
        square = input('Choose a coordinate: ')
        if board[square] == '-':
            if square in board.keys() and square != 'board' and square != 'turn':
                board[square] = marker
                flag = False
            else:
                print('Please choose a valid coordinate.')
        else:
            print('That square already has a mark!')
    
def check_board(board):
    pass
# Use the turn number.

def tic_tac_toe():
    board = create_board()
    game_won = False
    while not game_won:
        display_board(board)
        make_move(board)
        board['turn'] += 1
                
tic_tac_toe()