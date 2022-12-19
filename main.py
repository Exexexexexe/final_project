"""Главный модуль. Вызывает функции создания графических обЪектов.
Выполняет основной цикл программы.  
"""

import pygame
from model import calculate_larmour_frequency, recalculate_electric_particles_position
from vis import calculate_scale_factor, print_text, update_particle_position, \
draw_trajectory, draw_coordinate_system, window_width, window_height
from button import objects, input_buttons, user_data, Button, InputButton
from constants import WHITE
import user_data_proccesing as udp


def main():
    """Главная функция главного модуля, в ней вызываются функции создания
    графических объектов.
    Выполняет основной цикл.  
    """
    
    pygame.init()

    FPS = 30

    screen = pygame.display.set_mode((window_width, window_height))

    font = pygame.font.SysFont('Arial', 15)
    
    Button(screen, 400, 1, 75, 50, "Clear screen", font, udp.clear_screen)
    Button(screen, 0, 1, 75, 50, "Add particle", font, udp.add_particle)
    InputButton(screen, 650, 0, 75, 25, font, "1.Поле B: ")
    InputButton(screen, 650, 26, 75, 25, font, "2.Поле E: ")
    InputButton(screen, 80, 0, 75, 25, font, "a)Масса: ")
    InputButton(screen, 80, 26, 75, 25, font, "б)Заряд: ")
    InputButton(screen, 180, 0, 75, 25, font, "в)x0: ")
    InputButton(screen, 180, 26, 75, 25, font, "г)y0: ")
    InputButton(screen, 280, 0, 75, 25, font, "д)Vx0: ")
    InputButton(screen, 280, 26, 75, 25, font, "е)Vy0: ")

    calculate_scale_factor()

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    first_cycle = True
    start_time = 0
    
    while not finished:
        clock.tick(FPS)
        if first_cycle:
            screen.fill(WHITE)
            print_text(screen, "Введите данные полей и частицы", 200, 270, 40)
            pygame.display.update()
            pygame.time.delay(3000)
            screen.fill(WHITE)
            first_cycle = False
        udp.procces_user_data(user_data)
        if udp.mistake:
            print_text(screen, "Ошибка ввода!", 300, 250, 40)
            pygame.display.update()
            pygame.time.delay(3000)
            screen.fill(WHITE)
            for particle in udp.electric_particles:
                particle.start_time += 3  #  Обновляем начальное время частицы с учётом задержки
            udp.mistake = False
        for event in pygame.event.get():
            for inp in input_buttons:
                inp.handle_event(event)
            if event.type == pygame.QUIT:
                finished = True
        for obj in objects:
            obj.process()
        for inp in input_buttons:
            inp.update()
            inp.draw()
        if udp.new_particle:
            particle = udp.electric_particles[-1]  #  Новая частица находится в конце массива
            calculate_larmour_frequency(particle, udp.fields)
            particle.start_time = pygame.time.get_ticks()/1000    
            udp.new_particle = False
        if udp.changed_fields:
            for particle in udp.electric_particles:
                calculate_larmour_frequency(particle, udp.fields)
                particle.update(pygame.time.get_ticks()/1000)
            udp.changed_fields = False
        recalculate_electric_particles_position(udp.electric_particles, udp.fields, pygame.time.get_ticks()/1000)
        for particle in udp.electric_particles:
            update_particle_position(screen, particle)
            draw_trajectory(screen, particle)
        draw_coordinate_system(screen)
        print_text(screen, "Параметры", 540, 5, 25)
        print_text(screen, "полей", 560, 30, 25)
        pygame.display.update()
        screen.fill(WHITE)
    pygame.quit()
    
if __name__ == "__main__":
    main() 
