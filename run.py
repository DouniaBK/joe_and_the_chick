
import curses
from curses import textpad
import time
import random
import copy
import numpy as np


class Game:
    """ Initialize game"""

    def __init__(self, stdscr):
        curses.noecho()
        self.stdscr = stdscr  # Standardscreen parameter returned by curses
        self.snake = []
        self.chick = []
        self.box = []
        self.score = 0
        self.level = 3
        self.menu = ['Home', 'Play', 'Legend', 'Exit']
        self.welc_msg = ['☕  Welcome to Joe and the chick  🐤', 'Choose play to start or Legend to read the game instructions']
        self.direction = curses.KEY_RIGHT
        self.fieldItems = []
        self.speed = 200
        self.self_defense_coordinate = None

        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0

    """-------------------- MENU -----------------------"""

    def print_menu(self, selected_row_idx):
        self.stdscr.clear()

        h, w = self.stdscr.getmaxyx()

        self.stdscr.addstr(h//2 - 6, w//2 - len(self.welc_msg[0])//2, self.welc_msg[0])
        self.stdscr.addstr(h//2 - 4, w//2 - len(self.welc_msg[1])//2, self.welc_msg[1])


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
        """ Print menu in the center of the terminal"""
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()
        x = w//2 - len(text)//2
        y = h//2
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()

    def menu_main(self):
        """
        Try block to handle terminal incompatibility
        with disabling the cursor. If terminal does not
        support invisible cursors, as the one provided in the
        code-institute template, curs_set will return an error.
        """
        try:
            curses.curs_set(0)
        except Exception:
            print("Disabling cursor not supported by terminal provided by Code Institute")

        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_CYAN)
        current_row = 0
        self.print_menu(current_row)
        # handle menu item selection
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
                self.box[0][0]+4, self.box[1][0]-4), random.randint(self.box[0][1]+4, self.box[1][1]-4)]
            if (free_coord in self.snake) or (self.fieldItems[free_coord[0], free_coord[1]] > 0) or (free_coord == self.chick):
                free_coord = None
        return free_coord

    def food_coord(self):
        coords_chick = self.find_free_coordinate()

        return coords_chick

    def print_score(self):
        """print score in the top center of the terminal outside the field"""
        sh, sw = self.stdscr.getmaxyx()
        score_display = "Score: {}".format(self.score)
        self.stdscr.addstr(1, sw//2-len(score_display)//2, score_display)
        self.stdscr.refresh()

    def evaluate_field(self):
        """
        Check for collision, or whether the snake bit itself
        Check for collision with border or itself
        """
        collision = self.snake[0][0] in [self.box[0][0], self.box[1][0]] or self.snake[0][1] in [
            self.box[0][1], self.box[1][1]] or self.snake[0] in self.snake[1:]

        # Check for collision with items on the field
        collision = collision or (
            self.fieldItems[self.snake[0][0], self.snake[0][1]] == 1)

        return collision

    def generate_barrier_rectangle(self, x_start_percent, x_end_percent, y_start_percent, y_end_percent):
        """ Generate a rectangle with the measurements mentioned below 
        as a barrier """

        x_start_idx = int(
            np.floor(x_start_percent * (self.max_x - self.min_x))) + self.min_x
        x_end_idx = int(
            np.floor(x_end_percent * (self.max_x - self.min_x))) + self.min_x
        y_start_idx = int(
            np.floor(y_start_percent * (self.max_y - self.min_y))) + self.min_y
        y_end_idx = int(
            np.floor(y_end_percent * (self.max_y - self.min_y))) + self.min_y

        for x in range(x_start_idx, x_end_idx):
            for y in range(y_start_idx, y_end_idx):
                self.fieldItems[x, y] = 1

    def generate_barrier(self):
        """ 
        Generate a barrier
        Coodinates are calculated in percent
        Mug appears between the mid-center barriers
        """
        if self.level == 1:
            self.generate_barrier_rectangle(0.20, 0.26, 0.0, 0.50)
            self.generate_barrier_rectangle(0.70, 0.75, 0.0, 0.70)
            self.generate_barrier_rectangle(0.40, 0.45, 0.4, 1)

        if self.level == 2:
            self.generate_barrier_rectangle(0.20, 0.26, 0.0, 0.40)
            self.generate_barrier_rectangle(0.70, 0.75, 0.0, 0.40)
            self.generate_barrier_rectangle(0.20, 0.26, 0.6, 1)
            self.generate_barrier_rectangle(0.70, 0.75, 0.6, 1)
            self.generate_barrier_rectangle(0.00, 0.35, 0.48, 0.53)
            self.generate_barrier_rectangle(0.65, 1, 0.48, 0.53)

            # Add a coffee mug to the level
            sh, sw = self.stdscr.getmaxyx()
            coffee_mug = [int(np.ceil(0.45 * sh)), sw//2]
            self.fieldItems[coffee_mug[0], coffee_mug[1]] = 4
            self.stdscr.addstr(coffee_mug[0], coffee_mug[1], '☕')

        if self.level == 3:
            self.generate_barrier_rectangle(0.20, 0.26, 0.0, 0.25)
            self.generate_barrier_rectangle(0.70, 0.75, 0.0, 0.25)
            self.generate_barrier_rectangle(0.20, 0.26, 0.75, 1)
            self.generate_barrier_rectangle(0.70, 0.75, 0.75, 1)
            self.generate_barrier_rectangle(0.2, 0.85, 0.48, 0.52)
            self.generate_barrier_rectangle(0.48, 0.52, 0.2, 0.85)

            # Add a coffee mug to the level
            sh, sw = self.stdscr.getmaxyx()
            coffee_mug = [int(np.ceil(0.95 * (sh-3))), sw//2]
            self.fieldItems[coffee_mug[0], coffee_mug[1]] = 4
            self.stdscr.addstr(coffee_mug[0], coffee_mug[1], '☕')

    def is_within_barriers(self, x, y):
        return (x < self.max_x) and (x > self.min_x) and (y < self.max_y) and (y > self.min_y)

    def draw_barrier(self):
        """Print a barrier on the field"""
        for x in range(self.fieldItems.shape[0]):
            for y in range(self.fieldItems.shape[1]):
                if self.fieldItems[x, y] == 1 and self.is_within_barriers(x, y):
                    self.stdscr.addstr(x, y, '▩')

    def generate_reward(self):
        """ Generate sandwich for joe as a reward to increase score"""
        reward = self.find_free_coordinate()
        self.fieldItems[reward[0], reward[1]] = 2

    def draw_reward(self):
        """ Print reward on the field which will increase the score """
        for x in range(self.fieldItems.shape[0]):
            for y in range(self.fieldItems.shape[1]):
                if self.fieldItems[x, y] == 2 and self.is_within_barriers(x, y):
                    self.stdscr.addstr(x, y, '🌯')

    def evaluate_level_up(self):
        """ check the score and evaluate the level accordingly"""
        if (self.score >= 1):
            self.level = self.level + 1
            return True

        return False

    def initialize_field(self):

        self.stdscr.erase()
        self.stdscr.nodelay(1)
        # create the textpad rectangle where the field goes
        sh, sw = self.stdscr.getmaxyx()

        self.min_x = 3
        self.max_x = sh-3
        self.min_y = 3
        self.max_y = sw-3

        self.box = [[self.min_x, self.min_y], [self.max_x,  self.max_y]]
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
        # calculate center of the field (game window)
        snake_center_x = (self.max_x - self.min_x)//2 + self.min_x
        snake_center_y = (self.max_y - self.min_y)//2 + self.min_y

        # defined the snake (depending on the level)
        self.snake = [[snake_center_x, snake_center_y+1], [snake_center_x, snake_center_y], [snake_center_x, snake_center_y-1]]
        self.direction = curses.KEY_RIGHT
        if self.level == 2:
            self.snake = [[snake_center_x + 1, snake_center_y + 5], [snake_center_x + 1, snake_center_y+4], [snake_center_x + 1, snake_center_y+3]]
        elif self.level == 3:
            self.snake = [[snake_center_x + 4, snake_center_y + 5], [snake_center_x + 4, snake_center_y + 4], [snake_center_x + 4, snake_center_y + 3]]

        # draw snake's body with a character emoji
        for y, x in self.snake:
            self.stdscr.addstr(y, x, '▓')

        # create the chick with an emoji
        self.chick = self.food_coord()
        self.stdscr.addstr(self.chick[0], self.chick[1], '🐤')

        # print score
        self.score = 0
        self.print_score()
        #  set speed
        if self.level == 1:
            self.speed = 200
        elif self.level == 2:
            self.speed = 150
        elif self.level == 3:
            self.speed = 100
        self.stdscr.timeout(self.speed)

        self.stdscr.refresh()

    def progress_to_next_level(self):
        """ Allow progress to next level"""
        msg = "How you doing? Leveling up, player."
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
        Detect if snake ate taser and decrement one point
        """

        # Snake ate sandwitch
        if self.fieldItems[self.snake[0][0], self.snake[0][1]] == 2:
            self.score = + 2
            self.print_score()
            self.fieldItems[self.snake[0][0], self.snake[0][1]] = 0

        elif self.fieldItems[self.snake[0][0], self.snake[0][1] - 1] == 2:
            self.score = + 2
            self.print_score()
            self.fieldItems[self.snake[0][0], self.snake[0][1] - 1] = 0

        # Snake got tasered
        if self.fieldItems[self.snake[0][0], self.snake[0][1]] == 3:
            self.score = - 1
            if self.score < 0:
                self.score = 0
            self.print_score()
            self.fieldItems[self.snake[0][0], self.snake[0][1]] = 0

        elif self.fieldItems[self.snake[0][0], self.snake[0][1] - 1] == 3:
            self.score = - 1
            if self.score < 0:
                self.score = 0
            self.print_score()
            self.fieldItems[self.snake[0][0], self.snake[0][1] - 1] = 0

        # Snake drunk coffee and got hyper speed
        if self.fieldItems[self.snake[0][0], self.snake[0][1]] == 4:
            self.speed = int(self.speed / 2)
            self.stdscr.timeout(self.speed)
            self.fieldItems[self.snake[0][0], self.snake[0][1]] = 0

        elif self.fieldItems[self.snake[0][0], self.snake[0][1] - 1] == 4:
            self.speed = int(self.speed / 2)
            self.stdscr.timeout(self.speed)
            self.fieldItems[self.snake[0][0], self.snake[0][1] - 1] = 0

    def activate_chick_self_defense(self):
        """
        Print the lightening bold , representing
        a taser, right next to the chick starting level 2
        but if the spot is occupied, don't print
        Generate self defense about 50% of time for level 2
        """
        if self.level == 1:
            return

        # For level 2 generates the self defense about 50% of time
        if self.level == 2:
            result = random.randint(0, 10)
            if result < 6:
                return

        if self.score >= 0:
            self_defense_coords = copy.deepcopy(self.chick)
            self_defense_coords[0] = self_defense_coords[0] - 1
            self_defense_coords[1] = self_defense_coords[1] + 1
            if self.fieldItems[self_defense_coords[0], self_defense_coords[1]] == 0:
                self.fieldItems[self_defense_coords[0],
                                self_defense_coords[1]] = 3
                self.stdscr.addstr(
                    self_defense_coords[0], self_defense_coords[1], '⚡')
                self.self_defense_coordinate = self_defense_coords

    def deactivate_chick_self_defense(self):
        """ Clean up old chicks self defense weapon """
        if self.self_defense_coordinate is not None:
            self.stdscr.addstr(
                self.self_defense_coordinate[0], self.self_defense_coordinate[1], ' ')
            self.self_defense_coordinate = None
            self.stdscr.refresh()

    def run(self):
        """ Run the program"""
        # ----- Show Menu ----------
        ret_val = self.menu_main()
        # menu_main returns true or false,
        # to continue or quit the game respectively
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
                self.speed = int(self.speed * 0.9)
                self.stdscr.timeout(self.speed)
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
            if (lvlup is True):
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
