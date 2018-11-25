def padded(binary): # Adds trailing zeros so that number is printed in 8 bits
    return (8-len(binary))*'0'+binary

def printScreen(screen, width): # Prints the current state of the screen
    for i in range(len(screen)//(width//8)):
        for j in range(width//8):
            print(padded(bin(screen[i*(width//8)+j])[2:]), end='')
        print('')
            
def drawLine(screen, width, x1, x2, y):
    '''
    If both x1 and x2 are in the same byte, then the bits can be
    set in one step.
    
    Otherwise, the task can be divided into 3 parts:
    1. Set the bits in the byte containing bit x1
    2. Set the bits in the byte containing bit x2
    3. Set the bits in all the bytes between above two bytes
    '''
    if x1//8==x2//8:
        screen[y*(width//8)+(x1//8)]|=((1<<(x2-x1+1))-1)<<(8-((x2%8)+1))

    else:
        # Part 1
        screen[y*(width//8)+(x1//8)]|=(1<<(8-(x1%8)))-1

        # Part 2
        screen[y*(width//8)+(x2//8)]|=((1<<((x2%8)+1))-1)<<(8-((x2%8)+1))

        # Part 3
        for i in range(y*(width//8)+(x1//8)+1, y*(width//8)+(x2//8)):
            screen[i]|=(1<<8)-1

height,width=map(int,input().split())
screen=[0 for i in range((width//8)*height)]
printScreen(screen, width)
while True:
    x1,x2,y=map(int,input().split()) # Zero indexed
    drawLine(screen, width, x1, x2, y)
    printScreen(screen, width)
