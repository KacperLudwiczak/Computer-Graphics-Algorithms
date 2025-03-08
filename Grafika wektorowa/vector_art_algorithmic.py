import webbrowser
import os

def bresenham_line(x0, y0, x1, y1):
    """Algorytm Bresenhama do rysowania linii"""
    points = []
    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
    err = dx + dy

    while True:
        points.append(f"{x0},{y0}")
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy

    return " ".join(points)

def bresenham_circle(cx, cy, r):
    """Algorytm Bresenhama do rysowania okręgu"""
    points = []
    x, y = r, 0
    d = 1 - r

    def plot_points(x, y):
        coords = [
            (cx + x, cy + y), (cx - x, cy + y),
            (cx + x, cy - y), (cx - x, cy - y),
            (cx + y, cy + x), (cx - y, cy + x),
            (cx + y, cy - x), (cx - y, cy - x)
        ]
        for px, py in coords:
            points.append(f"{px},{py}")

    while x >= y:
        plot_points(x, y)
        y += 1
        if d < 0:
            d += 2 * y + 1
        else:
            x -= 1
            d += 2 * (y - x) + 1

    return " ".join(points)

def generate_mountain(x1, y1, x2, y2, x3, y3):
    """Tworzy ścieżkę SVG dla góry"""
    return f"M{x1},{y1} L{x2},{y2} L{x3},{y3} Z"

def generate_svg():
    svg_code = f'''<?xml version="1.0" encoding="UTF-8"?>
    <svg width="500" height="300" xmlns="http://www.w3.org/2000/svg">
    
    <!-- Tło -->
    <rect width="100%" height="100%" fill="lightblue" />

    <!-- Słońce (za pomocą okręgu Bresenhama) -->
    <polyline points="{bresenham_circle(400, 50, 30)}" fill="yellow" stroke="orange" stroke-width="3"/>

    <!-- Góry (za pomocą własnych ścieżek) -->
    <path d="{generate_mountain(50,240,150,140,250,240)}" fill="gray" stroke="black" stroke-width="2"/>
    <path d="{generate_mountain(180,240,300,130,420,240)}" fill="darkgray" stroke="black" stroke-width="2"/>
    <path d="{generate_mountain(350,240,450,160,550,240)}" fill="dimgray" stroke="black" stroke-width="2"/>

    <!-- Drzewa (za pomocą okręgów Bresenhama + linii) -->
    <polyline points="{bresenham_line(50, 210, 50, 250)}" stroke="saddlebrown" stroke-width="5"/>
    <polyline points="{bresenham_circle(50, 200, 20)}" fill="green" />

    <polyline points="{bresenham_line(400, 210, 400, 250)}" stroke="saddlebrown" stroke-width="5"/>
    <polyline points="{bresenham_circle(400, 200, 20)}" fill="green" />

    <!-- Trawa (na dole ekranu) -->
    <rect y="240" width="100%" height="60" fill="green" />
    </svg>'''

    with open("vector_art_algorithmic.svg", "w", encoding="utf-8") as file:
        file.write(svg_code)

    print("Plik SVG został wygenerowany: vector_art_algorithmic.svg")

    # Automatyczne otwarcie w przeglądarce
    webbrowser.open("file://" + os.path.abspath("vector_art_algorithmic.svg"))

# 🔹 Wygenerowanie SVG
generate_svg()
