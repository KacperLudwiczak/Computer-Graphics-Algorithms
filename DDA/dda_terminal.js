function DDALine(x0, y0, x1, y1, width = 220, height = 200) {
    let dx = x1 - x0;
    let dy = y1 - y0;
    let steps = Math.max(Math.abs(dx), Math.abs(dy));

    let x_incr = dx / steps;
    let y_incr = dy / steps;

    let x = x0;
    let y = y0;

    // Tworzenie pustej siatki
    let grid = Array.from({ length: height }, () => Array(width).fill(" "));

    // Rysowanie pikseli
    for (let i = 0; i <= steps; i++) {
        let px = Math.round(x);
        let py = Math.round(y);

        if (px >= 0 && px < width && py >= 0 && py < height) {
            grid[height - py - 1][px] = "•"; // Odwrócenie osi Y
        }

        x += x_incr;
        y += y_incr;
    }

    // Wyświetlenie siatki w terminalu
    console.log(grid.map(row => row.join("")).join("\n"));
}

// Przykładowe rysowanie linii w terminalu
DDALine(200, 180, 180, 160);
