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
### How to play

This game is meant to be played in between breaks to relax, have fun and do something that doesn't require mental exhaustion and take the players mind of a stressful day.

The game revolves around the character of Joe Tribiani from Friends. The Snake (▓) plays the role of Joe, the ultimate player, he has to:
    * Catch a chick (🐤) to score 1 point
    * Eat a pastrami Sandwich (🌯) to regain force and score 2 points
    * Avoid being tasered (⚡) and lose 1 point
    * Stay away from barriers (▩) and borders or instant death it is
    * Abstain from biting oneself
    * Have fun
 
### Visual Design

* Menu:
<display menu screenshot>

 As the gamer enters the game console, he is asked to choose an item from the menu, play, legend or exit. The play button directs the gamer to start playing the game, the legend option, contains instructions on how to play the game. Finally the Exit options allows the player to stop the game.

* The game:
< add game screenshot>

The design of the game is clean and playful adhedring to the character of Joe Tribiani's, from Friends, personality traits. The use of emojies and unicode characters inspire inner playfulness and encourage the player to continue playing. The game field is a pad created using curses. It displays clean visual borders for the player to not cross. Above the field, a score is displayed for the player to see his total score.
Throughout the game, messages will appear to show indicate the state of game to the player such as, "Game Over!" or "Congrats Joe, you scored enough to level up" or ask for an input to exit the game.

The characters in the game are:
    * Snake ▓  
    * Chick 🐤
    * Pastrami Sandwich🌯
    * Taser ⚡
    * Barrier ▩

### Features
* Page Elements
* Additional Features

* Emojis:

Emoticons are wildly used among the targeted players of this game, they can be used as their own language to convey different meanings in various scenarios. Hence, their use can add contextual or additional emotional meaning to the player and a fun upbeat game environment. As the game is set around the dating scene of a loveable character, the emojis represent what Joe is known for, his love for sandwiches, his chick magnetism and catchphrases.

* Snake ▓ :

    The snake a.k.a Joe body consists of three body parts, which increases in size as the score increases hense increasing the difficulty of navigation and the risk of biting itself leading to the end of the game. The snakes coordinates are continously tracked to avoid appearing on another item existing on the field and also to check for collision with another item, leading to change in score or end of the game.

* Chick 🐤:

    The chick is worth the chase as it rewards 1 point but can also hurt the score if armed. The chick will appear on the field where a spot is free and conitnously reappears after being cought.

* Taser ⚡:

    The taser is a weapon that will appear north of the chick giving the elusion that the chick is carrying it. The snake needs to navigate to the chick without touching the taser or the score will decrease of one point. However, if the score is at 0, it will remain as so. The taser is activated and then deactivated after being cought thus it will not continously accompany the chick.

* Speed :

   The speed of the snake will increase as the score increases making it more challenging to navigate the field and catch the chick.

* Pastrami Sandwich 🌯 :

    The Sandwich is a reward that will randomly appear on free coordinates in the field for Joe to give him a booster point.

* Field :

    The field is a rectangle textpad created using curses. 

* Barriers:

 The barriers are specifically designed for each level. As the player increases his score, the barriers will change position and shape to create a maze-like environment. The barriers will appear in specific coordinates where nor the snake or the other features are to avoid a premature end of the game.

 * Coffee mug:
    
    The coffee mug is a trap that gives joe super speed leading to a challenging navigation in the game. Thankfully, it will only last few seconds.

* Features Not Yet Implemented












## Bugs
* Although executing properly within Gitpod, the command to disable the terminals cursor "curses.curs_set(0)" returns an error in the deployed version on heroku, which means that the supplied terminal implementation does not support disabling the cursor.
The cursor will therefore be visible in the deployed version of the app, while being invisible on a local or Gitpod terminal. 



Next steps:
level 1


level 2


level 3