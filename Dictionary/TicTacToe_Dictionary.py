#  Code from the "Automate The Boring Stuff" Book
#  CH 5: Tic-Tac-Toe Board. 
#  A simple game of Tic-Tac-Toe in a dictionary.


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
   

theBoard= {'top-L' :' ', 'top-M': ' ', 'top-R': ' ',
           'mid-L' :' ', 'mid-M': ' ', 'mid-R': ' ',
           'low-L' :' ', 'low-M': ' ', 'low-R': ' '}


turn = 'X'             #initial
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move=input()
    theBoard[move]= turn        #put 'X' or 'O' values in specified key (move) of the Dictionary
    if turn == 'X':             #ex: theBoard['top-L']= X
        turn ='O'
    else:
        turn = 'X'

printBoard(theBoard)
