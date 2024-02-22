import math
from closest_pair import closest_points
from closest_pair import brute_force


def test_closest_pair():
    points = [(1, 3), (-4, 5), (6, 2), (7, 4), (-2, -4)]
    result = closest_points(points)
    assert result == ((6, 2), (7, 4))


def test_closest_pair_empty():
    result = closest_points([])
    assert result == (None, None)


def test_closest_pair_collinear_points():
    points = [(0, 0), (1, 1), (2, 2)]
    result = closest_points(points)
    assert result in [((0, 0), (1, 1)), ((1, 1), (2, 2))]


def test_square():
    points = [(0, 0), (0, 1), (1, 0), (1, 1)]
    result = closest_points(points)
    assert result in [((0, 0), (0, 1)), ((0, 0), (1, 0)), ((1, 0), (1, 1)), (0, 1), (1, 1)]


def test_all_negative():
    points = [(-1, -3), (-4, -5), (-6, -2), (-7, -4), (-2, -4)]
    result = closest_points(points)
    assert result == ((-2, -4), (-1, -3))


def test_brute_force():
    points = [(1, 3), (-4, 5), (6, 2), (7, 4), (-2, -4)]
    result = brute_force(points)
    assert result == ((6, 2), (7, 4))
