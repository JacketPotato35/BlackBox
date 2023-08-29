import pygame
import sys
from pygame.locals import QUIT
import numpy as np
import os 
from subprocess import run
from Terminal.exec import exec_with_return 
import sys
import random

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height =display.get_size()
background_colour=((63,63,63))
display.fill(background_colour)
pygame.display.set_caption('hackbox')
class Text():

    def __init__(self):
        self.font = pygame.font.SysFont("Comic Sans", 20)
        self.text = self.font.render(("hello"), True, (155, 155, 155))

    def render(self, display, text, locx, locy, font_size, colour):
        self.font = pygame.font.SysFont("Courier", font_size)
        self.text = self.font.render((text), True, colour)
        size = self.font.size(text)
        display.blit(self.text, (locx, locy))

    def renderall(self,display, font_size, colour,list, user_row):
        y=10
        row_num=1
        for row in list:
            if row_num==(user_row+1):
                self.render(display,str(row_num),0,y ,font_size,colour) 
                self.render(display, str(row)+"□", 40, y , font_size, colour)
            else:
                self.render(display,str(row_num),0,y ,font_size,colour) 
                self.render(display, row, 40, y , font_size, colour)
            y+=40
            row_num+=1
        
class Question():
    def __init__(self):
        self.a=0
        self.question=[["mod","    #use modulus to find the remainder when a=7 and is divided by 3","    a=7"],["%","=","3"],["1"]]
        self.row_limit=len(self.question[0])
        self.question_comments=self.question[0]
        self.checkers=self.question[1]

    def execute(self,code):
        a=0
        str=""""""
        for row in code:
            str+="\n"
            str+=row
        str+=""
        print(str)
        try:
            a=exec_with_return(str)
            check=self.check_code(a,str)
            return check
        except Exception as e:
            return e
    def check_code(self,a,code_str):
        for i in self.checkers:
            if i not in code_str :
                return a
        if [str(a)]==self.question[2]:
            return "check passed"
        else:
            return a
    def reset(self,new_question):
        self.question=[(new_question[0]),(new_question[1]),(new_question[2])]
        self.row_limit=len(self.question[0])
        self.question_comments=self.question[0]
        self.checkers=self.question[1]
        
 

class Terminal():
    def __init__(self):
        self.text=Text()
        self.question=Question()
        self.user_text=[]
        for i in range(self.question.row_limit):
            self.user_text+=[self.question.question_comments[i]]
        self.user_text+=[""]
        self.user_row=self.question.row_limit
        self.user_text[self.user_row]+="    "
        self.user_text+=["    return a"]
        self.user_text+=[f"{self.question.question[0][0]}()"]
        self.question_array=[
            [["expo","    #use the exponential operator to bring a to the power of 5","    a=2"],["**","5"],["32"]],
            [["modulus","    #use modulus to find the remainder when a=7 and is divided by 3","    a=7"],["%","=","3"],["1"]],
            [["floordiv","    #use floor division to divide a by 3 when a=11","    a=11"],["//","3"],["3"]],
            [["add","    #use addition to add 5 to a when a=7","    a=7"],["+","5"],["12"]],
            [["sub","    #use subtraction to subtract 8 when a=11","    a=11"],["-","8"],["3"]]
            ]

    def clear(self):
        self.user_text=[]
        for i in range(self.question.row_limit):
            self.user_text+=[self.question.question_comments[i]]
        self.user_text+=[""]
        self.user_row=self.question.row_limit
        self.user_text[self.user_row]+="    "
        self.user_text+=["    return a"]
        self.user_text+=[f"{self.question.question[0][0]}()"]
    
    def run(self, display):
        while True:
            for event in pygame.event.get():
                display.fill((background_colour))
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                        button_press=event.key
                        if (button_press==pygame.K_DOWN or button_press==pygame.K_RETURN) and self.user_row+1==len(self.user_text) and self.user_row<18:
                            self.user_text+=["    "]  
                        if button_press==pygame.K_UP and self.user_row>=self.question.row_limit+1:
                            self.user_row-=1
                        elif button_press==pygame.K_DOWN and self.user_row<18 and self.user_row<len(self.user_text)-3:
                            self.user_row+=1
                        elif button_press==pygame.K_RETURN and self.user_row<18:
                            self.user_row+=1
                            self.user_text.insert(self.user_row,"    ")
                        elif button_press==pygame.K_BACKSPACE:
                            if not len(self.user_text[self.user_row])<=4:
                                self.user_text[self.user_row]=self.user_text[self.user_row][:len(self.user_text[self.user_row])-1]
                        elif button_press==pygame.K_TAB:
                            self.user_text[self.user_row]+="    "
                        elif button_press==pygame.K_ESCAPE:
                            self.text.render(display,str(self.question.execute(self.user_text)),screen_width/8,screen_height/7*6,20, (255,0,0))
                            self.check=self.question.execute(self.user_text)
                            if self.check=="check passed":
                                self.question.reset(self.question_array[random.randint(0,4)])
                            self.clear()
                        elif button_press==pygame.K_HASH:
                            print(self.user_row, self.user_text)
                            self.clear()
                        if (button_press!=pygame.K_RETURN) and (button_press!=pygame.K_BACKSPACE) and (button_press!=pygame.K_TAB) and( button_press!=pygame.K_ESCAPE) and button_press!=pygame.K_HASH:
                            button_press=event.unicode
                            self.user_text[self.user_row]+=button_press
            self.text.renderall(display,20,(255,255,255),self.user_text,self.user_row)
            pygame.display.update()
            clock.tick(60)
            self.nulll=[("code already there","code lines these take up(they cannot be changed)"),("tihings the checker wants"),("output/return value the checker wants ")]
terminal=Terminal()
terminal.run(display)