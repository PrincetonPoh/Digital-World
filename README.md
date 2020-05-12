---
title: 'Digital World 10.009 Final Assignment'
disqus: hackmd
---

Digital World 10.009 Final Assignment
===

## Gravity Guy

### Table of Contents

1. Motivation
2. How to play the game
3. The code
4. Reflection

## Motivation

After asking around to see what my friends are coding, I realised a number of them are doing adventure style game (similar to the example given). Hence I decided that I am definitely not doing that. I thought about what elements can I change to make my game different. 

I was inspired by my childhood game called gravity guy where you flip the direction of gravity to avoid obstacles. I wanted to create a text based reaction game where there is immediate user feedback. However, it requires the installation of the keyboard module which doesn't come directly with the python installation. Knowing that kivy can code for keyboard events, I thought why not also make a simple GUI as well.

## How to play the game

It is really simple. Just use the controls 'w' and 's' to move the cursor out of the way of sharp and pointy obstacles that are coming at you. :)

The Code
---
The code is split into 3 sections: 'Game Items', 'State Machine', 'GUI part'

Game Items: OOP really helps to break down the task into more manageable chunks. I was able to build and test each individual functions/attributes before moving to the next. Being able to make visible progress as I code helps.

```codehilite=
#### Game items
class Sprite():
    def __init__(self):
        ...

    def jump(self):
        ...

class Obstacle():
    def __init__(self):
        ...

    def advance_top(self):
        ...
    
    def advance_bottom(self):
        ...
    
    def summon(self):
        ...

    def un_summon(self):
       ...
    
    def string(self):
        ...
```
<br />

State Machine: This is where I code in most of the logic involved. e.g movement, summoning of obstacles, flipping the gravity, collision, win and losing criteria.
State 0 = cursor(bottom);
State 1 = cursor(top);
State 3 = win;
State 4 = lose;

```codehilite=
#### State Machine
class CM(sm.SM):
    start_state = 0
    
    def get_next_values(self, state, inp):
        ## flipping gravity
        ...

        ## summoning obstacle
        ...           

        ## win condition
        ...
        
        ## lose condition
            ...
        
        ## when ppl anyhow press :)
            ...
        return next_state, output
```
<br />

GUI part: Kivy is split into 2 sections. The first portion is Builder.load_string() which is used for the styling of the objects (kinda like css). The second portion is where the object classes are defined. The toughest part is trying to integrate kivy with the requirements of the statemachine (especially in the update2 function)

```codehilite=
class Display(Widget):
    # to update GUI about the changes from the state-machine
    def update2(self, *args):
        # collision
        ... 

        # interate through level1 and summon the obstacles
        ...
        
        # update statemachine
        x, y = c.get_next_values(c.state, self.sm_inp)
        ...

        # indicate that the obstacle course is over with a 'win'
        

    def key_action(self, *args):
        ...
```
<br />

## Reflection

This is the first few times I coded from scratch and so it took way longer than expected. I can really see the value of OOP. It makes designing more flexible as I can add/remove functions without affecting the core function of the game. Overall, this was a good project to do for me to dip my toes into coding.


> Video of gameplay: https://www.youtube.com/watch?v=W6rsWfqAGK0&feature=youtu.be



