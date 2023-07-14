import pygame
import sys
from pygame.locals import QUIT
import numpy as np
import os 
from subprocess import run
from exec import exec_with_return 
import sys
import random
from dataclasses import dataclass
import sqlite3

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
        print(text)
        self.font = pygame.font.SysFont("Courier", font_size)
        self.text = self.font.render((str(text)), True, colour)
        display.blit(self.text, (locx, locy))

    def renderall(self,display, font_size, colour,list, user_row):
        y=10
        row_num=1
        for row in list[0]:
            if row_num==(user_row+1):
                self.render(display,str(row_num),0,y ,font_size,colour) 
                self.render(display, str(row)+"□", 40, y , font_size, colour)
            else:
                self.render(display,str(row_num),0,y ,font_size,colour) 
                self.render(display, row, 40, y , font_size, colour)
            y+=40
            row_num+=1

@dataclass
class Question():
    function_name : str
    comments : str
    pre_written_code: list
    end_written_code : list
    conditions : list 
    answer : str    


def convert_2_string(question: Question, user_code):
    code_str = f"def {question.function_name}():"+"\n"
    code_str += "\t" + (question.comments or "") +"\n"
    code_str += "\t" + (question.pre_written_code or "")+"\n"
    code_str += "\t" + (user_code or "")+"\n"
    code_str += "\t" + (question.end_written_code or "")+"\n"
    code_str += f"""{question.function_name}()"""
    return code_str

class Terminal():
    def __init__(self):
        self.text=Text()
        question_parts=self.get_random_from_table()
        self.question=Question(question_parts[0],question_parts[1],question_parts[2],question_parts[3],question_parts[4],question_parts[5])
        self.user_text=[self.question_2_array()]
        self.start_limit=2+len(self.str_2_list(self.question.pre_written_code))
        self.end_limit=1+len(self.str_2_list(self.question.end_written_code))
        self.user_row=self.start_limit+1
        print(self.question_2_array())
        self.user_text=[self.question_2_array()]
        print(self.start_limit,self.end_limit)

    def question_2_array(self):
        question_array=[]
        question_array+=[f"""def {self.question.function_name}():"""]
        question_array+=[f"""\t{self.question.comments}"""]
        pre_written_code = self.str_2_list(self.question.pre_written_code)
        for question_line in pre_written_code:
            question_array+=[f"""\t{question_line}"""]
        question_array+=[""]
        end_written_code = self.str_2_list(self.question.end_written_code)
        for question_line in end_written_code:
            question_array+=[f"""\t{question_line}"""]
        question_array+=[f"""{self.question.function_name}()"""]
        return question_array
        
    def str_2_list(self, str):
        list = str.strip("""]['""").split(', ')
        return list

    def get_random_from_table(self):
        connection_obj = sqlite3.connect('QUESTION.db')
        cursor_obj = connection_obj.cursor()
        cursor_obj.execute("""
        SELECT MAX(id) FROM question;
        """)
        range=cursor_obj.fetchall()
        random_num=random.randint(1,range[0][0])
        cursor_obj.execute(f"""
        SELECT * FROM question
        WHERE id={random_num}
        """)
        a=cursor_obj.fetchall()
        question=a[0][1],a[0][2],a[0][3],a[0][4],a[0][5],a[0][6]
        return question

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