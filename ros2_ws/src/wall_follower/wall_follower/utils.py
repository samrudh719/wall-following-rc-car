import math


def clamp(value,
          minimum,
          maximum):

    return max(min(value,
                   maximum),
               minimum)


def normalize_angle(angle):

    while angle > math.pi:
        angle -= 2 * math.pi

    while angle < -math.pi:
        angle += 2 * math.pi

    return angle