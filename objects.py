"""Модуль содержит класс, который описывает частицу на экране.  """

class Particle:
    """Тип данных, описывающий частицу.
    Содержит массу, координаты, скорость частицы (нвчальные и текущие значения),
    массив с о всеми предыдущими координатами для прорисовки траектории,
    а также заряд частицы, её цвет и время запуска.
    """
    
    m = 0
    """Масса частицы"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    x0 = 0
    """Начальная координата по оси **x**"""

    y0 = 0
    """Начальная координата по оси **x**"""

    previous_coordinates = []
    """Массив хранит координаты частицы в каждом кадре"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    V0x = 0
    """Начальная скорость по оси **x**"""

    V0y = 0
    """Нчальная координата по оси **y**"""

    w_b = 0
    """Ларморовская частота"""

    q = 0
    """Заряд частицы относительно единичного"""

    start_time = 0
    """Время с начала программы "запуска" частицы"""

    R = 4
    """Визуальный радиус частицы в пикселях"""

    color = None
    """Цвет частицы на экране"""

    image = None
    """Изображение частицы"""

    def update(self, t):
        """Обновляет параметры частицы при изменение полей"""
        self.x0 = self.x
        self.y0 = self.y
        self.V0x = self.Vx
        self.V0y = self.Vy
        self.start_time = t


