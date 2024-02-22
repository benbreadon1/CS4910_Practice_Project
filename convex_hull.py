import math as m


def orientation(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = *p1, *p2, *p3  # unpack points into xy coords
                                            # We need this to determine the next point to be added to the hull
    d = (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)  # Using slope magnitude to determine orientation
    if d > 0:
        return 1  # if first slope smaller than second, counterclockwise
    elif d < 0:
        return -1  # if second slope smaller than first, clockwise
    else:
        return 0  # else, collinear (straight line)


def gift_wrapping(points):
    if not points:
        return []  # handles empty list case

    on_hull = min(points)  # find leftmost point (smallest x value)
    hull = []  # create list to store points in hull

    while True:
        hull.append(on_hull)  # add first point to the hull, start searching
        next_point = points[0]  # assume that the first point is the next point
        for point in points:
            o = orientation(on_hull, next_point, point)  # start by calculating orientation of
                                                         # current point, next point, and current loop point
            if next_point == on_hull or o == 1 or (o == 0 and m.dist(on_hull, point) > m.dist(on_hull, next_point)):
                # if the next point is already on the hull or the orientation is counterclockwise,
                # update next_point to current point.  We don't want counterclockwise points or collinear
                # points, so we add that if the distance between the current hull point and the point we're
                # looking at is greater than the current next point we update next_point
                next_point = point
        on_hull = next_point  # after we've found the new point, we update the hull and repeat the whole loop
        if on_hull == hull[0]:  # if we end up at the beginning, we know we're done
            break

    return hull


points1 = [(0, 0), (1, 1), (1, 2), (2, 2), (3, 0)]
points2 = [(0, 3), (3, 3), (2, 1), (1, 3), (2, 0)]

gift_wrapping(points1)
gift_wrapping(points2)
