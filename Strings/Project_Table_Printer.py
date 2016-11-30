# "Automate the Boring Stuff" book
# CH6: Table printer.
# Writes a function name prinTable() that takes a list of lists of strings and displays
# it right justified in each column.

def printTable(tableData,colWidths):

    for i in range(len(tableData[0])):      #range(4) this prints the rows
        for j in range(len(tableData)):     #range(3) this prints the columns 
            print(tableData[j][i].rjust(colWidths[j]+1),end='')
        print('')
    


def length_cols(tableData):

    colWidths = [0] * len(tableData)        #colWidth= [0, 0, 0]
    max = 0
    index=0
    for i in tableData:         #'apples', 'oranges', 'cherries' ,'banana'
        for j in i:             #goes through each word
            if len(j) > max:
                max = len(j)
        colWidths[index]=max
        max=0
        index += 1
    return colWidths

    
tableData= [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs','cats','moose','goose']]


printTable(tableData,length_cols(tableData))

 
