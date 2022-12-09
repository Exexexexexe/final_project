from constants import*

def calculate_force(particle, electric_particles, fields):
    """Вычисляет силу, действующую на тело.
    Параметры:
    **particle** - частица, для которой нужно вычислить действующую силу.  
    **electric_particles** - список обЪектов, которые воздействуют на тело.
    **fields** - значения перпендикулярных электрических и магнитного полей в виде:
    [Bz, Ey]
    """

    particle.Fx = particle.Fy = 0
    w_b = UNIT_CHARGE * particle.q * fields[0] / particle.m  # ларморовская частота
    particle.Fx += w_b * particle.Vy * particle.m
    particle.Fy += UNIT_CHARGE * particle.q * fields[1] - w_b * particle.Vx * particle.m
        
def move_electric_particles(particle, dt):
    """Перемещает частицу в соответствие с действующей на него силой.
    Параметры:
    **particle** - частицу, которую нужно 
    """
    
    particle.previous_coordinates.append([particle.x, particle.y])
    ax = particle.Fx/particle.m
    particle.x += particle.Vx * dt + ax * dt ** 2 / 2
    particle.Vx += ax*dt
    ay = particle.Fy / particle.m
    particle.y += particle.Vy * dt + ay * dt ** 2 / 2
    particle.Vy += ay * dt

def recalculate_electric_particles_position(electric_particles, fields, dt):
    """Пересчитывает координаты частиц.
    Параметры:
    **electric_particles** - список частиц, для которых нужно пересчитать координаты.
    **fields** - значения перпендикулярных электрических и магнитного полей в виде:
    [Bz, Ey]
    **dt** - шаг по времени
    """

    for particle in electric_particles:
        calculate_force(particle, electric_particles, fields)
    for particle in electric_particles:
            move_electric_particles(particle, dt)

if __name__ == "__main__":
    print("This module is not for direct call!")
