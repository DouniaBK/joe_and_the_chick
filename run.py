import curses
from curses import textpad

# create the textpad rectangle where the field goes


def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    box = [[3, 3], [sh-3, sw-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    stdscr.getch()
    # set the snake's 3 body parts
    snake = [[sh//2, sw//2+1], [sh//2, sh//2], [sh//2, sw//2-1]]
    direction = curses.KEY_RIGHT
    # draw snake body
    for y, x in snake:
        stdscr.addstr(y, x, '🟰')
    
    


curses.wrapper(main)
