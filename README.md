Joe and the chick is a simple snake game with level design architecture and story telling.  This game inspired by the character of Joe Tribiani from the world loved series, Friends. In this game the snake plays the role of Joe, chasing chicks, eating pastrami sandwiches and well sometimes he scores and othertimes he just puts his foot(tail) in his mouth and gets burned. Throughout the chick chase, Joe might be tempted by a Pastrami sandwitch to increase his score by two points or an attractive chick but that might just lead to his demise. As Joe scores more, he will continue to the next level, where more rewards, traps, speed and barriers will appear to increase the difficulty of the game. Joe and the chicks is designed as a fun, relaxing inbettwen thoughts/meetings type of game that boosts morals and clears the mind. The game is played on a python terminal and designed using curses textpad as a field and emojis and unicode characters to construct the environment. 

# Table of Contents
## UX
* Goals
* Visual Design
* Seamless Design
## Features
* Page Elements
* Additional Features
* Features Not Yet Implemented
# Information Architecture
* Database Structure
* Data Models
## Technologies Used
* Languages
* Frameworks
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
### Goals

The goal of this fun game is to:
    * Catch a chick
    * Increase the score 
    * Avoid trappes and barriers
    * Catch a sandwich and score more points
    * Have fun
Furthermore, this game is meant to be played in between breaks to relax, have fun and do something that doesn't require mental exhaustion. 
### Visual Design

* Menu:
<display menu screenshot>

 As the gamer enters the game console, he is asked to choose an item from the menu, play, settings or exit. The play button directs the gamer to start playing, the settings option, allows the user to change the settings of the game such as the speed and level of difficulty. Finally the Exit options allows to stop the game.

* The game:
< add game screenshot>

The design of the game is clean and playful adhedring to the character of Joe Tribiani's, from Friends, personality traits. The use of emojies and unicode characters inpspire inner playfulness and encourage the player to continue playing. The game field is a pad created using curses. It displays clean borders for the gamer to not cross. 

## Bugs
* Although executing properly within Gitpod, the command to disable the terminals cursor "curses.curs_set(0)" returns an error in the deployed version on heroku, which means that the supplied terminal implementation does not support disabling the cursor.
The cursor will therefore be visible in the deployed version of the app, while being invisible on a local or Gitpod terminal. 