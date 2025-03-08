// Algorytm Bresenhama do rysowania linii. 
// Wykorzystuje tylko operacje całkowite.

function bresenhamLine(x0, y0, x1, y1, width = 40, height = 20) {
    let grid = Array.from({ length: height }, () => Array(width).fill(" "));

    let dx = Math.abs(x1 - x0), sx = x0 < x1 ? 1 : -1;
    let dy = -Math.abs(y1 - y0), sy = y0 < y1 ? 1 : -1;
    let err = dx + dy;

    while (true) {
        if (x0 >= 0 && x0 < width && y0 >= 0 && y0 < height) {
            grid[height - y0 - 1][x0] = "•"; 
        }
        if (x0 === x1 && y0 === y1) break;
        let e2 = 2 * err;
        if (e2 >= dy) { err += dy; x0 += sx; }
        if (e2 <= dx) { err += dx; y0 += sy; }
    }

    console.log(grid.map(row => row.join("")).join("\n"));
}

bresenhamLine(2, 2, 30, 15);
