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
    
    while 1:
        # everytime the snake moves, anew head has to be created to resamble motion
        key= stdscr.getch()

        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]
            direction = key
        
        head = snake[0]

        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1]+1]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1]-1]
        elif direction == curses.KEY_UP:
            new_head = [head[0], head[1]-1]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0], head[1]-1]

        snake.insert(0, new_head)
        stdscr  .addstr(new_head[0], new_head[1], '🟰')  




curses.wrapper(main)
