"""Модуль физической модели.
Вычисляет физические координаты частицы в каждый момент времени, в соответствие
с уравнением движения.  
"""

import math
from constants import UNIT_CHARGE

def calculate_larmour_frequency(particle, fields):
    """Расчитывает ларморовскую частоту частицы в данном магнитном поле.  """
    particle.w_b = UNIT_CHARGE*particle.q*fields[0]/particle.m
        
def move_electric_particles(particle, fields, t):
    """Перемещает частицу в соответствие с уравнением движения.
    Параметры:
    **particle** - частицу, которую нужно 
    """

    if fields[0] != 0:
        V_drift = fields[1]/fields[0]
    w_b = particle.w_b
    x0 = particle.x0
    y0 = particle.y0
    V0x = particle.V0x
    V0y = particle.V0y
    V0 = (V0x**2 + V0y**2) ** 0.5
    particle.previous_coordinates.append([particle.x, particle.y])
    t -= particle.start_time
    #Записываем в явном виде решение уравнения движения
    if w_b != 0:
        particle.x = (V_drift)*t - ((V_drift-V0)/abs(w_b))*math.sin(abs(w_b)*t) - (V0y/w_b)*math.cos(abs(w_b)*t) + x0 + V0y/w_b
        particle.y = ((V_drift-V0)/w_b) * (1-math.cos(abs(w_b*t))) + (V0y/abs(w_b))*math.sin(abs(w_b)*t) + y0
    else:
        particle.x = x0 + V0x*t
        particle.y = UNIT_CHARGE*particle.q*fields[1]/2*particle.m * t**2 + V0y*t + y0
        
def recalculate_electric_particles_position(electric_particles, fields, t):
    """Пересчитывает координаты частиц.
    Параметры:
    **electric_particles** - список частиц, для которых нужно пересчитать координаты.
    **fields** - значения перпендикулярных электрических и магнитного полей в виде:
    [Bz, Ey]
    **dt** - шаг по времени
    """

    for particle in electric_particles:
        move_electric_particles(particle, fields, t)

if __name__ == "__main__":
    print("This module is not for direct call!")
