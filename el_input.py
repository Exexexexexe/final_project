from objects import Particle

def read_electric_particle_data_from_file(input_filename):
    """Cчитывает данные о частицах из файла, создаёт сами частицы
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """

    electric_particles = []
    with open(input_filename) as input_file:
        for line in input_file:
            particles = []
            for _ in range(int(line[0])):
                particle = Particle()
                particles.append(particle)
            parse_particle_parametrs(line, particles)
            electric_particles.append(particles)
    return electric_particles


def parse_particle_parametrs(line, particles):
    """Считывает данные о частицах из строки.
    Входная строка должна иметь следующий формат:
    <Число частиц данного типа> <радиус в пикселях> <масса> <q> <x> <y> 

    Здесь (x, y) - начальные координаты частиц данного типа,
    q - заряд частицы относительно единичного.
    Пример строки:
    100 5 1e-30 2 10 10

    Параметры:
    **line** - строка с описанием частиц одного типа.  
    **particles** - массив с объектами частиц одного типа.
    """

    param = line.split()
    for particle in particles:
        particle.N = int(param[0])
        particle.R = float(param[1])
        particle.m = float(param[2])
        particle.q = float(param[3])*1.6e-19
        particle.x = float(param[4])
        particle.y = float(param[5])

def write_electric_particles_data_to_file(output_filename, electric_particles):
    """Сохраняет данные о частицах в файл.
    Строки должны иметь следующий формат:
    <Число частиц данного типа> <радиус в пикселях> <масса> <q> <x> <y>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for particles in electric_particles:
            print("%i %f %f %f %f %f %f" % (particles[0].N, particles[0].R, particles[0].m, paticles[0].q, particles[0].x, paticles[0].y), file=out_file)

if __name__ == "__main__":
    print("This module is not for direct call!")
