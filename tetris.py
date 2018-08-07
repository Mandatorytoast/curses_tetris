import curses, copy, random

stdscr = curses.initscr()
curses.noecho()
stdscr.keypad(True)
curses.curs_set(0)
stdscr.timeout(400)

graphic = 'X'

x_pos = 30
y_pos = 0
max_x = 19
#STARTING COORDINATES FOR ALL THE TETRONIMOES
#TODO: ADD ROTATED VERSIONS
#TODO: MAKE FIRST POSITION THE LOWEST POINT ON THE BLOCK
tetronimo = {"I": [[0,1],[0,2],[0,3],[0,4]],
             "O": [[0,1],[0,2],[1,1],[1,2]],
             "T": [[0,1],[0,2],[0,3],[1,2]],
             "Z": [[0,1],[0,2],[1,2],[1,3]],
             "N": [[1,1],[1,2],[0,2],[0,3]],
             "L": [[0,1],[1,1],[2,1],[2,2]],
             "RL": [[0,2],[1,2],[2,2],[2,1]]}

placedblocks = []

blocks = list(tetronimo.keys())


c = 0

current_block = copy.deepcopy(tetronimo["T"])
#MAIN GAME LOOP
while True:
    c = stdscr.getch()
    if c==ord('q'):
        break
    stdscr.clear()
    for i in current_block:
        stdscr.addstr(i[0],i[1], graphic)
        i[0] += 1
        #MOVE TETRONIMO LEFT AND RIGHT WHILE FALLING
        if c == curses.KEY_RIGHT:
            i[1] += 1
        elif c == curses.KEY_LEFT:
            i[1] -= 1
    
    for i in placedblocks:
        stdscr.addstr(i[0],i[1], graphic)
    
    #DEBUGGING INFO
    #stdscr.addstr(2, 20, "placed blocks: {}\n".format(placedblocks))
    #stdscr.addstr(1, 20, "current block: {}".format(current_block))
    
    
    if current_block[0][0] == max_x:
        for i in current_block:
            placedblocks.append(i)

        current_block = copy.deepcopy(tetronimo[blocks[random.randint(0,len(blocks)-1)]]) 

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
