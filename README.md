Joe and the chick is a simple snake game with level design architecture.  The game is inspired by the character of Joe Tribiani from the world loved series, Friends. In this game the snake plays the role of Joe, chasing chicks, eating pastrami sandwiches and well sometimes he scores and othertimes he just puts his foot(tail) in his mouth and gets burned. Throughout the chick chase, Joe might be tempted by a Pastrami sandwitch to increase his score by two points or a hot chick but that might just lead to his demise if the chick took some self defense classes. As Joe scores more, he will continue to the next level, where more rewards, traps, speed and barriers will appear to increase the difficulty of the game. Joe and the chicks is designed as a fun, relaxing inbettwen thoughts and meetings type of game that boosts morals and clears the mind. The game is played on a python terminal and designed using curses, emojies and unicode characters to construct the environment. 

# Table of Contents
## Goals
* How to play
* Visual Design
## Features
* Page Elements
* Additional Features
* Features Not Yet Implemented
# Information Architecture
* Database Structure
* Data Models
## Technologies Used
* Languages
* Libraries
* Packages
* Platforms
* Other Tools
## Testing
* Automated Testing
* Manual Testing
* Bugs
## Deployment
* Local Deployment
* Heroku Deployment
## Credit and Developer's story
* Code
* Developer

## UX
### How to play

This game is meant to be played in between breaks to relax, have fun and do something that doesn't require mental exhaustion and take the players mind of a stressful day.

The game revolves around the character of Joe Tribiani from Friends. The Snake (▓) plays the role of Joe, the ultimate player, who has to:

    * Catch a chick (🐤) to score points
    * Eat a pastrami Sandwich (🌯) to regain force and score 2 points
    * Avoid being tasered (⚡) by a chick and lose 1 point
    * Have some coffee ☕ to increase his speed
    * Stay away from barriers (▩) and borders or instant death it is
    * Abstain from biting oneself
    * Have fun!

The game is played using the following keys:
1. KEY_UP to move upward
2. KEY_DOWN to move downward
3. KEY_RIGHT to move right
4. KEY_LEFT to move upward
5. Press X to exit the game or select it in the menu
6. Press any key to return to the Menu from Legend
7. Enter to select

### Visual Design

* Menu:
![the menu ](images/Screenshot-menu.png) 

 As the gamer enters the game console, he is asked to choose an item from the menu: play, legend or exit. The play button directs the gamer to start playing the game. The legend option, contains instructions on how to play the game. Finally, the exit option allows the player to stop the game. The menu items appear in the middle of the terminal and the item selected is highlighted for better visual contrast. The user is allowed to use Key down/up and enter to select menu items.

* The game:

The design of the game is clean and playful adhedring to the character of Joe Tribiani's, from Friends, personality traits. The use of emojies and unicode characters inspire inner playfulness and encourage the player to continue playing. The game field is a pad created using curses. It displays clean visual borders for the player to not cross. Above the field, a score is displayed for the player to see his total score.
Throughout the game, messages will appear to show indicate the state of game to the player such as, "Game Over!" or "You've got game, player! Next Level" or ask for an input to exit the game.

* Emojis as a design choice:

Emoticons are widely used among the targeted players' age range of this game. Emojis are often used in communication as coded language to convey different meanings in various scenarios to various groups. Hence, their use in this game can add contextual or additional emotional meaning to the players and a fun upbeat game environment. As the game is set around the dating scene of a loveable character, the emojis represent what Joe is known for, his love for sandwiches, his chick magnetism and catchphrases.

The characters in the game are:
* Snake ▓  
* Chick 🐤
* Pastrami Sandwich 🌯 rewards 2 points
* Taser ⚡decrement 1 point
* Barrier ▩ instant death
* Cofee mug ☕ increase speed by 25%

### Features

#### Game Elements:

