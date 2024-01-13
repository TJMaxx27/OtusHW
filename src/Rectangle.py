from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b, name):
        super().__init__(name='Rectangle')
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Нельзя создать прямоугольник")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return 0




