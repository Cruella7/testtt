def sides(a, b, c):
    try:
        if a <= 0 or b <= 0 or c <= 0:
            return None
        elif a + b <= c or a + c <= b or b + c <= a:
            return None
        else:
            return a, b, c
    except ValueError:
        return None


def triangle_type(a, b, c):
    if a == b == c:
        return "Это равносторонний треугольник"
    elif a == b or a == c or b == c:
        return "Это равнобедренный треугольник"
    else:
        return "Это разносторонний треугольник"


def area(a, b, c):
    # Calculate the area of a triangle
    p = (a + b + c) / 2
    if a == b == c:
        s = (a ** 2 * 3 ** (1 / 2)) / 4
    elif a == b or a == c or b == c:
        s = (b * (p - a) * (p - c)) ** (1 / 2)
    else:
        s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
    return "Площадь треугольника:", s
