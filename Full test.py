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
        self.question=[("#use modulus to find the remainder when a=7 and is divided by 3","a=7"),("%","=","4"),("1") ]
        self.row_limit=len(self.question[0])
        self.question_comments=self.question[0]
    def insert_self_code(self,code):
        for i in self.question[0]:
            code+=i
        return code
    def execute(self,code,str):
        a=0
        for row in code:
            str+="\n    "
            str+=row
        str+="\n    return a"
        str+="\na()"
        print(str)
        str+=""
        try:
            a=exec_with_return(str)
            check=self.check_code(a)
            if check==True:
                return "reset_question"
            return a
        except Exception as e:
            print(e)
            return e
    def check_code(self,a):
        if str(a)==str(self.question[2]):
            return True
        
code_str="""def a():\n"""
text=Text()
question=Question()
user_text=[]
for i in range(question.row_limit):
    user_text+=[question.question_comments[i]]
user_text+=[""]
user_row=question.row_limit
a=exec_with_return("""def a():\n    a=16\n    return a\na()""")
print(a)
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
                elif button_press==pygame.K_HASH:
                    user_text=[""]
                    user_row=0
                if (button_press!=pygame.K_RETURN) and (button_press!=pygame.K_BACKSPACE) and (button_press!=pygame.K_TAB) and( button_press!=pygame.K_ESCAPE) and button_press!=pygame.K_HASH:
                    button_press=event.unicode
                    user_text[user_row]+=button_press
    text.renderall(display,20,(255,255,255),user_text,user_row)
    pygame.display.update()
    clock.tick(60)
    nulll=[("code already there","code lines these take up(they cannot be changed)"),("tihings the checker wants"),("output/return value the checker wants ")]