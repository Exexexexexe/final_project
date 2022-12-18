"""Модуль отвечает за обработку информации, введённой пользователем.  """

from constants import RED, BLUE, BLACK
from objects import Particle

fields = [0, 0]
"""Глобальная переменная содержит значение полей B и E в виде: [B, E].  """

particle_infa = {}
"""Глобальная переменная содержит информацию о не созданной частице.  """

electric_particles = []
"""Глобальная переменная содержит информацию, о всех существующих частицах.  """

mistake = False
"""Глобальная переменная, содержит информацию о наличии ошибки ввода.  """

changed_fields = False
"""Глобальная переменная, содержит информацию об изменении полей.  """

new_particle = False
"""Глобальная переменная, содержит информацию о создании новой частицы.  """


def procces_user_data(user_data):
    """Обрабатывает информацию введённую пользователем.  """
    global particle_infa, changed_fields
    if len(user_data):
        for data in user_data:
            if list(data.keys())[0][0] == '1':
                fields[0] = float(list(data.values())[0])
                changed_fields = True
            elif list(data.keys())[0][0] == '2':
                fields[1] = float(list(data.values())[0])
                changed_fields = True
            elif list(data.keys())[0][0] == 'a':
                particle_infa['m'] = float(list(data.values())[0])
            elif list(data.keys())[0][0] == 'б':
                particle_infa['q'] = int(list(data.values())[0])
            elif list(data.keys())[0][0] == 'в':
                particle_infa['x0'] = float(list(data.values())[0])
            elif list(data.keys())[0][0] == 'г':
                particle_infa['y0'] = float(list(data.values())[0])
            elif list(data.keys())[0][0] == 'д':
                particle_infa['Vx0'] = float(list(data.values())[0])
            elif list(data.keys())[0][0] == 'е':
                particle_infa['Vy0'] = float(list(data.values())[0])
        user_data.clear()
            
def add_particle():
    """Функция передоётся в class Button, при его создании.
    Добавляет новую частицу при нажатии кнопки.  
    """
    
    global particle_infa, electric_particles, new_particle, mistake
    
    if len(particle_infa) != 6:
        mistake = True
    else:
        if particle_infa['x0'] != 0 and particle_infa['y0'] != 0:
            mistake = True
        else:
            particle = Particle()
            particle.m = particle_infa['m']
            particle.q = particle_infa['q']
            particle.x = particle.x0 = particle_infa['x0']
            particle.y = particle.y0 = particle_infa['y0']
            particle.Vx = particle.V0x = particle_infa['Vx0']
            particle.Vy = particle.V0y = particle_infa['Vy0']
            particle.previous_coordinates = []
            particle_infa = {}
            electric_particles.append(particle)
            new_particle = True
            if particle.q > 0:
                particle.color = RED
            elif particle.q < 0:
                particle.color = BLUE
            else:
                particle.color = BLACK

def clear_screen():
    """Функция передоётся в class Button, при его создании.
    Удаляет все существующие частицы при нажатии кнопки.  
    """
    
    global electric_particles
    
    electric_particles.clear()

if __name__ == "__main__":
    print("This module is not for direct call!")      
