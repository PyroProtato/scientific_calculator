import pygame, sys, random, asyncio, math
from pygame.locals import *
from resources.classes import Button
from color_screen import Color_screen
pygame.init()
 
# Colours
COLOR_BACKGROUND = (43, 43, 43)
NUMBER_COLOR = (217, 217, 217)
MODIFYER_COLOR = (217, 217, 217)
OPERATION_COLOR = (66, 66, 66)
SPECIAL_COLOR = (105, 105, 105)
TOP_COLOR = (159, 159, 159)
ENTER_COLOR = (3, 26, 64)
DELETE_COLOR = (51, 51, 51)
CLRALL_COLOR = (51, 51, 51)

color_list = [NUMBER_COLOR, MODIFYER_COLOR, OPERATION_COLOR, SPECIAL_COLOR, TOP_COLOR, ENTER_COLOR, DELETE_COLOR, CLRALL_COLOR]
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
OG_WINDOW_WIDTH = 700
OG_WINDOW_HEIGHT = 900

WINDOW_WIDTH = OG_WINDOW_WIDTH
WINDOW_HEIGHT = OG_WINDOW_WIDTH


#Sounds
click_sound = pygame.mixer.Sound("resources/sounds/mixkit-classic-click-1117.wav")
 








class calcBtn:
  def __init__(self, symbol:str, type:str, position:tuple):

    self.symbol = symbol
    self.type = type
    self.position = position
    self.font_size = 50
    self.font = pygame.font.Font('resources/fonts/SourceCodePro-Semibold.ttf', self.font_size)

    if self.type == "number":
      self.color = NUMBER_COLOR
      self.hover_color = (250, 250, 250)
      self.pressed_color = (138, 138, 138)
      self.text_color = (0, 0, 0)
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*7
    elif self.type == "modifyer":
      self.color = MODIFYER_COLOR
      self.hover_color = (250, 250, 250)
      self.pressed_color = (138, 138, 138)
      self.text_color = (0, 0, 0)
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*7
    elif self.type == "operation":
      self.color = OPERATION_COLOR
      self.hover_color = (97, 97, 97)
      self.pressed_color = (46, 46, 46)
      self.text_color = (255, 255, 255)
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*7
    elif self.type == "special":
      self.color = SPECIAL_COLOR
      self.hover_color = (160, 160, 160)
      self.pressed_color = (70, 70, 70)
      self.text_color = (255, 255, 255)
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*7
    elif self.type == "top":
      self.color = TOP_COLOR
      self.hover_color = (200, 200, 200)
      self.pressed_color = (125, 125, 125)
      self.text_color = (255, 255, 255)
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*4
    elif self.type == "enter":
      self.color = ENTER_COLOR
      self.hover_color = (5, 46, 115)
      self.pressed_color = (3, 17, 41)
      self.text_color = (255, 255, 255)
      self.width = WINDOW_WIDTH/100*71
      self.height = WINDOW_HEIGHT/100*7
    elif self.type == "delete":
      self.color = ENTER_COLOR
      self.hover_color = (89, 89, 89)
      self.pressed_color = (18, 18, 18)
      self.text_color = (255, 255, 255)
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*7
    elif self.type == "clear all":
      self.color = CLRALL_COLOR
      self.hover_color = (89, 89, 89)
      self.pressed_color = (18, 18, 18)
      self.text_color = (255, 255, 255)
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*4

    self.x = WINDOW_WIDTH/100*self.position[0]
    self.y = WINDOW_HEIGHT/100*self.position[1]

    self.button = Button((self.x, self.y), (self.width, self.height), self.color)
    
    if self.type == 'special':
      self.button.ellipse()


  def draw(self, mousePos, mouseIsDown):

    if self.type == "number":
      self.color = color_list[0]
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*7
    elif self.type == "modifyer":
      self.color = color_list[1]
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*7
    elif self.type == "operation":
      self.color = color_list[2]
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*7
    elif self.type == 'special':
      self.color = color_list[3]
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*7
    elif self.type == "top":
      self.color = color_list[4]
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*4
    elif self.type == "enter":
      self.color = color_list[5]
      self.width = WINDOW_WIDTH/100*71
      self.height = WINDOW_HEIGHT/100*7
    elif self.type == "delete":
      self.color = color_list[6]
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*7
    elif self.type == "clear all":
      self.color = color_list[7]
      self.width = WINDOW_WIDTH/100*14
      self.height = WINDOW_HEIGHT/100*4

    self.x = WINDOW_WIDTH/100*self.position[0]
    self.y = WINDOW_HEIGHT/100*self.position[1]

    self.button = Button((self.x, self.y), (self.width, self.height), self.color)

    if self.type == 'special':
      self.button.ellipse()

    self.button.update(self.hover_color, self.pressed_color, mousePos, mouseIsDown)

    self.button.add_text(self.font, self.symbol, self.text_color)

    while self.button.text_rect.width >= WINDOW_WIDTH/100*14 or self.button.text_rect.height >= WINDOW_HEIGHT/100*4:
      self.font_size -= 1
      self.font = pygame.font.Font('resources/fonts/SourceCodePro-Semibold.ttf', self.font_size)
      self.button.add_text(self.font, self.symbol, self.text_color)
    while self.button.text_rect.height <= WINDOW_HEIGHT/100*3:
      self.font_size += 1
      self.font = pygame.font.Font('resources/fonts/SourceCodePro-Semibold.ttf', self.font_size)
      self.button.add_text(self.font, self.symbol, self.text_color)

    self.button.add_border(2, self.text_color)

    self.button.draw(WINDOW)
  
  def isPressed(self, mousePos, mouseUp):
    return self.button.check_press(mousePos, mouseUp)





