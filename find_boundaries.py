def find_boundaries(toponym):
    bounded_by = toponym["boundedBy"]["Envelope"]

    lower_corner = bounded_by["lowerCorner"].split()
    upper_corner = bounded_by["upperCorner"].split()

    delta_x = str(abs(float(lower_corner[0]) - float(upper_corner[0])))
    delta_y = str(abs(float(lower_corner[1]) - float(upper_corner[1])))
    return delta_x, delta_y
