class Particle:
    """Тип данных, описывающий частицу.
    Содержит массу, координаты, скорость частицы,
    а также визуальный радиус частицы в пикселах и её заряд.
    """

    N = 0
    """Число частиц данного типа"""
    
    m = 0
    """Масса частицы"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус частицы"""

    q = 1.6e-19
    """Заряд частицы"""

    image = None
    """Изображение частицы"""

    fixed = False
