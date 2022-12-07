electric_constant = 8.9918e9
""" Электрическая постоянная в законе Кулона"""

def calculate_force(particle, electric_particles, fields):
    """Вычисляет силу, действующую на тело.
    Параметры:
    **particle** - частица, для которой нужно вычислить действующую силу.  
    **electric_particles** - список обЪектов, которые воздействуют на тело.
    **fields** - значения перпендикулярных электрических и магнитного полей в виде:
    [Bz, Ey]
    """

    particle.Fx = particle.Fy = 0
    for particles in electric_particles:
        for partic in particles:
            if partic == particle:
                continue  # тело не действует силой Кулона на само себя!
            r =((particle.x - partic.y)**2 +(particle.y - partic.y)**2)**0.5
            particle.Fx += electric_constant * particle.q * partic.q * (particle.x - partic.x) / (r ** 3)
            particle.Fy += electric_constant * particle.q * partic.q * (particle.y - partic.y) / (r ** 3)
    w_b = particle.q * fields[0] / particle.m  # ларморовская частота
    particle.Fx += w_b * particle.Vy * particle.m
    particle.Fy += particle.q * fields[1] - w_b * particle.Vx * particle.m
    if particle.fixed:
        particle.Fx = particle.Fy = 0
        particle.Vx = particle.Vy = 0
        
def move_electric_particles(particle, dt):
    """Перемещает частицу в соответствие с действующей на него силой.
    Параметры:
    **particle** - частицу, которую нужно 
    """

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

    for particles in electric_particles:
        for particle in particles:
            calculate_force(particle, electric_particles, fields)
    for particles in electric_particles:
        for particle in particles:
            move_electric_particles(particle, dt)

if __name__ == "__main__":
    print("This module is not for direct call!")
