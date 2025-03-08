def dda_line(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))

    x_incr = dx / steps
    y_incr = dy / steps

    x, y = x0, y0
    pixels = []

    for _ in range(int(steps) + 1):
        pixels.append((round(x), round(y)))
        x += x_incr
        y += y_incr

    return pixels

def draw_terminal_line(x0, y0, x1, y1, width=50, height=20):
    pixels = dda_line(x0, y0, x1, y1)
    
    # Tworzenie pustej siatki
    grid = [[" " for _ in range(width)] for _ in range(height)]
    
    # Rysowanie pikseli na siatce (uwzględniając odwróconą oś Y terminala)
    for x, y in pixels:
        if 0 <= x < width and 0 <= y < height:
            grid[height - y - 1][x] = "•"  # Odwracamy oś Y

    # Wyświetlenie siatki w terminalu
    for row in grid:
        print("".join(row))

# Przykładowe rysowanie linii w terminalu
draw_terminal_line(2, 2, 30, 15)
