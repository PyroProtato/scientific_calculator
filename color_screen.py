import pygame, sys, random, asyncio
from pygame.locals import *
from resources.classes import Button
pygame.init()
 
# Colours
COLOR_BACKGROUND = (43, 43, 43)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 375

NUMBER_COLOR = (217, 217, 217)
MODIFYER_COLOR = (217, 217, 217)
OPERATION_COLOR = (66, 66, 66)
SPECIAL_COLOR = (105, 105, 105)
TOP_COLOR = (159, 159, 159)
ENTER_COLOR = (3, 26, 64)
DELETE_COLOR = (51, 51, 51)
CLRALL_COLOR = (51, 51, 51)

colors = [NUMBER_COLOR, MODIFYER_COLOR, OPERATION_COLOR, SPECIAL_COLOR, TOP_COLOR, ENTER_COLOR, DELETE_COLOR, CLRALL_COLOR]

#COLORS
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
BROWN = (139,69,19)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
D1 = (217, 217, 217)
D2 = (66, 66, 66)
D3 = (105, 105, 105)
D4 = (159, 159, 159)
D5 = (3, 26, 64)
D6 = (51, 51, 51)

#BUTTON FONT
FONT_SIZE = 20
FONT = pygame.font.Font('resources/fonts/SourceCodePro-Semibold.ttf', FONT_SIZE)
BORDER_WIDTH = 5
BUTTON_COLOR = (180, 180, 180)
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Color Changer')