def insertChar(character:str, text_entries:list, cursor_pos):
  temp = list(text_entries[len(text_entries)-1]['text'])
  temp.insert(cursor_pos, character)
  temp = "".join(temp)
  text_entries[len(text_entries)-1]['text'] = temp

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def calculate(text_list, mod=None, power_base=None):
  text_list = [x for x in text_list if x != ""]
  try:
      index = 0
      while index < len(text_list):

        if text_list[index] == '/': #Division
          calculation = float(text_list[index-1]) / float(text_list[index+1])
          text_list[index+1] = calculation
          del text_list[index]
          del text_list[index-1]
          index = 0
        
        if text_list[index] == '*': #Multiplication
          calculation = float(text_list[index-1]) * float(text_list[index+1])
          text_list[index+1] = calculation
          del text_list[index]
          del text_list[index-1]
          index = 0
        try:
          if is_float(text_list[index]) and is_float(text_list[index+1]):
            calculation = float(text_list[index]) * float(text_list[index+1])
            text_list[index+1] = calculation
            del text_list[index]
            index = 0
        except:
          pass
        
        index += 1

        if len(text_list) == 2 and is_float(text_list[0]) and is_float(text_list[1]):
          index = 0
      

      index = 0
      while index < len(text_list):
        if text_list[index] == '-': #Subtraction
          calculation = float(text_list[index-1]) - float(text_list[index+1])
          text_list[index+1] = calculation
          del text_list[index]
          del text_list[index-1]
          index = 0
        
        if text_list[index] == '+': #Addition
          calculation = float(text_list[index-1]) + float(text_list[index+1])
          text_list[index+1] = calculation
          del text_list[index]
          del text_list[index-1]
          index = 0
        
        index += 1


      if mod == '√':
        text_list[0] = float(text_list[0])
        text_list[0] = math.sqrt(text_list[0])
      if mod == '^':
        power_base = float(power_base)
        text_list[0] = float(text_list[0])
        text_list[0] = pow(power_base, text_list[0])
      
      return text_list
    

  except:
    return ""
















