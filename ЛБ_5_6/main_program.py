from funk import sides, triangle_type, area

def main():
    try:
        a = float(input("Введите длину стороны a: "))
        b = float(input("Введите длину стороны b: "))
        c = float(input("Введите длину стороны c: "))
        triangle_sides = sides(a, b, c)

        if triangle_sides is not None:
            triangle_type_result = triangle_type(*triangle_sides)
            area_result = area(*triangle_sides)

            print(triangle_type_result)
            print(area_result)
    except ValueError:
        print("Некорректный ввод. Введите число")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
