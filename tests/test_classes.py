from OtusHW.src.Rectangle import Rectangle
from OtusHW.src.Square import Square
from OtusHW.src.Triangle import Triangle
from OtusHW.src.Circle import Circle
import pytest


@pytest.mark.parametrize(('side_a', 'side_b', 'expected_area'),
                         [(3, 5, 15),
                          (3.5, 5.5, 19.25)],
                         ids=['integer', 'float'])
def test_rectangle(side_a, side_b, expected_area):
    r = Rectangle(side_a, side_b, name='Rectangle')
    assert r.get_area() == expected_area


@pytest.mark.parametrize(('side_a', 'expected_area'),
                         [(5, 25),
                          (5.5, 30.25)
                          ],
                         ids=['integer', 'float'])
def test_square(side_a, expected_area):
    r = Square(side_a)
    assert r.get_area() == expected_area


@pytest.mark.parametrize(('side_a', 'side_b', 'side_c', 'expected_area'),
                         [
                             (3, 4, 5, 6.0),  # Обычный треугольник/regular
                             (3, 3, 3, 3.897),  # Равносторонний треугольник/equilateral
                             (4, 4, 5, 7.806),  # Равнобедренный/isosceles
                         ],
                         ids=['TriangleRegular', 'TriangleEquilateral', 'TriangleIsosceles'])
def test_triangle(side_a, side_b, side_c, expected_area):
    r = Triangle(side_a, side_b, side_c, name='Triangle')
    assert round(r.get_area(), 3) == round(expected_area, 3)


def test_triangle_negative_sides():
    with pytest.raises(ValueError):
        Triangle(-3, 4, -5, name='Triangle')


@pytest.mark.parametrize(('radius', 'expected_area'),
                         [(2, 12.56),
                          (3.33, 34.819)
                          ],
                         ids=['integer', 'float'])
def test_circle(radius, expected_area):
    r = Circle(radius, name='Circle')
    assert round(r.get_area(), 3) == round(expected_area, 3)


def test_circle_negative_radius():
    with pytest.raises(ValueError):
        Circle(-2, name='Circle')


def test_circle_zero_radius():
    with pytest.raises(ValueError):
        Circle(0, name='Circle')


@pytest.mark.parametrize(('figure1', 'figure2', 'expected_sum'),
                         [
                             (Rectangle(3, 4, 'Rectangle'), Circle(5, 'Circle'), 90.5),
                             (Triangle(3, 4, 5, 'Triangle'), Square(5), 31),
                             (Triangle(3, 3, 3, 'Triangle'), Triangle(4, 4, 5, 'Triangle'), 11.703)
                         ],
                         ids=['Rectangle_and_Circle', 'Triangle_and_Square', 'TriangleEquilateral_and_TriangleIsosceles'])
def test_area_figure_sum(figure1, figure2, expected_sum):
    result = figure1.get_area() + figure2.get_area()
    assert round(result, 3) == round(expected_sum, 3)
