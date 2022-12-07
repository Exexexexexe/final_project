"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие графические объекты и перемещающие их на экране, принимают физические координаты
"""

import pygame

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 800
"""Ширина окна"""

window_height = 600
"""Высота окна"""

scale_factor = 1
"""Масштабирование экранных координат по отношению к физическим.
Тип: int
Мера: количество пикселей на один метр."""


def scale_x(x):
    """Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Параметры:
    **x** — x-координата модели.
    """

    return int(x*scale_factor) + window_width/2


def scale_y(y):
    """Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.
    Параметры:
    **y** — y-координата модели.
    """

    return int(-y*scale_factor) + window_height/2

def create_particle_image(space, particle):
    """Создаёт отображаемый объект частицыы.
    Параметры:
    **space** — холст для рисования.
    **particle** — объект частицы.
    
    """
    
    x = particle.x
    y = particle.y
    r = particle.R
    particle.image = pygame.draw.circle(space, (255, 0, 0), (x, y), r, 0)

def update_particle_position(space, particle):
    """Перемещает отображаемый объект на холсте.
    Параметры:
    **space** — холст для рисования.
    **particle** — частица, которую нужно переместить.
    """
    x = particle.x
    y = particle.y
    r = particle.R
    if x + 10*r < 0 or x - 10*r > window_width or y + 10*r < 0 or y - 10*r > window_height:
        particle.fixed = True # частица не может выйти за пределы образца
    pygame.draw.circle(space, (255, 0, 0), (x, y), r, 0)    

if __name__ == "__main__":
    print("This module is not for direct call!")
