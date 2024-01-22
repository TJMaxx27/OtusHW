
from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a, name="Square"):
        if side_a <= 0:
            raise ValueError("Нельзя создать квадрат")
        super().__init__(side_a, side_a, name)


