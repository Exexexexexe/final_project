import pygame
from constants import*

objects = []
input_buttons = []
user_data = []


class Button:
    def __init__(self, screen, x, y, width, height, buttonText, font, onclickFunction=None, onePress=False):
        """Конструктор класса Button

        Args:
        (x, y) - координаты кнопки.  
        width - ширина кнопки.
        height - высота нопки.
        buttonText - текст кнопки.
        onclickFunction - функция вызываемая при нажатии кнопки.
        onePress - будет ли кнопка нажата один раз.
        
        """

        global objects

        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.fillColors = {
            'normal': GRAY,
            'hover': BLUE,
            'pressed': RED
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        objects.append(self)

    def process(self):
        """Обрабатывает поведение мыши на экране.  """
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)

class InputButton:
    def __init__(self, screen, x, y, width, height, font, name=''):
        """Конструктор класса InputButton
        Args:
        screen - холст для рисования.
        (x, y) - координаты кнопки.  
        width - ширина кнопки.
        height - высота нопки.
        font - шрифт.  
        name - текст кнопки.
        """

        global input_buttons
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.name = name
        self.text = ""
        self.surface = font.render(self.name + self.text, True, BLACK)
        self.active = False
        self.colors = {
            'active': RED,
            'inactive': GRAY
            }
        self.font = font
        input_buttons.append(self)

    def handle_event(self, event):
        """Обрабатывает ввод данных через кнопку.
        Args:
        **event** - событие, объект pygame.Event.  
        """
        
        global user_data
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    user_data.append({self.name: self.text})
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text =  self.text[:-1]
                else:
                    self.text += event.unicode
                self.surface = self.font.render(self.name + self.text, True, BLACK)

    def update(self):
        """ Изменяет размер кнопки в соответствии с длиной текста. """
        
        self.rect.w = self.surface.get_width()+10

    def draw(self):
        """Рисует кнопку на экране.  """
        self.screen.blit(self.surface, (self.rect.x+5, self.rect.y+5))
        if self.active:
            pygame.draw.rect(self.screen, self.colors['active'], self.rect, 2)
        else:
            pygame.draw.rect(self.screen, self.colors['inactive'], self.rect, 2)
            
        
    


    
    
            

        
        
        


