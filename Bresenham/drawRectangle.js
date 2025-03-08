// Algorytm rysowania prostokąta. Wykorzystuje proste iteracje, aby rysować poziome i pionowe odcinki.
// Może być implementowany przy użyciu algorytmu Bresenhama dla linii, ale w prostszych przypadkach wystarczy iteracja.

function drawRectangle(x0, y0, x1, y1, width = 40, height = 20) {
    let grid = Array.from({ length: height }, () => Array(width).fill(" "));

    for (let x = x0; x <= x1; x++) {
        if (x >= 0 && x < width) {
            if (y0 >= 0 && y0 < height) grid[height - y0 - 1][x] = "•";
            if (y1 >= 0 && y1 < height) grid[height - y1 - 1][x] = "•";
        }
    }

    for (let y = y0; y <= y1; y++) {
        if (y >= 0 && y < height) {
            if (x0 >= 0 && x0 < width) grid[height - y - 1][x0] = "•";
            if (x1 >= 0 && x1 < width) grid[height - y - 1][x1] = "•";
        }
    }

    console.log(grid.map(row => row.join("")).join("\n"));
}

drawRectangle(5, 5, 25, 15);
