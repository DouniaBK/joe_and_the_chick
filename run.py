import curses
from curses import textpad
import numpy as np
import random
import copy
import time


class Game:
    def __init__(self, stdscr):
        curses.noecho()
        self.stdscr = stdscr  # Standardscreen parameter returned by curses
        self.snake = []
        self.chick = []
        self.box = []
        self.score = 0
        self.level = 1
        self.menu = ['Home', 'Play', 'Settings', 'Exit']
        self.direction = curses.KEY_RIGHT
        self.fieldItems = []
        self.self_defense_coordinate = None

    """-------------------- MENU -----------------------"""

    def print_menu(self, selected_row_idx):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()
        for idx, row in enumerate(self.menu):
            x = w//2 - len(row)//2
            y = h//2 - len(self.menu)//2 + idx
            if idx == selected_row_idx:
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y, x, row)
                self.stdscr.attroff(curses.color_pair(1))
            else:
                self.stdscr.addstr(y, x, row)
        self.stdscr.refresh()

    def print_center(self, text):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()
        x = w//2 - len(text)//2
        y = h//2
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()

    def menu_main(self):
        # Try block to handle terminal incompatibility
        # with disabling the cursor. If terminal does not
        # support invisible cursors, as the one provided in the
        # code-institute template, curs_set will return an error.
        try:
            curses.curs_set(0)
        except Exception:
            print("Disabling cursor not supported by terminal")

        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_CYAN)

        current_row = 0
        self.print_menu(current_row)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1

            elif key == curses.KEY_DOWN and current_row < len(self.menu)-1:
                current_row += 1
            elif (key == curses.KEY_ENTER) or (key in [10, 13]):

                if self.menu[current_row] == 'Play':
                    return True

                if self.menu[current_row] == 'Exit':
                    return False

            self.print_menu(current_row)

    """-------------------- Game -----------------------"""
    def find_free_coordinate(self): 
        """
        find the food coordinates making sure it appears inside the box
        but not on the body of the snake """
        free_coord = None

        while free_coord is None:
            free_coord = [random.randint(
                self.box[0][0]+1, self.box[1][0]-1), random.randint(self.box[0][1]+1, self.box[1][1]-1)]
            if (free_coord in self.snake) or (self.fieldItems[free_coord[0], free_coord[1]] > 0) or (free_coord == self.chick):
                free_coord = None
        return free_coord

    def food_coord(self):
        coords_chick = self.find_free_coordinate()

        return coords_chick

    # print score in the middle of the box
    def print_score(self):
        sh, sw = self.stdscr.getmaxyx()
        score_display = "Score: {}".format(self.score)
        self.stdscr.addstr(1, sw//2-len(score_display)//2, score_display)
        self.stdscr.refresh()

    # Check for collision, or whether the snake bit itself
    def evaluate_field(self):

        # Check for collision with border or itself
        collision = self.snake[0][0] in [self.box[0][0], self.box[1][0]] or self.snake[0][1] in [
            self.box[0][1], self.box[1][1]] or self.snake[0] in self.snake[1:]

        # Check for collision with items on the field
        collision = collision or (
            self.fieldItems[self.snake[0][0], self.snake[0][1]] == 1)

        return collision

    def generate_barrier(self):
        """ Generate a barrier at a random place """
        if self.level == 1:
            barrier = self.find_free_coordinate()
            self.fieldItems[barrier[0], barrier[1]] = 1
            self.fieldItems[barrier[0], barrier[1]+1] = 1
            self.fieldItems[barrier[0], barrier[1]+2] = 1

        if self.level == 2:
            barrier = self.find_free_coordinate()
            self.fieldItems[barrier[0], barrier[1]] = 1
            self.fieldItems[barrier[0]+1, barrier[1]+1] = 1
            self.fieldItems[barrier[0]+2, barrier[1]+2] = 1
            self.fieldItems[barrier[0]+3, barrier[1]+3] = 1
            self.fieldItems[barrier[0]+4, barrier[1]+4] = 1

    # Print a barrier on the field
    def draw_barrier(self):
        for x in range(self.fieldItems.shape[0]):
            for y in range(self.fieldItems.shape[1]):
                if self.fieldItems[x, y] == 1:
                    self.stdscr.addstr(x, y, '▩')

    def generate_reward(self):
        """ Generate sandwich for joe as a reward to increase score"""
        if self.level == 1:
            reward = self.find_free_coordinate()
            self.fieldItems[reward[0], reward[1]] = 2

        if self.level == 2:
            reward = self.find_free_coordinate()
            self.fieldItems[reward[0], reward[1]] = 2

    # Print reward on the field which will increase the score
    def draw_reward(self):
        for x in range(self.fieldItems.shape[0]):
            for y in range(self.fieldItems.shape[1]):
                if self.fieldItems[x, y] == 2:
                    self.stdscr.addstr(x, y, '🌯')

    def evaluate_level_up(self):
        if (self.score >= 4):
            self.level = self.level + 1
            return True

        return False

    def initialize_field(self):

        self.stdscr.erase()
        self.stdscr.nodelay(1)
        # create the textpad rectangle where the field goes
        sh, sw = self.stdscr.getmaxyx()
        self.box = [[3, 3], [sh-3, sw-3]]
        textpad.rectangle(
            self.stdscr, self.box[0][0], self.box[0][1], self.box[1][0], self.box[1][1])

        # initialize field items array, which stores the game level
        self.fieldItems = np.zeros((sh, sw))

        # generate_barrier
        self.generate_barrier()
        self.draw_barrier()

        # generate reward and print it on the field
        self.generate_reward()
        self.draw_reward()

        # set the snake's 3 body parts
        self.snake = [[sh//2, sw//2+1], [sh//2, sh//2], [sh//2, sw//2-1]]
        self.direction = curses.KEY_RIGHT

        # draw snake's body with a character emoji
        for y, x in self.snake:
            self.stdscr.addstr(y, x, '▓')

        # create the chick with an emoji
        self.chick = self.food_coord()
        self.stdscr.addstr(self.chick[0], self.chick[1], '🐤')

        # print score
        self.score = 0
        self.print_score()

        self.stdscr.timeout(400)
        self.stdscr.refresh()

    def progress_to_next_level(self):
        msg = "Level up"
        sh, sw = self.stdscr.getmaxyx()
        self.stdscr.addstr(sh//2, sw//2-len(msg)//2, msg)
        self.stdscr.nodelay(0)
        # key = self.stdscr.getch()
        self.stdscr.refresh()
        time.sleep(5)
        self.initialize_field()

    def snake_ate_chick(self, coords_snake_head, coords_chick):
        """
        Determine if the snake ate the chick and return true if so
        The terminal draws the chick one cell to the left
        due to the emoji size. This visual offset is
        compensated for here by extending the radius of possible hits
        """
        chick_with_offset = copy.deepcopy(coords_chick)
        chick_with_offset[1] = chick_with_offset[1] + 1
        return (coords_snake_head == chick_with_offset) or (coords_snake_head == coords_chick)

    def snake_ate_stuff(self):
        """
        Detect if snake ate a sandwich and reward two points
        Detect if snake ate taser and derement one point
        """
        ate_stuff = False
        # Snake ate sandwitch
        if self.fieldItems[self.snake[0][0], self.snake[0][1]] == 2:
            self.score =+ 2
            self.print_score()
            ate_stuff = True

        # Snake got tasered
        if self.fieldItems[self.snake[0][0], self.snake[0][1]] == 3:
            self.score =- 1
            if self.score < 0:
                self.score = 0
            self.print_score()
            ate_stuff = True

        if ate_stuff == True:
            self.fieldItems[self.snake[0][0], self.snake[0][1]] = 0
        
    def activate_chick_self_defense(self):
        """
        Print the lightening bold , representing a taser, right next to the chick
        but if the spot is occupied, don't print
        """
        if self.score >= 0:
            self_defense_coords = copy.deepcopy(self.chick)
            self_defense_coords[0] = self_defense_coords[0] - 1
            self_defense_coords[1] = self_defense_coords[1] + 1
            if self.fieldItems[self_defense_coords[0], self_defense_coords[1]] == 0:
                self.fieldItems[self_defense_coords[0], self_defense_coords[1]] = 3
                self.stdscr.addstr(self_defense_coords[0], self_defense_coords[1], '⚡')
                self.self_defense_coordinate = self_defense_coords

    def deactivate_chick_self_defense(self):
        """ Clean up old chicks self defense weapon """
        if not self.self_defense_coordinate == None:
            self.stdscr.addstr(self.self_defense_coordinate[0], self.self_defense_coordinate[1], ' ')
            self.self_defense_coordinate = None
            self.stdscr.refresh()

    def run(self):
        # ----- Show Menu ----------
        ret_val = self.menu_main()
        # menu_main returns true or false, to continue or quit the game respectively
        if not ret_val:
            return
        # ----- Start Game ----------
        """ Set up curses
        Try block to handle terminal incompatibility 
        with disabling the cursor. If terminal does not
        support invisible cursors, as the one provided in the
        code-institute template, curs_set will return an error."""
        try:
            curses.curs_set(0)
        except Exception:
            print("Disabling cursor not supported by terminal")
        self.stdscr.nodelay(1)

        # Initialize the playing field based on the current level
        self.initialize_field()

        while 1:
            # everytime the snake moves, anew head is created
            # ask the user to press a key
            key = self.stdscr.getch()

            if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP,
                       curses.KEY_DOWN]:
                self.direction = key

            head = self.snake[0]

            if self.direction == curses.KEY_RIGHT:
                new_head = [head[0], head[1]+1]
            elif self.direction == curses.KEY_LEFT:
                new_head = [head[0], head[1]-1]
            elif self.direction == curses.KEY_UP:
                new_head = [head[0]-1, head[1]]
            elif self.direction == curses.KEY_DOWN:
                new_head = [head[0]+1, head[1]]

            # insert a new head
            self.stdscr.addstr(new_head[0], new_head[1], '▓')
            self.snake.insert(0, new_head)
            self.stdscr.addstr(10, 10, ' ')

            # Check if the snake ate something besides the chick
            self.snake_ate_stuff()

            # increment the score if snake catches the chick
            # display a new chick after the last one is eaten
            # and increase the lenght of the snake
            ate_chick = self.snake_ate_chick(self.snake[0], self.chick)
            if ate_chick:
                # increment score
                self.score += 1
                self.print_score()

                self.deactivate_chick_self_defense()

                # display a new chick everytime the snake eats the last one
                self.chick = self.food_coord()

                self.stdscr.addstr(self.chick[0], self.chick[1], '🐤')
                self.activate_chick_self_defense()
                # increase speed of the game
                #self.stdscr.timeout(100 - (len(self.snake)//3) % 90)
            else:
                # to mimic motion the last part of the head has to be removed
                # and replaced by a space
                self.stdscr.addstr(self.snake[-1][0], self.snake[-1][1], ' ')
                self.snake.pop()
            """
            rules of the game
            if snake crashes against the border, a barrier or bites itself
            the game is over
            """
            if (self.evaluate_field()):
                msg = "Game Over!"
                sh, sw = self.stdscr.getmaxyx()
                self.stdscr.addstr(sh//2, sw//2-len(msg)//2, msg)
                self.stdscr.nodelay(0)
                self.stdscr.getch()
                break

            self.stdscr.refresh()

            # Evaluate the level progress
            lvlup = self.evaluate_level_up()
            if (lvlup == True):
                self.progress_to_next_level()

            # key = self.stdscr.getch()


def main(stdscr):
    game = Game(stdscr)
    game.run()
    curses.endwin()


# Run the game if this is main
if __name__ == "__main__":
    try:
        # start main program loop
        curses.wrapper(main)

    # quit curses and print exception if there was an error
    except Exception as e:
        print(e)