* Snake ▓ :

    The snake a.k.a Joe body initially consists of three body parts, which increases in size as the score increases hense increasing the difficulty of navigation and the risk of biting itself leading to the end of the game. The snakes coordinates are continously tracked to avoid appearing on another item existing on the field and also to check for collision with another item, leading to change in score or end of the game.

* Chick 🐤:

    The chick is worth the chase as it rewards 1 point but can also hurt the score if armed. The chick will appear on the field where a spot is free and continuously reappears after being cought. 

* Taser ⚡:

    The taser is a weapon that will appear north of the chick giving the elusion that the chick is carrying it. The snake needs to navigate to the chick without touching the taser or the score will decrease by one point. However, if the score is at 0, it will remain as so. The taser is activated and then deactivated after being cought thus it will not continously accompany the chick.

* Speed:

   The speed of the snake will increase as the score increases making it more challenging to navigate the field and catch the chick.

* Pastrami Sandwich 🌯 :

    The Sandwich is a reward that will randomly appear on free coordinates in the field for Joe to give him a booster point without increasing speed.

* Field:

    The field is a rectangle textpad created using curses. 

* Barriers:

 The barriers are specifically designed for each level. As the player increases his score, the barriers will change position and shape to create a maze-like environment. The barriers will appear in specific coordinates where neither the snake nor the other features are, to avoid a premature end of the game.

 * Coffee ☕:
    
    The coffee mug is a trap that gives joe super speed leading to a challenging navigation in the game. The speed is increased by 25%.

* The score:

    It is displayed outside of the game field and it increments everytime the player scores or looses points. The score of the player, also determines the level of the game:

* The level design:

    The game is designed with three levels in mind. As the player scores 5 points, he moves to the next, second level and then third level. Each level is designed differently. The speed increases, the barrier maze changes, new items appear on the field making the game more and more challenging.

#### Additional Features
  
The menu:
    
 * Play allows the player to enter the game
 * Legend detailed instructions on how to play the game
 * Exit allows the player to end the game.
 * Cursor feature has a try block to handle terminal incompatibility with disabling the cursor
 * Functions that find item coordinates making sure it appears inside the box but not on the body of the snake
### Features Not Yet Implemented

  * Two players version (Joe and Chandler or Joe and Ross)
  * The chick moves to escape the snake
  * The taser randomly moves around the chick for better protection
  * Introduction of a rival that hinders the chick chase
  * The chick is not interested in Joe but rather Monica
  * Pause the game feature with an input

## Information Architecture
## Data Models

The game class is divided into three sections:

1. Initialization of the game set up and helper functions that avoid crashing the terminal

2. Menu and messages section: includes functions that will generate, print and design the menu. including a try block to handle terminal incompatibility to disable the cursor. The messages displayed to guide the player are also included in this section.

3. Game section: includes various functions that handle the logic of the game from checking coordinates availability, collision, generating and printing items, incrementing score, creating the level design and finally running the game. 

## Technologies Used
### Languages
    I used python to develop and design the game logic.
### Libraries

