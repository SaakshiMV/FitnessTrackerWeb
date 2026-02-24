import math

def calculate_angle(p1, p2, p3):
    """Calculate angle at joint p2 between points p1-p2-p3"""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    angle = math.degrees(
        math.atan2(y3 - y2, x3 - x2) - 
        math.atan2(y1 - y2, x1 - x2)
    )
    if angle < 0:
        angle += 360
    if angle > 180:
        angle = 360 - angle
    return angle