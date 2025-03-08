# Algorytm Bresenhama do rysowania linii
def draw_line(x0, y0, x1, y1, width=40, height=20):
    grid = [[" " for _ in range(width)] for _ in range(height)]

    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
    err = dx + dy

    while True:
        if 0 <= x0 < width and 0 <= y0 < height:
            grid[height - y0 - 1][x0] = "•"
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy

    # Wyświetlenie w terminalu
    for row in grid:
        print("".join(row))


# Algorytm Bresenhama do rysowania okręgu
def draw_circle(xc, yc, r, width=40, height=20):
    grid = [[" " for _ in range(width)] for _ in range(height)]

    x = 0
    y = r
    d = 3 - 2 * r

    def plot_points(x, y):
        points = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]
        for px, py in points:
            if 0 <= px < width and 0 <= py < height:
                grid[height - py - 1][px] = "•"

    while y >= x:
        plot_points(x, y)
        x += 1
        if d > 0:
            y -= 1
            d += 4 * (x - y) + 10
        else:
            d += 4 * x + 6

    # Wyświetlenie w terminalu
    for row in grid:
        print("".join(row))

# Algorytm rysowania prostokąta (Bounding Box Algorithm)
def draw_rectangle(x0, y0, x1, y1, width=40, height=20):
    grid = [[" " for _ in range(width)] for _ in range(height)]

    # Rysowanie poziomych boków
    for x in range(x0, x1 + 1):
        if 0 <= x < width:
            if 0 <= y0 < height:
                grid[height - y0 - 1][x] = "•"
            if 0 <= y1 < height:
                grid[height - y1 - 1][x] = "•"

    # Rysowanie pionowych boków
    for y in range(y0, y1 + 1):
        if 0 <= y < height:
            if 0 <= x0 < width:
                grid[height - y - 1][x0] = "•"
            if 0 <= x1 < width:
                grid[height - y - 1][x1] = "•"

    # Wyświetlenie w terminalu
    for row in grid:
        print("".join(row))


# Algorytm rysowania trójkąta (Triangle Outline Algorithm)
def draw_triangle(x0, y0, x1, y1, x2, y2, width=40, height=20):
    grid = [[" " for _ in range(width)] for _ in range(height)]

    def draw_line(x0, y0, x1, y1):
        dx = abs(x1 - x0)
        sx = 1 if x0 < x1 else -1
        dy = -abs(y1 - y0)
        sy = 1 if y0 < y1 else -1
        err = dx + dy

        while True:
            if 0 <= x0 < width and 0 <= y0 < height:
                grid[height - y0 - 1][x0] = "•"
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    # Rysowanie trzech krawędzi trójkąta
    draw_line(x0, y0, x1, y1)
    draw_line(x1, y1, x2, y2)
    draw_line(x2, y2, x0, y0)

    # Wyświetlenie w terminalu
    for row in grid:
        print("".join(row))


# Testowanie algorytmów w terminalu
print("Linia:")
draw_line(2, 2, 30, 15)

print("\nKoło:")
draw_circle(20, 10, 8)

print("Prostokąt:")
draw_rectangle(5, 5, 25, 15)

print("\nTrójkąt:")
draw_triangle(5, 5, 20, 15, 35, 5)
