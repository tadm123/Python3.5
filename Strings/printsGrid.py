# ThinkPython - http://greenteapress.com/thinkpython2/html/thinkpython2004.html
# Exercise 3 - prints a grid with assigned width and height.

def grid(height,width):
    for h in range(height):
        print('+ - - - - ' *width + '+')
        print('|         ' *width + '|')
        print('|         ' *width + '|')
        print('|         ' *width + '|')
        print('|         ' *width + '|')
    print('+ - - - - '*width + '+')


print('This program prints a grid.\n')
h = int(input('Type the height of grid: '))
w = int(input('Type the width of grid: '))
grid(h,w)
