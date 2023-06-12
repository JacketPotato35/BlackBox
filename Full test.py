import pygame
import sys
from pygame.locals import QUIT
import numpy as np

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 1820, 980
display = pygame.display.set_mode((screen_width, screen_height))
display.fill((126,126,126))
pygame.display.set_caption('hackbox')

class Text():

    def __init__(self):
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(("hello"), True, (155, 155, 155))

    def render(self, display, text, locx, locy, font_size, colour):
        self.font = pygame.font.SysFont("Verdana", font_size)
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
        
def execute(code):
    str=""""""
    for row in code:
        str+=row
        str+=" "
    print(str)
    try:
        exec(str)
        return ""
    except Exception as e:
        return e
        

        
text=Text()
user_text=[""]
user_row=0
while True:
    for event in pygame.event.get():
        display.fill((126,126,126))
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
                button_press=event.key
                print(pygame.key.name(button_press))
                if (button_press==pygame.K_DOWN or button_press==pygame.K_RETURN) and user_row+1==len(user_text) and user_row<18:
                    user_text+=[""]
                if button_press==pygame.K_UP and user_row>0:
                    user_row-=1
                elif button_press==pygame.K_DOWN and user_row<18:
                    user_row+=1
                elif button_press==pygame.K_RETURN and user_row<18:
                    user_row+=1
                elif button_press==pygame.K_BACKSPACE:
                    user_text[user_row]=user_text[user_row][:len(user_text[user_row])-1]
                elif button_press==pygame.K_TAB:
                    user_text[user_row]+="  "
                elif button_press==pygame.K_ESCAPE:
                    text.render(display,str(execute(user_text)),20,800,20, (255,0,0))
                if (button_press!=pygame.K_RETURN) and (button_press!=pygame.K_BACKSPACE) and (button_press!=pygame.K_TAB) and( button_press!=pygame.K_ESCAPE):
                    button_press=event.unicode
                    user_text[user_row]+=button_press
                print(user_row)
    text.renderall(display,20,(255,255,255),user_text,user_row)
    pygame.display.update()
    clock.tick(60)