class Screen1:
  #Initializes all of the variables that are needed for the screen to work
  def __init__(self):

    #STATE
    self.running = False
    
    #COLORS
    self.color_bg = COLOR_BACKGROUND
    self.display_bg_color = (100, 100, 100)

    #FONTS
    self.display_font = pygame.font.Font('resources/fonts/SourceCodePro-Semibold.ttf', 20)


    #USERINPUTS
    self.mouseIsDown = False
    self.mouseUp = False
    self.mouseDown = False
    self.mousePos = None


    #OBJECTS


    #buttons
    self.btn0 = calcBtn("0", "number", (24, 79))
    self.btn1 = calcBtn("1", "number", (24, 70))
    self.btn2 = calcBtn("2", "number", (43, 70))
    self.btn3 = calcBtn("3", "number", (62, 70))
    self.btn4 = calcBtn("4", "number", (24, 61))
    self.btn5 = calcBtn("5", "number", (43, 61))
    self.btn6 = calcBtn("6", "number", (62, 61))
    self.btn7 = calcBtn("7", "number", (24, 52))
    self.btn8 = calcBtn("8", "number", (43, 52))
    self.btn9 = calcBtn("9", "number", (62, 52))
    self.btn_decimal = calcBtn(".", "modifyer", (43, 79))
    self.btn_negative = calcBtn("(-)", "modifyer", (62, 79))
    self.btn_plus = calcBtn("+", "operation", (81, 79))
    self.btn_minus = calcBtn("-", "operation", (81, 70))
    self.btn_multiply = calcBtn("×", "operation", (81, 61))
    self.btn_divide = calcBtn("÷", "operation", (81, 52))
    self.btn_sqrt = calcBtn("√", "special", (5, 61))
    self.btn_power = calcBtn("^", "special", (5, 70))
    self.btn_pi = calcBtn("π", "special", (5, 79))
    self.btn_lpar = calcBtn("(", "top", (24, 46))
    self.btn_rpar = calcBtn(")", "top", (43, 46))
    self.btn_larrow = calcBtn("<-", "top", (62, 46))
    self.btn_rarrow = calcBtn("->", "top", (81, 46))
    self.btn_enter = calcBtn("enter", "enter", (24, 88))
    self.btn_delete = calcBtn("del", "delete", (5, 88))
    self.btn_clear = calcBtn("clr", "delete", (5, 52))
    self.btn_clearall = calcBtn("clr all", "clear all", (5, 46))


    #calc text
    self.text_entries = []
    self.text_entries.append({'text':'', 'answer':''})

    #Cursor
    self.cursor_pos = 0
    self.cursor_blink = 0

    #Misc
    self.shifted = False
    


  


  def run(self, events):
    key = None

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
        if event.key == K_LSHIFT or event.key == K_RSHIFT:
          self.shifted = True
        key = event.key
        if event.key == K_c:
          return "cs"
      if event.type == KEYUP:
        if event.key == K_LSHIFT or event.key == K_RSHIFT:
          self.shifted = False


    

    """PROCESSING"""
    self.display_bg = pygame.Rect(WINDOW_WIDTH/100*5, WINDOW_HEIGHT/100*3, WINDOW_WIDTH/100*90, WINDOW_HEIGHT/100*40)


    #Updates the text if a button is pressed
    if self.btn_enter.isPressed(self.mousePos, self.mouseUp) or key == K_RETURN: #Enter
      pygame.mixer.Sound.play(click_sound)
      self.text_entries.append({'text':'', 'answer':''})
    if self.btn0.isPressed(self.mousePos, self.mouseUp) or (key == K_0 and self.shifted == False): #0
      pygame.mixer.Sound.play(click_sound)
      insertChar('0', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn1.isPressed(self.mousePos, self.mouseUp) or (key == K_1 and self.shifted == False): #1
      pygame.mixer.Sound.play(click_sound)
      insertChar('1', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn2.isPressed(self.mousePos, self.mouseUp) or (key == K_2 and self.shifted == False): #2
      pygame.mixer.Sound.play(click_sound)
      insertChar('2', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn3.isPressed(self.mousePos, self.mouseUp) or (key == K_3 and self.shifted == False): #3
      pygame.mixer.Sound.play(click_sound)
      insertChar('3', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn4.isPressed(self.mousePos, self.mouseUp) or (key == K_4 and self.shifted == False): #4
      pygame.mixer.Sound.play(click_sound)
      insertChar('4', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn5.isPressed(self.mousePos, self.mouseUp) or (key == K_5 and self.shifted == False): #5
      pygame.mixer.Sound.play(click_sound)
      insertChar('5', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn6.isPressed(self.mousePos, self.mouseUp) or (key == K_6 and self.shifted == False): #6
      pygame.mixer.Sound.play(click_sound)
      insertChar('6', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn7.isPressed(self.mousePos, self.mouseUp) or (key == K_7 and self.shifted == False): #7
      pygame.mixer.Sound.play(click_sound)
      insertChar('7', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn8.isPressed(self.mousePos, self.mouseUp) or (key == K_8 and self.shifted == False): #8
      pygame.mixer.Sound.play(click_sound)
      insertChar('8', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn9.isPressed(self.mousePos, self.mouseUp) or (key == K_9 and self.shifted == False): #9
      pygame.mixer.Sound.play(click_sound)
      insertChar('9', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn_decimal.isPressed(self.mousePos, self.mouseUp) or (key == K_PERIOD and self.shifted == False): #.
      pygame.mixer.Sound.play(click_sound)
      insertChar('.', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn_negative.isPressed(self.mousePos, self.mouseUp) or (key == K_MINUS and self.shifted): #(-) #IDK what to do for actual keyboard key
      pygame.mixer.Sound.play(click_sound)
      insertChar('-', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn_plus.isPressed(self.mousePos, self.mouseUp) or (key == K_EQUALS and self.shifted): #+
      pygame.mixer.Sound.play(click_sound)
      insertChar(' + ', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 3
    if self.btn_minus.isPressed(self.mousePos, self.mouseUp) or (key == K_MINUS and self.shifted == False): #-
      pygame.mixer.Sound.play(click_sound)
      insertChar(' - ', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 3
    if self.btn_multiply.isPressed(self.mousePos, self.mouseUp) or (key == K_8 and self.shifted): #*
      pygame.mixer.Sound.play(click_sound)
      insertChar(' * ', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 3
    if self.btn_divide.isPressed(self.mousePos, self.mouseUp) or (key == K_SLASH and self.shifted == False): #/
      pygame.mixer.Sound.play(click_sound)
      insertChar(' / ', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 3
    if self.btn_delete.isPressed(self.mousePos, self.mouseUp) or key == K_BACKSPACE or len(self.text_entries[0]['text']) > 38: #del
      pygame.mixer.Sound.play(click_sound)
      self.cursor_blink = 0
      if self.cursor_pos != 0:
        temp = list(self.text_entries[len(self.text_entries)-1]['text'])
        if temp[self.cursor_pos-1] != " " and temp[self.cursor_pos-1] != "(":
          del temp[self.cursor_pos-1]
          self.cursor_pos -= 1
        elif temp[self.cursor_pos-1] == " ":
          del temp[self.cursor_pos-1]
          del temp[self.cursor_pos-2]
          del temp[self.cursor_pos-3]
          self.cursor_pos -= 3
        elif temp[self.cursor_pos-2] == "^" or temp[self.cursor_pos-2] == "√":
          del temp[self.cursor_pos-1]
          del temp[self.cursor_pos-2]
          self.cursor_pos -= 2
        elif temp[self.cursor_pos-1] == "(":
          del temp[self.cursor_pos-1]
          self.cursor_pos -= 1
        self.text_entries[len(self.text_entries)-1]['text'] = "".join(temp)
    if self.btn_clear.isPressed(self.mousePos, self.mouseUp): #clear  #ALSO DONT KNOW FOR KEYBOARD
      pygame.mixer.Sound.play(click_sound)
      self.text_entries[len(self.text_entries)-1]['text'] = ""
      self.cursor_blink = 0
    if self.btn_clearall.isPressed(self.mousePos, self.mouseUp): #clear all    #ALSO DONT KNOW FOR KEYBOARD
      pygame.mixer.Sound.play(click_sound)
      self.text_entries = [{'text':"", 'answer':""}]
      self.cursor_blink = 0
    if self.btn_lpar.isPressed(self.mousePos, self.mouseUp) or (key == K_9 and self.shifted): #(
      pygame.mixer.Sound.play(click_sound)
      insertChar('(', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn_rpar.isPressed(self.mousePos, self.mouseUp) or (key == K_0 and self.shifted): #)
      pygame.mixer.Sound.play(click_sound)
      insertChar(')', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn_pi.isPressed(self.mousePos, self.mouseUp) or (key == K_p and self.shifted == False): #π
      pygame.mixer.Sound.play(click_sound)
      insertChar('π', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 1
    if self.btn_sqrt.isPressed(self.mousePos, self.mouseUp) or (key == K_s and self.shifted == False): #√
      pygame.mixer.Sound.play(click_sound)
      insertChar('√(', self.text_entries, self.cursor_pos) 
      self.cursor_blink = 0
      self.cursor_pos += 2
    if self.btn_power.isPressed(self.mousePos, self.mouseUp) or (key == K_6 and self.shifted): #^
      pygame.mixer.Sound.play(click_sound)
      insertChar('^(', self.text_entries, self.cursor_pos)
      self.cursor_blink = 0
      self.cursor_pos += 2
    if self.btn_larrow.isPressed(self.mousePos, self.mouseUp) or key == K_LEFT: #<-
      pygame.mixer.Sound.play(click_sound)
      self.cursor_blink = 0
      if self.cursor_pos != 0:
        temp = list(self.text_entries[len(self.text_entries)-1]['text'])
        if temp[self.cursor_pos-1] != " " and temp[self.cursor_pos-1] != "(":
          self.cursor_pos -= 1
        elif temp[self.cursor_pos-1] == " ":
          self.cursor_pos -= 3
        elif temp[self.cursor_pos-2] == "^" or temp[self.cursor_pos-2] == "√":
          self.cursor_pos -= 2
    if self.btn_rarrow.isPressed(self.mousePos, self.mouseUp) or key == K_RIGHT: #->
      pygame.mixer.Sound.play(click_sound)
      self.cursor_blink = 0
      if self.cursor_pos != len(self.text_entries[len(self.text_entries)-1]['text']):
        temp = list(self.text_entries[len(self.text_entries)-1]['text'])
        try:
          if temp[self.cursor_pos] != " " and temp[self.cursor_pos] != "^" and temp[self.cursor_pos] != "√":
            self.cursor_pos += 1
          elif temp[self.cursor_pos] == " ":
            self.cursor_pos += 3
          elif temp[self.cursor_pos] == "^" or temp[self.cursor_pos] == "√":
            self.cursor_pos += 2
        except:
          self.cursor_pos += 1



    
    #Handles Cursor Position
    if self.cursor_pos < 0:
      self.cursor_pos = 0
    if self.cursor_pos > 38:
      self.cursor_pos = 38
    if self.cursor_pos > len(self.text_entries[len(self.text_entries)-1]['text']):
      self.cursor_pos -= 1

    
    #Calculations

    #converts the text into processable format
    text = self.text_entries[len(self.text_entries)-1]['text']
    text_list = []
    number = ""
    for char in text:
      if char == ' ':
        text_list.append(number)
        number = ""
      elif char == 'π':
        text_list.append(number)
        text_list.append(math.pi)
        number = ""
      elif char == '^' or char == "√":
        text_list.append(number)
        number = ""
        number += char
      elif char == '(':
        text_list.append(number)
        text_list.append(char)
        number = ""
      elif char == ')':
        text_list.append(number)
        number = ""
        number += char
        text_list.append(number)
        number = ""
      else:
        number += char
    text_list.append(number)
    text_list = [x for x in text_list if x != ""]



    #Runs the Calculations
    num_rpars = len([x for x in text_list if x == '('])
    num_lpars = len([x for x in text_list if x == ')'])
    if num_lpars != num_rpars:
      text_list = ""
    elif num_lpars == num_rpars and num_rpars != 0:
      num_pars = num_rpars
      pairs = []
      temp_text_list = text_list[:]
      while num_pars != 0:
        lpar = None
        rpar = None
        for index, element in enumerate(temp_text_list):
          if element == '(':
            rpar = index
          if element == ')':
            lpar = index
          if rpar != None and lpar != None:
            pairs.append((rpar, lpar))
            temp_text_list[lpar] = ""
            temp_text_list[rpar] = ""
            num_pars -= 1
            break
    

      try:
        for pair in pairs:
          mod = None
          if pair[0] != 0:
            if text_list[pair[0]-1] == '^':
              mod = '^'
            elif text_list[pair[0]-1] == '√':
              mod = '√'
          if mod == '^':
            answer = calculate(text_list[pair[0]+1:pair[1]], mod, text_list[pair[0]-2])
          else:
            answer = calculate(text_list[pair[0]+1:pair[1]], mod)
          text_list[pair[1]] = answer[0]
          for index in range(pair[0], pair[1]):
            text_list[index] = ""

          if mod == '√':
            text_list[pair[0]-1] = ""
          if mod == '^':
            text_list[pair[0]-1] = ""
            text_list[pair[0]-2] = ""
      
        
      
        text_list = [x for x in text_list if x != ""]
      
      except:
        text_list = ""
    
    
    if text_list != "":
      text_list = calculate(text_list)
    


    #Enters the Answer
    try:
      if text_list == "" or text_list == []:
        self.text_entries[len(self.text_entries)-1]['answer'] = ""
      elif len(text_list) == 1:
        if text_list[0].is_integer():
          self.text_entries[len(self.text_entries)-1]['answer'] = str(int(text_list[0]))
        else:
          self.text_entries[len(self.text_entries)-1]['answer'] = str(round(text_list[0], 20))
    except:
      self.text_entries[len(self.text_entries)-1]['answer'] = ""

    ans_ex = False
    num_ex = 0
    while len(self.text_entries[len(self.text_entries)-1]['answer']) > 8:
      ans_ex = True
      num_ex += 1
      self.text_entries[len(self.text_entries)-1]['answer'] = self.text_entries[len(self.text_entries)-1]['answer'][0:len(self.text_entries[len(self.text_entries)-1]['answer'])-1]
    if ans_ex:
      if '.' not in self.text_entries[len(self.text_entries)-1]['answer']:
        e_answer = [x for x in self.text_entries[len(self.text_entries)-1]['answer'][0:3]]
        e_answer.insert(1, '.')
        e_answer = "".join(e_answer)
        e_answer += f'E+{num_ex+7}'
        self.text_entries[len(self.text_entries)-1]['answer'] = e_answer
      else:
        self.text_entries[len(self.text_entries)-1]['answer'] += "…"

    

    #Deletes any xtra entries
    if len(self.text_entries) > 8:
      del self.text_entries[0]
      




    """DRAW TO SCREEN"""
    WINDOW.fill(self.color_bg)
    pygame.draw.rect(WINDOW, self.display_bg_color, self.display_bg)
    self.btn0.draw(self.mousePos, self.mouseIsDown)
    self.btn1.draw(self.mousePos, self.mouseIsDown)
    self.btn2.draw(self.mousePos, self.mouseIsDown)
    self.btn3.draw(self.mousePos, self.mouseIsDown)
    self.btn4.draw(self.mousePos, self.mouseIsDown)
    self.btn5.draw(self.mousePos, self.mouseIsDown)
    self.btn6.draw(self.mousePos, self.mouseIsDown)
    self.btn7.draw(self.mousePos, self.mouseIsDown)
    self.btn8.draw(self.mousePos, self.mouseIsDown)
    self.btn9.draw(self.mousePos, self.mouseIsDown)
    self.btn_decimal.draw(self.mousePos, self.mouseIsDown)
    self.btn_negative.draw(self.mousePos, self.mouseIsDown)
    self.btn_plus.draw(self.mousePos, self.mouseIsDown)
    self.btn_minus.draw(self.mousePos, self.mouseIsDown)
    self.btn_multiply.draw(self.mousePos, self.mouseIsDown)
    self.btn_divide.draw(self.mousePos, self.mouseIsDown)
    self.btn_sqrt.draw(self.mousePos, self.mouseIsDown)
    self.btn_power.draw(self.mousePos, self.mouseIsDown)
    self.btn_pi.draw(self.mousePos, self.mouseIsDown)
    self.btn_lpar.draw(self.mousePos, self.mouseIsDown)
    self.btn_rpar.draw(self.mousePos, self.mouseIsDown)
    self.btn_larrow.draw(self.mousePos, self.mouseIsDown)
    self.btn_rarrow.draw(self.mousePos, self.mouseIsDown)
    self.btn_enter.draw(self.mousePos, self.mouseIsDown)
    self.btn_delete.draw(self.mousePos, self.mouseIsDown)
    self.btn_clear.draw(self.mousePos, self.mouseIsDown)
    self.btn_clearall.draw(self.mousePos, self.mouseIsDown)

    #Display Text
    display_placement = 38
    self.display_font = pygame.font.Font('resources/fonts/SourceCodePro-Semibold.ttf', WINDOW_WIDTH//35)
    for index, entry in enumerate(self.text_entries[::-1]):
      #Background Rect
      bg_rect = pygame.Rect(WINDOW_WIDTH/100*5, WINDOW_HEIGHT/100*display_placement, WINDOW_WIDTH/100*90, WINDOW_HEIGHT/100*5)
      if index == 0:
        pygame.draw.rect(WINDOW, (180, 180, 180), bg_rect)
      else:
        pygame.draw.rect(WINDOW, (135, 135, 135), bg_rect)
      pygame.draw.line(WINDOW, (0, 0, 0), (WINDOW_WIDTH/100*5, WINDOW_HEIGHT/100*display_placement), (WINDOW_WIDTH/100*95, WINDOW_HEIGHT/100*display_placement), 1)

      #Input Text
      entry_text = self.display_font.render(entry['text'], True, (0, 0, 0), None)
      if index == 0:
        self.entry_text_rect = entry_text.get_rect()
      entry_text_rect = entry_text.get_rect()
      entry_text_rect.midleft = (WINDOW_WIDTH/100*7, bg_rect.midleft[1])
      WINDOW.blit(entry_text, entry_text_rect)

      #Answer Text
      answer_text = self.display_font.render(f'= {entry["answer"]}', True, (0, 0, 0), None)
      answer_text_rect = answer_text.get_rect()
      answer_text_rect.midleft = (WINDOW_WIDTH/100*75, bg_rect.midleft[1])
      WINDOW.blit(answer_text, answer_text_rect)

      #Misc.
      display_placement -= 5
  
    #Display Cursor
    self.cursor_blink += 1
    cursor = pygame.Rect(0, 0, WINDOW_WIDTH/100*0.25, WINDOW_HEIGHT/100*4)
    try:
      cursor.center = (self.cursor_pos*(self.entry_text_rect.width/len(self.text_entries[len(self.text_entries)-1]['text']))+WINDOW_WIDTH/100*6.9, WINDOW_HEIGHT/100*40.5)
    except ZeroDivisionError:
      cursor.center = (WINDOW_WIDTH/100*6.9, WINDOW_HEIGHT/100*40.5)
    #cursor.center = (self.cursor_pos*WINDOW_WIDTH/100*1.72+WINDOW_WIDTH/100*6.9, WINDOW_HEIGHT/100*40.5)
    if self.cursor_blink <= 35:
      pygame.draw.rect(WINDOW, (0, 0, 0), cursor)
    elif self.cursor_blink == 70:
      self.cursor_blink = 0
    
    
    #Misc.
    pygame.draw.rect(WINDOW, (0, 0, 0), self.display_bg, 1)
      




WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)








 
# The main function that controls the game
async def main () :
  
  #Makes the height and Width global variables
  global WINDOW_WIDTH
  global WINDOW_HEIGHT
  

  """INITIATE THE SCREENS"""
  initialize = True

  s1 = Screen1()
  s1.running = True

  cs = Color_screen()
  cs.running = False

  global color_list


  """MAIN GAME LOOP"""
  while True :

    #Updates Height and Width
    WINDOW_WIDTH = WINDOW.get_width()
    WINDOW_HEIGHT = WINDOW.get_height()

    """USER INPUT"""
    events = []
    for event in pygame.event.get() :
      events.append(event)
    

    """ACTIVATE SCREENS"""
    if s1.running:
      if initialize:
        pygame.display.set_caption('Calculator (Press c to change colors!)')
      status = s1.run(events)
      if status == "cs":
        cs.running = True
        initialize = True
        s1.running = False
    elif cs.running:
      if initialize:
        pygame.display.set_caption('Color Switcher (Press c to return)')
      status, color_list = cs.run(events, color_list)
      if status == "s1":
        cs.running = False
        initialize = True
        s1.running = True




 
    """UPDATE and FPS"""
    pygame.display.update()
    fpsClock.tick(FPS)

    await asyncio.sleep(0)

asyncio.run(main())