from convex_hull import orientation
from convex_hull import gift_wrapping


def test_collinear_orientation():
    assert orientation((0, 0), (1, 1), (2, 2)) == 0


def test_clockwise_orientation():
    assert orientation((0, 0), (1, 1), (2, 0)) == -1


def test_counterclockwise_orientation():
    assert orientation((0, 0), (1, 0), (2, 2)) == 1


def test_gift_wrapping():
    points = [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0), (3, 3)]
    hull = gift_wrapping(points)
    assert set(hull) == {(0, 0), (0, 2), (2, 0), (3, 3)}


def test_empty_list():
    points = []
    hull = gift_wrapping(points)
    assert hull == []
