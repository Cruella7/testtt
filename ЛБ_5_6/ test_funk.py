from funk import sides, triangle_type, area

def test_sides():
    result = sides(3, 4, 5)
    assert result is not None, "Test test_sides(a, b, c) is Fail for valid input"

    result = sides(0, 4, 5)
    assert result is None, "Test test_sides(a, b, c) is Fail for zero side"

    result = sides(-1, 4, 5)
    assert result is None, "Test test_sides(a, b, c) is Fail for negative side"

    print("Test test_sides(a, b, c) is OK")

def test_triangle_type():
    result = triangle_type(3, 3, 3)
    assert result == "Это равносторонний треугольник", "Test test_triangle_type(a, b, c) is Fail for equilateral triangle"

    result = triangle_type(4, 4, 3)
    assert result == "Это равнобедренный треугольник", "Test test_triangle_type(a, b, c) is Fail for isosceles triangle"

    result = triangle_type(5, 7, 9)
    assert result == "Это разносторонний треугольник", "Test test_triangle_type(a, b, c) is Fail for scalene triangle"

    print("Test test_triangle_type(a, b, c) is OK")

def test_area():
    result = area(3, 3, 3)
    assert result == ("Площадь треугольника:", 3.897114317029974), "Test test_area(a, b, c) is Fail for equilateral triangle"

    result = area(4, 4, 3)
    assert result == ("Площадь треугольника:", 5.562148865321747), "Test test_area(a, b, c) is Fail for isosceles triangle"

    result = area(5, 7, 9)
    assert result == ("Площадь треугольника:", 17.41228014936585), "Test test_area(a, b, c) is Fail for scalene triangle"

    print("Test test_area(a, b, c) is OK")

test_sides()
test_triangle_type()
test_area()