class Color_screen:
  #Initializes all of the variables that are needed for the screen to work
  def __init__(self):

    #STATE
    self.running = False
    
    #COLORS
    self.color_bg = COLOR_BACKGROUND

    #Background Rect
    self.background_rect = pygame.Rect(25, 100, 400, 250)
    self.choosing_rect = pygame.Rect(0, 0, 25, 25)

    #ELEMENT BUTTONS
    self.NUMBER_BUTTON = Button((25,25), (50,50), BUTTON_COLOR)
    self.NUMBER_BUTTON.add_text(FONT, "1", (0, 0, 0), -3)
    self.MODIFYER_BUTTON = Button((75,25), (50,50), BUTTON_COLOR)
    self.MODIFYER_BUTTON.add_text(FONT, "(-)", (0, 0, 0), -3)
    self.OPERATION_BUTTON = Button((125,25), (50,50), BUTTON_COLOR)
    self.OPERATION_BUTTON.add_text(FONT, "+", (0, 0, 0), -3)
    self.SPECIAL_BUTTON = Button((175,25), (50,50), BUTTON_COLOR)
    self.SPECIAL_BUTTON.add_text(FONT, "π", (0, 0, 0), -3)
    self.TOP_BUTTON = Button((225,25), (50,50), BUTTON_COLOR)
    self.TOP_BUTTON.add_text(FONT, "->", (0, 0, 0), -3)
    self.ENTER_BUTTON = Button((275,25), (50,50), BUTTON_COLOR)
    self.ENTER_BUTTON.add_text(FONT, "ent", (0, 0, 0), -3)
    self.DELETE_BUTTON = Button((325,25), (50,50), BUTTON_COLOR)
    self.DELETE_BUTTON.add_text(FONT, "del", (0, 0, 0), -3)
    self.CLRALL_BUTTON = Button((375,25), (50,50), BUTTON_COLOR)
    self.CLRALL_BUTTON.add_text(FONT, "clr", (0, 0, 0), -3)

    #COLOR BUTTONS
    self.RED = Button((50, 125), (50, 50), RED)
    self.YELLOW = Button((125, 125), (50, 50), YELLOW)
    self.BLUE = Button((200, 125), (50, 50), BLUE)
    self.ORANGE = Button((50, 200), (50, 50), ORANGE)
    self.GREEN = Button((125, 200), (50, 50), GREEN)
    self.PURPLE = Button((200, 200), (50, 50), PURPLE)
    self.BROWN = Button((50, 275), (50, 50), BROWN)
    self.BLACK = Button((125, 275), (50, 50), BLACK)
    self.WHITE = Button((200, 275), (50, 50), WHITE)
    self.D1 = Button((275, 125), (50, 50), D1)
    self.D2 = Button((350, 125), (50, 50), D2)
    self.D3 = Button((275, 200), (50, 50), D3)
    self.D4 = Button((350, 200), (50, 50), D4)
    self.D5 = Button((275, 275), (50, 50), D5)
    self.D6 = Button((350, 275), (50, 50), D6)


    #USERINPUTS
    self.mouseIsDown = False
    self.mouseUp = False
    self.mouseDown = False
    self.mousePos = None

    #Variables
    self.choice = 0
  


  def run(self, events, color_list):

    self.color_list = color_list

    
    
    """GETS USER INPUTS"""
    self.mouseDown = False
    self.mouseUp = False
    self.mousePos = pygame.mouse.get_pos()
    for event in events:
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        self.mouseIsDown = True
        self.mouseDown = True
      if event.type == MOUSEBUTTONUP:
        self.mouseIsDown = False
        self.mouseUp = True
      if event.type == KEYDOWN:
        if event.key == K_c:
          return "s1", self.color_list
    

    """PROCESSING"""

    
    #NUMBER BUTTONS
    self.NUMBER_BUTTON.add_border(BORDER_WIDTH, self.color_list[0])
    self.MODIFYER_BUTTON.add_border(BORDER_WIDTH, self.color_list[1])
    self.OPERATION_BUTTON.add_border(BORDER_WIDTH, self.color_list[2])
    self.SPECIAL_BUTTON.add_border(BORDER_WIDTH, self.color_list[3])
    self.TOP_BUTTON.add_border(BORDER_WIDTH, self.color_list[4])
    self.ENTER_BUTTON.add_border(BORDER_WIDTH, self.color_list[5])
    self.DELETE_BUTTON.add_border(BORDER_WIDTH, self.color_list[6])
    self.CLRALL_BUTTON.add_border(BORDER_WIDTH, self.color_list[7])

    self.NUMBER_BUTTON.update((250, 250, 250), (138, 138, 138), self.mousePos, self.mouseIsDown)
    self.MODIFYER_BUTTON.update((250, 250, 250), (138, 138, 138), self.mousePos, self.mouseIsDown)
    self.OPERATION_BUTTON.update((250, 250, 250), (138, 138, 138), self.mousePos, self.mouseIsDown)
    self.SPECIAL_BUTTON.update((250, 250, 250), (138, 138, 138), self.mousePos, self.mouseIsDown)
    self.TOP_BUTTON.update((250, 250, 250), (138, 138, 138), self.mousePos, self.mouseIsDown)
    self.ENTER_BUTTON.update((250, 250, 250), (138, 138, 138), self.mousePos, self.mouseIsDown)
    self.DELETE_BUTTON.update((250, 250, 250), (138, 138, 138), self.mousePos, self.mouseIsDown)
    self.CLRALL_BUTTON.update((250, 250, 250), (138, 138, 138), self.mousePos, self.mouseIsDown)

    if self.NUMBER_BUTTON.check_press(self.mousePos, self.mouseUp):
      self.choice = 0
    if self.MODIFYER_BUTTON.check_press(self.mousePos, self.mouseUp):
      self.choice = 1
    if self.OPERATION_BUTTON.check_press(self.mousePos, self.mouseUp):
      self.choice = 2
    if self.SPECIAL_BUTTON.check_press(self.mousePos, self.mouseUp):
      self.choice = 3
    if self.TOP_BUTTON.check_press(self.mousePos, self.mouseUp):
      self.choice = 4
    if self.ENTER_BUTTON.check_press(self.mousePos, self.mouseUp):
      self.choice = 5
    if self.DELETE_BUTTON.check_press(self.mousePos, self.mouseUp):
      self.choice = 6
    if self.CLRALL_BUTTON.check_press(self.mousePos, self.mouseUp):
      self.choice = 7

    #COLOR BUTTONS
    self.RED.update(RED, RED, self.mousePos, self.mouseIsDown)
    self.YELLOW.update(YELLOW, YELLOW, self.mousePos, self.mouseIsDown)
    self.BLUE.update(BLUE, BLUE, self.mousePos, self.mouseIsDown)
    self.ORANGE.update(ORANGE, ORANGE, self.mousePos, self.mouseIsDown)
    self.GREEN.update(GREEN, GREEN, self.mousePos, self.mouseIsDown)
    self.PURPLE.update(PURPLE, PURPLE, self.mousePos, self.mouseIsDown)
    self.BROWN.update(BROWN, BROWN, self.mousePos, self.mouseIsDown)
    self.BLACK.update(BLACK, BLACK, self.mousePos, self.mouseIsDown)
    self.WHITE.update(WHITE, WHITE, self.mousePos, self.mouseIsDown)
    self.D1.update(D1, D1, self.mousePos, self.mouseIsDown)
    self.D2.update(D2, D2, self.mousePos, self.mouseIsDown)
    self.D3.update(D3, D3, self.mousePos, self.mouseIsDown)
    self.D4.update(D4, D4, self.mousePos, self.mouseIsDown)
    self.D5.update(D5, D5, self.mousePos, self.mouseIsDown)
    self.D6.update(D6, D6, self.mousePos, self.mouseIsDown)

    if self.RED.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = RED
    if self.YELLOW.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = YELLOW
    if self.BLUE.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = BLUE
    if self.ORANGE.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = ORANGE
    if self.GREEN.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = GREEN
    if self.PURPLE.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = PURPLE
    if self.BROWN.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = BROWN
    if self.BLACK.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = BLACK
    if self.WHITE.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = WHITE
    if self.D1.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = D1
    if self.D2.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = D2
    if self.D3.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = D3
    if self.D4.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = D4
    if self.D5.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = D5
    if self.D6.check_press(self.mousePos, self.mouseUp):
      self.color_list[self.choice] = D6

    #Choosing Rect
    self.choosing_rect.topleft = (37.5+self.choice*50, 75)



    """DRAW TO SCREEN"""
    WINDOW.fill(self.color_bg)

    #Background Rect
    pygame.draw.rect(WINDOW, BUTTON_COLOR, self.background_rect)
    pygame.draw.rect(WINDOW, BUTTON_COLOR, self.choosing_rect)

    #NUMBER BUTTONS
    self.NUMBER_BUTTON.draw(WINDOW)
    self.MODIFYER_BUTTON.draw(WINDOW)
    self.OPERATION_BUTTON.draw(WINDOW)
    self.SPECIAL_BUTTON.draw(WINDOW)
    self.TOP_BUTTON.draw(WINDOW)
    self.ENTER_BUTTON.draw(WINDOW)
    self.DELETE_BUTTON.draw(WINDOW)
    self.CLRALL_BUTTON.draw(WINDOW)

    #Color Buttons
    self.RED.draw(WINDOW)
    self.YELLOW.draw(WINDOW)
    self.BLUE.draw(WINDOW)
    self.ORANGE.draw(WINDOW)
    self.GREEN.draw(WINDOW)
    self.PURPLE.draw(WINDOW)
    self.BROWN.draw(WINDOW)
    self.BLACK.draw(WINDOW)
    self.WHITE.draw(WINDOW)
    self.D1.draw(WINDOW)
    self.D2.draw(WINDOW)
    self.D3.draw(WINDOW)
    self.D4.draw(WINDOW)
    self.D5.draw(WINDOW)
    self.D6.draw(WINDOW)

    return "", self.color_list










 
