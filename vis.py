"""Модуль визуализации.
Функции, создающие графические объекты частиц и перемещающие их на экране,
принимают физические координаты.
"""

import pygame
from constants import BLACK

window_width = 800
"""Ширина окна"""

window_height = 600
"""Высота окна"""

scale_factor = None
"""Масштабирование экранных координат по отношению к физическим.
Тип: float
Мера: количество пикселей на один метр."""


def calculate_scale_factor(characteristic_size=20000):
    """Вычисляет значение глобальной переменной **characteristic_size**
    по характерному размеру области движения частицы.
    """

    global scale_factor
    scale_factor = min(window_width / characteristic_size, window_height / characteristic_size)
    
def scale_x(x):
    """Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Параметры:
    **x** — x-координата модели.
    """

    return int(x*scale_factor)


def scale_y(y):
    """Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.
    Параметры:
    **y** — y-координата модели.
    """
    
    return int(-y*scale_factor) + window_height//2

def create_particle_image(screen, particle):
    """Создаёт отображаемый объект частицыы.
    Параметры:
    **screen** — холст для рисования.
    **particle** — объект частицы.
    
    """
    
    x = scale_x(particle.x)
    y = scale_y(particle.y)
    r = particle.R
    particle.image = pygame.draw.circle(screen, particle.color, (x, y), r, 0)

def update_particle_position(screen, particle):
    """Перемещает отображаемый объект на холсте.
    Параметры:
    **screen** — холст для рисования.
    **particle** — частица, которую нужно переместить.  
    """

    x = scale_x(particle.x)
    y = scale_y(particle.y)
    r = particle.R
    pygame.draw.circle(screen, particle.color, (x, y), r, 0)


def draw_trajectory(screen, particle):
    """Рисует траекторию частицы.
    Параметры:
    **screen** — холст для рисования.
    **particle** — частица, траекторию которой нужно нарисовать.  
    """

    color = particle.color
    previous_coordinates = particle.previous_coordinates
    for i in range(1, len(previous_coordinates)):
        coord_1 = previous_coordinates[i-1]
        coord_2 = previous_coordinates[i]
        coord_1 = [scale_x(coord_1[0]), scale_y(coord_1[1])]
        coord_2 = [scale_x(coord_2[0]), scale_y(coord_2[1])]
        pygame.draw.aaline(screen, color, coord_1, coord_2)

def draw_coordinate_system(screen):
    """Рисует оси физической системы координат.
    Args:
    **screen** - холст для рисования.
    """

    pygame.draw.circle(screen, BLACK, (20, window_height//2), 7, 2)
    pygame.draw.circle(screen, BLACK, (20, window_height//2), 2, 0)
    pygame.draw.line(screen, BLACK, (20, window_height//2), (80, window_height//2), 2)
    pygame.draw.line(screen, BLACK, (75, window_height//2+5), (80, window_height//2), 2)
    pygame.draw.line(screen, BLACK, (75, window_height//2-5), (80, window_height//2), 2)
    pygame.draw.line(screen, BLACK, (20, window_height//2), (20, window_height//2-60), 2)
    pygame.draw.line(screen, BLACK, (15, window_height//2-55), (20, window_height//2-60), 2)
    pygame.draw.line(screen, BLACK, (25, window_height//2-55), (20, window_height//2-60), 2)
    draw_sign_to_axes(screen)

def draw_sign_to_axes(screen):
    """Рисует подписи по осями координат.
    Args:
    **screen** - холст для рисования.
    """

    font = pygame.font.Font(None, 16)
    text_1 = font.render("x", True, BLACK)
    text_2 = font.render("y, E", True, BLACK)
    text_3 = font.render("z, B", True, BLACK)
    screen.blit(text_1, (80, window_height//2+7))
    screen.blit(text_2, (27, window_height//2-55))
    screen.blit(text_3, (18, window_height//2+9))

def print_text(screen, text, x, y, size):
    """Выводит текст на экран.

    Args:
    screen - объект типа pygame.Surface.  
    text - текст который нужно вывести.  
    (x, y) - координаты верхнего левого угла текста.
    size - шрифт текста
    """
    font = pygame.font.Font(None, size)
    text_to_surface = font.render(text, True, BLACK)
    screen.blit(text_to_surface, (x, y))
    

if __name__ == "__main__":
    print("This module is not for direct call!")
