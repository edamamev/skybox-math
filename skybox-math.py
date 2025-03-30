import math
import numpy as np

KILOMETRES_PER_LIGHTYEAR = 9460730472000
KILOMETRES_PER_AU = 149600000
SUN_RADIUS_KM = 695700
ARCSECONDS_PER_RADIAN = math.pi / 648000


def draw_star(star_diameter, star_vector):
    star_distance = get_vector_magnitude(star_vector)
    star_angular_diameter = get_star_angular_diameter(star_diameter, star_distance)

    star_point = get_unit_vector(star_vector)
    star_inclination = get_angle_between_center_and_point(star_point)
    star_tangent_vector = get_point_tangent_unit_vector(star_point, star_inclination)
    star_tangent_vector_rotated = rotate_tangent_unit_vector(star_point, star_tangent_vector)

    star_physical_radius = math.sin(star_angular_diameter / 2)
    print("Distance km: ",star_distance)
    print("Angular Diameter rad: ", star_angular_diameter)
    print("Normal Vector: ", star_point)
    print("Inclination: ", star_inclination)
    print("Tangent Vector: ", star_tangent_vector)
    print("Rotated Tangent Vector: ", star_tangent_vector_rotated)
    return star_physical_radius


def get_star_angular_diameter(star_diameter, star_distance):
    """
    Returns the Star's Angular Diameter in Radians.
    Both the Stars Diameter in Distance must be in the same unit.
    """
    return star_diameter / star_distance


def get_angle_between_center_and_point(P):
    if (P[2] == 0):
        return 0
    Q = (P[0], P[1], 0)
    H = 1
    length_OQ = math.sqrt(\
        pow(P[0], 2)\
        + pow(P[1], 2)\
        )
    return math.acos(length_OQ)


def rotate_tangent_unit_vector(normal_vector, tangent_vector):
    normal_vector = np.array(normal_vector)
    tangent_vector = np.array(tangent_vector)
    cross = np.cross(normal_vector, tangent_vector)
    cos = math.cos(math.pi / 2)
    sin = math.sin(math.pi / 2)
    v = (cos * tangent_vector) + (sin * cross)
    return v


def get_point_tangent_unit_vector(P, theta):
    if (theta == 0):
        return 0
    Sz = csc(theta)
    if (P[2] > 0):
        S = (0, 0,  Sz)
    else:
        S = (0, 0, -Sz)
    tangent_vector = get_vector_from_points(P, S)
    return get_unit_vector(tangent_vector)
    

def get_unit_vector(vector):
    magnitude = get_vector_magnitude(vector)
    return (\
        vector[0] / magnitude, \
        vector[1] / magnitude, \
        vector[2] / magnitude
    )


def get_vector_magnitude(vector):
    return math.sqrt(\
        pow(vector[0], 2)\
        + pow(vector[1], 2)\
        + pow(vector[2], 2)\
    )


def get_vector_from_points(p1, p2):
    return (\
        p2[0] - p1[0],\
        p2[1] - p1[1],\
        p2[2] - p1[2]\
    )


def csc(angle):
    return 1 / math.sin(angle)


def get_arc_minutes_from_radians(radians):
    return radians * math.pi / 10800


def get_arc_minutes_from_degrees(degrees):
    return degrees * 60


def get_arc_seconds_from_radians(radians):
    return radians * ARCSECONDS_PER_RADIAN


def get_arc_seconds_from_degrees(degrees):
    return get_arc_minutes_from_degrees(degrees) * 60


def get_milliarc_seconds_from_arc_seconds(arcseconds):
    return arcseconds * 1000


def get_milliarc_seconds_from_radians(radians):
    return get_arc_seconds_from_radians(radians) * 1000


def get_radians_from_degrees(degrees):
    return degrees * (math.pi / 180)


def get_degrees_from_radians(radians):
    return radians * (180 / math.pi)


def get_km_from_ly(ly):
    return ly * KILOMETRES_PER_LIGHTYEAR


def get_km_from_au(au):
    return au * KILOMETRES_PER_AU


def get_normalised_vector(vector):
    vector = np.array(vector)
    vector_magnitude = np.linalg.norm(vector)
    return vector / vector_magnitude


def get_angular_diameter_in_radians(object_diameter, object_distance):
    return 2 * math.atan(object_diameter / object_distance)


def get_radians_angle_of_normalised_vector_from_centre(normalised_vector):
    return math.acos(\
        math.sqrt(\
            (normalised_vector[0] * normalised_vector[0])\
            + (normalised_vector[1] * normalised_vector[1])\
        )\
    )
#star_vector = [1,5,7]
#star_distance_ly = 405
# star_radius_km = SUN_RADIUS_KM
# star_distance_au = 1

# star_distance_km = get_km_from_au(star_distance_au)
# star_angular_diameter_in_radians = get_angular_diameter_in_radians(star_radius_km, star_distance_km)
# print("Radians:", star_angular_diameter_in_radians)
# print("Degrees: ", get_degrees_from_radians(star_angular_diameter_in_radians))
# print("Arc Seconds: ", get_arc_seconds_from_radians(star_angular_diameter_in_radians))
# print("Milliarc Seconds: ",  get_milliarc_seconds_from_radians(star_angular_diameter_in_radians))

star_diameter = 1.2 * SUN_RADIUS_KM
star_vector_ly = [1,3,5]
star_vector_km = [\
        get_km_from_ly(star_vector_ly[0]),\
        get_km_from_ly(star_vector_ly[1]),\
        get_km_from_ly(star_vector_ly[2])\
    ]

#print(draw_star(star_diameter, star_vector_km))
point = get_unit_vector(star_vector_ly)
print("Point: ", point)
angle = get_angle_between_center_and_point(point)
print("Angle: ", angle)
tangent = get_point_tangent_unit_vector(point, angle)
print("Tangent: ", tangent)

tangent_vector = get_vector_from_points(point, tangent)
rotated_tangent = rotate_tangent_unit_vector(point, tangent_vector)
print("Tangent Vector: ",tangent_vector)
print("Rotated Tangent Vector:", rotated_tangent)
print(rotated_tangent + point)