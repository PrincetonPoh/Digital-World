from kivy.base import runTouchApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from libdw import sm
import time
walls = 'IIII--------------------------------'
#### Game items
class Sprite():
    def __init__(self):
        self.sprite = ['  ', '>'] 
        self.top = self.sprite[0]
        self.bottom = self.sprite[1]
        self.life = 3

    def jump(self):
        self.sprite[0], self.sprite[1] = self.sprite[1], self.sprite[0]
        self.top = self.sprite[0]
        self.bottom = self.sprite[1]
Player = Sprite()

class Obstacle():
    def __init__(self):
        self.area_top = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','-|','-|',' ',' ',' ',' ',' ']
        self.area_bottom = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','-|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.thing_to_add = ' '
        self.string_area_top = ''
        self.string_area_bottom = ''

    def advance_top(self):
        self.area_top.pop(0)
        self.area_top.append(self.thing_to_add)
    
    def advance_bottom(self):
        self.area_bottom.pop(0)
        self.area_bottom.append(self.thing_to_add)
    
    def summon(self):
        self.thing_to_add = '-|'

    def un_summon(self):
        self.thing_to_add = ' '  
    
    def string(self):
        self.string_area_top = ''
        for i in range(len(self.area_top)):
            self.string_area_top += self.area_top[i]
        
        self.string_area_bottom = ''
        for k in range(len(self.area_bottom)):
            self.string_area_bottom += self.area_bottom[k]

    
Obs = Obstacle()

    


#### State Machine
class CM(sm.SM):
    start_state = 0
    
    def get_next_values(self, state, inp):
        ## flipping gravity
        if state == 0 and inp =='w':
            next_state = 1
            Player.jump()
            game = walls + '\n' + Player.top + Obs.string_area_top + '\n' + Player.bottom + Obs.string_area_bottom + '\n' + walls
            output = game

        elif state == 1 and inp == 's':
            next_state = 0
            Player.jump()
            # Obs.advance_top()
            # Obs.string()
            game = walls + '\n' + Player.top + Obs.string_area_top + '\n' + Player.bottom + Obs.string_area_bottom + '\n' + walls
            output = game

        ## summoning obstacle
        elif state == 0 and inp == 'up':
            next_state = 0
            Obs.summon()
            Obs.advance_top()
            Obs.string()
            Obs.un_summon()  
            game = walls + '\n' + Player.top + Obs.string_area_top + '\n' + Player.bottom + Obs.string_area_bottom + '\n' + walls
            output = game  
        elif state == 1 and inp == 'up':
            next_state = 1
            Obs.summon()
            Obs.advance_top()
            Obs.string()
            Obs.un_summon()  
            game = walls + '\n' + Player.top + Obs.string_area_top + '\n' + Player.bottom + Obs.string_area_bottom + '\n' + walls
            output = game

        elif state == 0 and inp == 'down':
            next_state = 0
            Obs.summon()
            Obs.advance_bottom()
            Obs.string()
            Obs.un_summon()  
            game = walls + '\n' + Player.top + Obs.string_area_top + '\n' + Player.bottom + Obs.string_area_bottom + '\n' + walls
            output = game  
        elif state == 1 and inp == 'down':
            next_state = 1
            Obs.summon()
            Obs.advance_bottom()
            Obs.string()
            Obs.un_summon()  
            game = walls + '\n' + Player.top + Obs.string_area_top + '\n' + Player.bottom + Obs.string_area_bottom + '\n' + walls
            output = game           

        ## win condition
        elif state == 0 and inp == 'win':
            next_state = 3
            game = 'GAME OVER \n \n you win :) \n \n good things never last'
            output = game
        elif state == 1 and inp == 'win':
            next_state = 3
            game = 'GAME OVER \n \n you win :) \n \n good things never last'
            output = game

        elif state == 3:
            next_state = 3
            game = 'GAME OVER \n \n you win :) \n \n good things never last'
            output = game
        
        ## lose condition
        elif state == 0 and inp == 'GG':
            next_state = 4
            game = 'GAME OVER \n \n you win :) \n \n good things never last'
            output = game
        elif state == 1 and inp == 'GG':
            next_state = 4
            game = 'GAME OVER \n \n you win :) \n \n good things never last'
            output = game

        elif state == 4 :
            next_state = 4
            game = 'GAME OVER \n \n you LOSE \n better luck next time :/ \n \n Please run kivy again to play again'
            output = game
        
        ## when ppl anyhow press :)
        elif state == 0 and inp != 'w':
            next_state = 0
            Obs.advance_top()
            Obs.advance_bottom()
            Obs.string()
            game = walls + '\n' + Player.top + Obs.string_area_top + '\n' + Player.bottom + Obs.string_area_bottom + '\n' + walls
            output = game
        elif state == 1 and inp != 's':
            next_state = 1
            Obs.advance_top()
            Obs.advance_bottom()
            Obs.string()
            game = walls + '\n' + Player.top + Obs.string_area_top + '\n' + Player.bottom + Obs.string_area_bottom + '\n' + walls
            output = game
        self.state = next_state    #usually the code works seperately without this line but somehow when i ran it with this whole progam, it doesnt

        return next_state, output

c = CM()
c.start()

#### GUI part
Builder.load_string('''
<Root>:
    Display:
        
<Display>:
    game:game
    Label:
        color: 1, 0, 0, 1
        id: game
        text: 'hi'
        pos: 300, 300
    Label:
        text: 'Press  w  /  s  to move'
        pos: 300,450

''')

class Root(Widget):
    pass

class Display(Widget):
    game = ObjectProperty()
    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)
        Clock.schedule_interval(self.update2, 1/8)
        self.sm_inp = 'A'

        self.count = 0
        self.level1 = [' ',' ',' ','down',' ',' ',' ',' ',' ',' ',' ',' ','up',' ',' ',' ',' ',' ','down',' ',' ',' ',' ',' ',' ','up',' ',' ',' ','down',' ',' ',' ',' ',' ',' ',' ',' ','up',' ',' ',' ',' ',' ','down','down',' ',' ',' ',' ',' ','up',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

        Window.bind(on_key_down = self.key_action)

    # to update GUI about the changes from the state-machine
    def update2(self, *args):
        # collision
        if Obs.area_top[0] == '-|' and Player.top == '>':
            self.sm_inp = 'GG'
        elif Obs.area_bottom[0] == '-|' and Player.bottom == '>':
            self.sm_inp = 'GG' 

        # interate through level1 and summon the obstacles
        elif self.count < len(self.level1):
            self.sm_inp = self.level1[self.count]
        
        x, y = c.get_next_values(c.state, self.sm_inp)
        self.game.text = y
        if self.count < len(self.level1)-1:
            self.count += 1
        # indicate that the obstacle course is over with a 'win'
        elif self.count == len(self.level1)-1:
            self.sm_inp = 'win'
            self.count += 1
        elif self.count == 32:
            self.count = 0
        else:
            self.sm_inp = 'A'
        pass

    def key_action(self, *args):
        self.sm_inp = args[3]
        x, y = c.get_next_values(c.state, self.sm_inp)
        self.game.text = y
       

class DeceptiveApp(App):
    def build(self):
        return Root()

DeceptiveApp().run()
