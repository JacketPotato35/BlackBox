import pygame
import sys
from pygame.locals import QUIT
import numpy as np
import os 
from subprocess import run
from exec import exec_with_return 
import sys


pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 1320, 780
display = pygame.display.set_mode((screen_width, screen_height))
display.fill((126,126,126))
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
        self.question=[["#use modulus to find the remainder when a=7 and is divided by 3","a=7"],["%","=","3"],["1"] ]
        self.row_limit=len(self.question[0])
        self.question_comments=self.question[0]
        self.checkers=self.question[1]
    def execute(self,code,str):
        a=0
        for row in code:
            str+="\n    "
            str+=row
        str+="\n    return a"
        str+="\na()"
        str+=""
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
    def reset(self,new_question):
        print(new_question)
        self.question=[(new_question[0]),(new_question[1]),(new_question[2])]
        print(self.question)
        self.row_limit=len(self.question[0])
        self.question_comments=self.question[0]
        self.checkers=self.question[1]
        
        

question_array=[["#use the exponential operator to the power of to bring a to the power of 5","a=2"],["**"],["32"]]

text=Text()
question=Question()
user_text=[]
code_str="""def a():\n"""
for i in range(question.row_limit):
    user_text+=[question.question_comments[i]]
user_text+=[""]
user_row=question.row_limit
first=[("#use modulus to find the remainder when a=7 and is divided by 3","a=7"),("%","=","4"),("1") ]
while True:
    for event in pygame.event.get():
        display.fill((126,126,126))
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
                button_press=event.key
                if (button_press==pygame.K_DOWN or button_press==pygame.K_RETURN) and user_row+1==len(user_text) and user_row<18:
                    user_text+=[""]
                if button_press==pygame.K_UP and user_row>=question.row_limit+1:
                    user_row-=1
                elif button_press==pygame.K_DOWN and user_row<18:
                    user_row+=1
                elif button_press==pygame.K_RETURN and user_row<18:
                    user_row+=1
                    user_text.insert(user_row,"")
                elif button_press==pygame.K_BACKSPACE:
                    user_text[user_row]=user_text[user_row][:len(user_text[user_row])-1]
                elif button_press==pygame.K_TAB:
                    user_text[user_row]+="      "
                elif button_press==pygame.K_ESCAPE:
                    text.render(display,str(question.execute(user_text,code_str)),screen_width/8,screen_height/7*6,20, (255,0,0))
                    check=question.execute(user_text,code_str)
                    if check=="check passed":
                        question.reset(question_array)
                        user_text=[]
                        code_str="""def a():\n"""
                        for i in range(question.row_limit):
                            user_text+=[question.question_comments[i]]
                        user_text+=[""]
                        user_row=question.row_limit
                        print(question.question)
                elif button_press==pygame.K_HASH:
                    user_text=[]
                    code_str="""def a():\n"""
                    for i in range(question.row_limit):
                        user_text+=[question.question_comments[i]]
                    user_text+=[""]
                    user_row=question.row_limit
                if (button_press!=pygame.K_RETURN) and (button_press!=pygame.K_BACKSPACE) and (button_press!=pygame.K_TAB) and( button_press!=pygame.K_ESCAPE) and button_press!=pygame.K_HASH:
                    button_press=event.unicode
                    user_text[user_row]+=button_press
    text.renderall(display,20,(255,255,255),user_text,user_row)
    pygame.display.update()
    clock.tick(60)
    nulll=[("code already there","code lines these take up(they cannot be changed)"),("tihings the checker wants"),("output/return value the checker wants ")]