import curses
from curses import textpad
import random


# Food coordinate making sure it does not appear on the the body
# of the snake
def food_coord(snake, box):
    chick = None

    while chick is None:
        chick = [random.randint(box[0][0]+1, box[1][0]-1),
                 random.randint(box[0][1]+1, box[1][1]-1)]
        if chick in snake:
            chick = None
    return chick




# create the textpad rectangle where the field goes
def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(150)
    sh, sw = stdscr.getmaxyx()
    box = [[3, 3], [sh-3, sw-3]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    stdscr.getch()
    # set the snake's 3 body parts
    snake = [[sh//2, sw//2+1], [sh//2, sh//2], [sh//2, sw//2-1]]
    direction = curses.KEY_RIGHT

    # draw snake body
    for y, x in snake:
        stdscr.addstr(y, x, '#')

    # create the chick
    chick = food_coord(snake, box)
    stdscr.addstr(chick[0], chick[1], '🐤')

    # print score
    score = 0
    score_display = "Score: {}".format(score)
    stdscr.addstr(1, sw//2-len(score_display)//2, score_display)

    while 1:
        # everytime the snake moves, anew head has to be created
        # ask the user to press a key
        key = stdscr.getch()

        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP,
                   curses.KEY_DOWN]:
            direction = key

        head = snake[0]

        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1]+1]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1]-1]
        elif direction == curses.KEY_UP:
            new_head = [head[0]-1, head[1]]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0]+1, head[1]]

        # insert a new head
        stdscr.addstr(new_head[0], new_head[1], '#')
        snake.insert(0, new_head)

        # increment the score if snake catches the chick
        # and increase the lenght of the snake
        if snake[0] == chick:
            # increment score
            score += 1
            score_display = "Score: {}".format(score)
            stdscr.addstr(1, sw//2-len(score_display)//2, score_display)
            # display a new chick everytime the snake eats the last one
            chick = food_coord(snake, box)
            stdscr.addstr(chick[0], chick[1], '🐤')
        else:
            # to mimic motion the last part of the head has to be removed and
            # replaced by a space
            stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()
        # rules of the game
        # if snake crashes agaist the border or bites itself
        # the game is over.
        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1] in [box[0][1], box[1][1]] or
                snake[0] in snake[1:]):
            msg = "Game Over!"
            stdscr.addstr(sh//2, sw//2-len(msg)//2, msg)
            stdscr.nodelay(0)
            stdscr.getch()

        stdscr.refresh()
        key = stdscr.getch()


curses.wrapper(main)
