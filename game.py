# Initial implementation of game class, to tranfer run.py functionality into game class
import curses
from curses import textpad
import random
import copy


class Game:
    def __init__(self, stdscr):
        print('init')
        self.stdscr = stdscr  # Standardscreen parameter returned by curses
        
    """
    find the food coordinates making sure it appears inside the box
    but not on the body of the snake 
    """
    def food_coord(self, snake, box):
        chick = None

        while chick is None:
            chick = [random.randint(box[0][0]+1, box[1][0]-1), random.randint(box[0][1]+1, box[1][1]-1)]
            if chick in snake:
                chick = None
        return chick

    # print score in the middle of the box
    def print_score(self, score):
        sh, sw = self.stdscr.getmaxyx()
        score_display = "Score: {}".format(score)
        self.stdscr.addstr(1, sw//2-len(score_display)//2, score_display)
        self.stdscr.refresh()

    """
    Determine if the snake ate the chick and return true if so
    The terminal draws the chick one cell to the left
    due to the emoji size. This visual offset is
    compensated for here by extending the radius of possible hits
    """

    def snake_ate_chick(self, coords_snake_head, coords_chick):
        chick_with_offset = copy.deepcopy(coords_chick)
        chick_with_offset[1] = chick_with_offset[1] + 1
        return (coords_snake_head == chick_with_offset) or (coords_snake_head == coords_chick)
    
    def main(self):
        # ----- Start Game ----------
        # set up curses
        curses.curs_set(0)
        curses.noecho()
        self.stdscr.erase()
        self.stdscr.nodelay(1)
        self.stdscr.timeout(350)

        # create the textpad rectangle where the field goes
        sh, sw = self.stdscr.getmaxyx()
        box = [[3, 3], [sh-3, sw-3]]
        textpad.rectangle(self.stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
        self.stdscr.getch()

        # set the snake's 3 body parts
        snake = [[sh//2, sw//2+1], [sh//2, sh//2], [sh//2, sw//2-1]]
        direction = curses.KEY_RIGHT

        # draw snake's body with a character emoji
        for y, x in snake:
            self.stdscr.addstr(y, x, '▓')

        # create the chick with an emoji
        chick = self.food_coord(snake, box)
        self.stdscr.addstr(chick[0], chick[1], '🐤')

        # print score
        score = 0
        self.print_score(score)

        while 1:
            # everytime the snake moves, anew head is created
            # ask the user to press a key
            key = self.stdscr.getch()

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
            self.stdscr.addstr(new_head[0], new_head[1], '▓')
            snake.insert(0, new_head)

            # increment the score if snake catches the chick
            # display a new chick after the last one is eaten
            # and increase the lenght of the snake
            eaten = self.snake_ate_chick(snake[0], chick)
            if eaten:
                # increment score
                score += 1
                self.print_score(score)
                # display a new chick everytime the snake eats the last one
                chick = self.food_coord(snake, box)

                self.stdscr.addstr(chick[0], chick[1], '🐤')
                # increase speed of the game
                self.stdscr.timeout(100 - (len(snake)//3) % 90)
            else:
                # to mimic motion the last part of the head has to be removed and
                # replaced by a space
                self.stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
                snake.pop()
            # rules of the game
            # if snake crashes agaist the border or bites itself
            # the game is over.
            if (snake[0][0] in [box[0][0], box[1][0]] or
                snake[0][1] in [box[0][1], box[1][1]] or
                    snake[0] in snake[1:]):
                msg = "Game Over!"
                self.stdscr.addstr(sh//2, sw//2-len(msg)//2, msg)
                self.stdscr.nodelay(0)
                self.stdscr.getch()
                break

            self.stdscr.refresh()
            # key = self.stdscr.getch()


def main(stdscr): 
    game = Game(stdscr)
    game.main()
    curses.endwin()


# Run the game if this is main
if __name__ == "__main__":
    try:
        # start main program loop
        curses.wrapper(main)
            
    # quit curses and print exception if there was an error
    except Exception:
        print("Exception")
