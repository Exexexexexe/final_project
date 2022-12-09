import pygame
import sys
from constants import*

#font = pygame.font.SysFont('Arial', 40)

objects = []

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
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)


    
    
            

        
        
        