* Curses : find the link [here](https://docs.python.org/3/howto/curses.html) for a detailed description.
* Numpy : to install numpy, simply type in the terminal : pip3 install numpy
* Random
* Time
* Copy
### Platforms

 **Github**
 * Storing code remotely and deployment.

 **Gitpod**
 * IDE for project development.
 * Other Tools

**Wikipedia**
 * For emojis and unicode characters 
## Bugs

### Cursor Deactivation

* Bug: Although executing properly within Gitpod, the command to disable the terminals cursor "curses.curs_set(0)" returns an error in the deployed version on Heroku, which means that the supplied Code Institute terminal implementation does not support disabling the cursor.
The cursor will therefore be visible in the deployed version of the app, while being invisible on a local or Gitpod terminal. 

* Fix: Try block to handle terminal incompatibility with disabling the cursor. If a terminal does not support invisible cursors, as the one provided in the Code-Institute template, curs_set will return an error. The try block lets the game continue without crashing.

### Chick Emoji

 * Bug: Due to the size of the chick emoji, the collision between the snake the chick was not being registered consistently. Visually the player thinks he has hit the target but computationaly it did not due to the visual offset. This is due to the fact, that chick emoji as well as many other emojis occupy two cells when drawn by the terminal, while only being linked to a single coordinate computationally.

 * Fix: This behavior was taken into account when determining if the snake ate the chick, by extending the radius of the collision detection algorithm to two cells instead of one.

### Taser

* Bug: Appears on top of other items.
* Fix: Place only if north of the chick is free.

* Bug/problem: Appeared too often and thus made the game too hard.
* Fix: Add a probability of 50% of appearance.

### General for all Emojis

* Bug: Emojis visually occupy more than one cell within the terminal, which leads to incorrect 
detection behavior.
* Fix: This terminal drawing behavior needed to be taken into account during collision detection. 

### Calculation of barrier position

* Bug: Barriers looked different depending on the online terminal and the Gitpod terminal, which was due to an incorrect calculation of the barrier position.
* Fix: Adapted the terminal position to take into account only the game field.
           
### The curses addstr function
* Bug: the curses function addstr() would on occasion crash the application if writing in the terminal failed.
* Fix: The fix was to wrap addstr() into a try block, which avoids crashing the game if addstr returns an error.

### Terminal flagged errors
* Problem: line too long (86 > 79 characters) was often flagged but since it didn't affect the program and the testing process, I chose to disable quality assurance in some cases as shown below.
* Fix : # noqa

### Heroku terminal text-size error:

* Bug: the deployed heroku terminal could not display the full size text without crashing.
* Solution: the text size and the coordinates had to be adjusted to fit the terminal.

## Known bugs:
### Heroku terminal crashing:
* Bug: the game sometimes crashes randomly or misprints a section of the game in the heroku terminal in a none deterministic way.
* Solution: Since the Heroku terminal misbehaves randomly but the Gitpod terminal works perfectly, I was not able to solve the issue.

## Testing
### Python Interactive Debugging:
![interactive debugging ](images/screenshot_debug_coordinates.png)
- Logical error and bugs were resolved using the interactive Python debugging console, to manully step through the code line by line and inspecting the progression of local and global variables. E.g. to improve collision detection, between the snake and the chick due to the terminals specific drawing behavior of emojis. 


### Manual Testing
- The game has been thoughly tested in the local(Gitpod) terminal as well as the Heroku terminal. Error resolved in this manner were often related to the size of the text or barriers not being displayed equally in both terminals.

- For learning purposes, the menu and the object-oriented version of the game were drafted in seperate files before being copied back into run.py, where development continued. The files menu.py and game.py have been deleted.

- The entire code has been validated by the CI Python Linter(PEP8 Python validator) provided by Code Institute and no errors were reported.

## Deployment

 The game was development and deployed using the Code Institute's mock terminal for Heroku. 

 * I followed the steps provided by the Code Institute for a smooth        
     deployment, which are:
  1. Fork the python template repository
  2. Develop the initial game program
  3. Create the Heroku app
  4. Add the building backs to Python and NodeJS as instructed
  5. Link the Heroku app to the github repository Joe and the chick
  6. Deploy and then view app, proceed with developing and testing the game.

## Credit and Contact

* Code
    Part of the basic game structure using curses, have been done follwoing a course on how to use curses provided by Nikhil Kumar Singh also known as Indian phythonista. These sections are mentioned in the code.

* Developer's story:

    Growing up, the timeless series Friends, was one of my favorites as it continuously cheered me up and thus, I wanted to bring
    these funny moments and hilarious and unforgettable lines to the game. Joe's outgoing, halfwitted personality and love of dating women (chicks) inspired me in creating and developing this chasing game. I have further plans to add other characters from Friends injecting more humor and challeges to the game. I hope you have fun playing this game.
    I am available at douniazedbacha@gmail.com .