# "Automate The Boring Stuff" Book
#  CH 4 Project: Character picture grid.
#  Write a code that uses it to print a heart


# Notice that the heart in the list is stored from right to left.
# So you need to print the grid[1][0],grid[2][0]... the add a new line when
# it goes to the next line.. The last thing your program will print is grid[8][5].

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]



for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j],end='')
    print('')

    
            
