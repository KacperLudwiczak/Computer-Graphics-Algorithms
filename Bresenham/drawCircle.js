// Algorytm rysowania okręgu (Bresenhama). 
// Stosuje tylko operacje na liczbach całkowitych.

function drawCircle(xc, yc, r, width = 40, height = 20) {
    let grid = Array.from({ length: height }, () => Array(width).fill(" "));

    let x = 0, y = r;
    let d = 3 - 2 * r;
    
    function plotPoints(x, y) {
        let points = [
            [xc + x, yc + y], [xc - x, yc + y],
            [xc + x, yc - y], [xc - x, yc - y],
            [xc + y, yc + x], [xc - y, yc + x],
            [xc + y, yc - x], [xc - y, yc - x]
        ];
        points.forEach(([px, py]) => {
            if (px >= 0 && px < width && py >= 0 && py < height) {
                grid[height - py - 1][px] = "•";
            }
        });
    }

    while (y >= x) {
        plotPoints(x, y);
        x++;
        if (d > 0) {
            y--;
            d += 4 * (x - y) + 10;
        } else {
            d += 4 * x + 6;
        }
    }

    console.log(grid.map(row => row.join("")).join("\n"));
}

drawCircle(20, 10, 8);
