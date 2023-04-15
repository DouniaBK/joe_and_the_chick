Joe and the chick is a simple snake game with level design architecture and story telling.  This game inspired by the character of Joe Tribiani from the world loved series, Friends. In this game the snake plays the role of Joe, chasing chicks, eating pastrami sandwiches and well sometimes he scores and othertimes he just puts his foot(tail) in his mouth and gets burned. Throughout the chick chase, Joe might be tempted by a Pastrami sandwitch to increase his score by two points or a hot chick but that might just lead to his demise if the chick took some self defense classes. As Joe scores more, he will continue to the next level, where more rewards, traps, speed and barriers will appear to increase the difficulty of the game. Joe and the chicks is designed as a fun, relaxing inbettwen thoughts and meetings type of game that boosts morals and clears the mind. The game is played on a python terminal and designed using curses, emojies and unicode characters to construct the environment. 

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
## Credit and Contact
* Images
* Code
* Contact

## UX
### How to play

This game is meant to be played in between breaks to relax, have fun and do something that doesn't require mental exhaustion and take the players mind of a stressful day.

The game revolves around the character of Joe Tribiani from Friends. The Snake (▓) plays the role of Joe, the ultimate player, who has to:

    * Catch a chick (🐤) to score points
    * Eat a pastrami Sandwich (🌯) to regain force and score 2 points
    * Avoid being tasered (⚡) and lose 1 point
    * Stay away from barriers (▩) and borders or instant death it is
    * Abstain from biting oneself
    * Have fun

The game is played using the following keys:
1. KEY_UP to move upward
2. KEY_DOWN to move downward
3. KEY_RIGHT to move right
4. KEY_LEFT to move upward
5. Press X to exit
6. Press H to Menu
7. Enter to select
8. Press P to pause the game

### Visual Design

* Menu:
<display menu screenshot>

 As the gamer enters the game console, he is asked to choose an item from the menu, play, legend or exit. The play button directs the gamer to start playing the game, the legend option, contains instructions on how to play the game. Finally the Exit options allows the player to stop the game. The menu items appear in the middle of the terminal and the item selected is highlighted for better visual contrast. The user is allowed to use Key down/up and enter to select menu items.

* The game:
< add game screenshot>

The design of the game is clean and playful adhedring to the character of Joe Tribiani's, from Friends, personality traits. The use of emojies and unicode characters inspire inner playfulness and encourage the player to continue playing. The game field is a pad created using curses. It displays clean visual borders for the player to not cross. Above the field, a score is displayed for the player to see his total score.
Throughout the game, messages will appear to show indicate the state of game to the player such as, "Game Over!" or "Congrats Joe, you scored enough to level up" or ask for an input to exit the game.

* Emojis as a design choice:

Emoticons are widely used among the targeted players' age range of this game. Emojis are often used in communication as coded language to convey different meanings in various scenarios to various groups. Hence, their use in this game can add contextual or additional emotional meaning to the players and a fun upbeat game environment. As the game is set around the dating scene of a loveable character, the emojis represent what Joe is known for, his love for sandwiches, his chick magnetism and catchphrases.

The characters in the game are:
* Snake ▓  
* Chick 🐤
* Pastrami Sandwich🌯 rewards 2 points
* Taser ⚡decrement 1 point
* Barrier ▩ instant death

### Features

#### Game Elements:

* Snake ▓ :

    The snake a.k.a Joe body consists of three body parts, which increases in size as the score increases hense increasing the difficulty of navigation and the risk of biting itself leading to the end of the game. The snakes coordinates are continously tracked to avoid appearing on another item existing on the field and also to check for collision with another item, leading to change in score or end of the game.

* Chick 🐤:

    The chick is worth the chase as it rewards 1 point but can also hurt the score if armed. The chick will appear on the field where a spot is free and conitnously reappears after being cought. 

* Taser ⚡:

    The taser is a weapon that will appear north of the chick giving the elusion that the chick is carrying it. The snake needs to navigate to the chick without touching the taser or the score will decrease of one point. However, if the score is at 0, it will remain as so. The taser is activated and then deactivated after being cought thus it will not continously accompany the chick.

* Speed:

   The speed of the snake will increase as the score increases making it more challenging to navigate the field and catch the chick.

* Pastrami Sandwich 🌯 :

    The Sandwich is a reward that will randomly appear on free coordinates in the field for Joe to give him a booster point.

* Field:

    The field is a rectangle textpad created using curses. 

* Barriers:

 The barriers are specifically designed for each level. As the player increases his score, the barriers will change position and shape to create a maze-like environment. The barriers will appear in specific coordinates where nor the snake or the other features are to avoid a premature end of the game.

 * Coffee mug:
    
    The coffee mug is a trap that gives joe super speed leading to a challenging navigation in the game. Thankfully, it will only last few seconds.

* The score:

    It is displayed outside of the game field and it increments everytime the player scores or looses points. The score of the player, also determines the level of the game:

* The level design:

    The game is designed with three levels in mind. As the player scores 4 points, he moves to the next second level and with the score of greater than 8, he moves to the third and final level. Each level is designed differently. The speed increases, the barrier maze changes, new items appear on the field making the game more and more challenging.

#### Additional Features
  The menu:
    * Home allows the player to pause the game, return to the menu and choose an item from the menu such as Legend
    * Play allows the player to enter the game
    * Legend detailed instructions on how to play the game
    * Exit allows the player to end the game.
    * Cursor feature has a try block to handle terminal incompatibility with disabling the cursor
    * Function that find item coordinates making sure it appears inside the box but not on the body of the snake
### Features Not Yet Implemented
  * Two players version (Joe and Chandler or Joe and Ross)
  * The chick avert the snake
  * The taser moves around the chick for better protection
  * Rival that hinders the chick chase.
  * The chick is not interested in Joe but rather Monica.

## Information Architecture
* Database Structure
## Data Models
The game class is devided into three section:
* Initializing the game set up 

* Menu section: includes functions that will generate, print and design the menu. including a try block to handle terminal incompatibility with disabling the cursor

* Game section: includes various functions that handle the logic of the game from checking coordinates availability, collision, generating and printing items, incrementing score and evaluating level design architecture.

* Run the game section: 
## Technologies Used
### Languages
    Python

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

### Curser

* Bug: Although executing properly within Gitpod, the command to disable the terminals cursor "curses.curs_set(0)" returns an error in the deployed version on heroku, which means that the supplied Code Institute terminal implementation does not support disabling the cursor.
The cursor will therefore be visible in the deployed version of the app, while being invisible on a local or Gitpod terminal. 

* Fix: Try block to handle terminal incompatibility with disabling the cursor. If terminal does not support invisible cursors, as the one provided in the code-institute template, curs_set will return an error.

### Chick Emoji
 * Bug: Due to the size of the chick emoji, the collision between the snake the chick was not being registered. Visually the player thinks he has hit the target but computationaly it did not due to an offset.

 * Fix: Determine if the snake ate the chick and return true if so The terminal draws the chick one cell to the left due to the emoji size. This visual offset is compensated for here by extending the radius of possible target hits.

### Taser

Bug: appears on other items
Fix: appear only if north of the chick is free

## Deployment
* Local Deployment
* Heroku Deployment