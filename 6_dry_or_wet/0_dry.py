def calc_area_rectangle(length, width):
    return length * width

def calc_area_circle(radius):
    return 3.14 * radius ** 2

def calc_area_triangle(base, height):
    return 0.5 * base * height

area1 = calc_area_rectangle(10, 5)
area2 = calc_area_circle(7)
area3 = calc_area_triangle(14, 7)

print(f"Area 1: {area1}, Area 2: {area2}, Area 3: {area3}")
