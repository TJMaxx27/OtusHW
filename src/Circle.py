from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius, name):
        super().__init__(name)
        if radius <= 0:
            raise ValueError("Нельзя создать круг с неположительным радиусом")
        self.radius = radius

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

    def get_area(self):
        return 3.14 * self.radius**2

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()

