import pygame
import numpy
from vis import *
from model import *
from el_input import *

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

physical_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

displayed_time = None
"""Отображаемое на экране время.
Тип: переменная pygame"""

time_step = None
"""Шаг по времени при моделировании.
Тип: float"""

electric_particles = []
"""Список частиц."""

def main():
    """Главная функция главного модуля.
    Создаёт оюъекты графического дизайна библиотеки pygame: окноб холст.
    """
    global electric_particles

    electric_particles = read_electric_particle_data_from_file("one_particle.txt")
    fields = [2e-7, 1e-6]
    
    pygame.init()

    FPS = 30

    window_width = 800
    """Ширина окна"""

    window_height = 600
    """Высота окна"""

    screen = pygame.display.set_mode((window_width, window_height))
    
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    first_cycle = True

    while not finished:
        if numpy.isnan(electric_particles[0][0].Fy):
            finished = True
            print("Yeee")
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == True:
                finished = True
        if first_cycle:
            for particles in electric_particles:
                for particle in particles:
                    create_particle_image(screen, particle)
            first_cycle = False
        recalculate_electric_particles_position(electric_particles, fields, dt)
        for particles in electric_particles:
            for particle in particles:
                update_particle_position(screen, particle)
        pygame.display.update()
        screen.fill((0, 0, 0))
        
    pygame.quit()
    
if __name__ == "__main__":
    main() 
