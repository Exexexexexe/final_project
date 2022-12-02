from objects import Particle


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
    **particles** - массив с объектами частиц.
    """

    param = line.split()
    for particle in particles:
        particle.R = float(param[1])
        particle.m = float(param[2])
        particle.q = float(param[3])
        particle.x = float(param[4])
        particle.y = float(param[5])


if __name__ == "__main__":
    print("This module is not for direct call!")
