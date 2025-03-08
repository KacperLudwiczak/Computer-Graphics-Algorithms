// JS program for DDA Line generation 

function round(n) { 
	if (n - Math.floor(n) < 0.5) 
		return Math.floor(n); 
	return Math.floor(n + 1); 
}; 

function DDALine(x0, y0, x1, y1) { 
	let dx = x1 - x0; 
	let dy = y1 - y0; 
	let step; 

	if (Math.abs(dx) > Math.abs(dy)) 
		step = Math.abs(dx); 
	else
		step = Math.abs(dy); 

	let x_incr = (dx / step); 
	let y_incr = (dy / step); 

	let x = x0; 
	let y = y0; 

	for (let i = 0; i < step; i++) { 
		console.log(round(x) + " " + round(y)); 
		x += x_incr; 
		y += y_incr; 
	} 
}; 

let x0 = 200, y0 = 180, x1 = 180, y1 = 160; 
DDALine(x0, y0, x1, y1); 

// Kod implementuje algorytm DDA (Digital Differential Analyzer) do generowania linii na podstawie współrzędnych dwóch punktów.

// Funkcja round(n) - zaokrąglanie wartości.
// function round(n) { 
// 	if (n - Math.floor(n) < 0.5) 
// 		return Math.floor(n); 
// 	return Math.floor(n + 1); 
// };
// Funkcja round(n) zaokrągla liczbę n do najbliższej liczby całkowitej zgodnie z klasycznymi zasadami matematyki.
// Jeśli część dziesiętna n jest mniejsza niż 0.5, zaokrągla w dół (Math.floor(n)).
// Jeśli część dziesiętna n jest większa lub równa 0.5, zaokrągla w górę (Math.floor(n + 1)).

// Funkcja DDALine(x0, y0, x1, y1) - generowanie punktów linii.
// function DDALine(x0, y0, x1, y1) { 
// 	let dx = x1 - x0; 
// 	let dy = y1 - y0; 
// dx i dy obliczają różnicę między współrzędnymi końcowymi i początkowymi linii.

// 	let step; 

// 	if (Math.abs(dx) > Math.abs(dy)) 
// 		step = Math.abs(dx); 
// 	else
// 		step = Math.abs(dy);
// step określa, ile kroków trzeba wykonać. Jest równy większej wartości między |dx| i |dy| (czyli długością linii w pikselach w poziomie lub pionie).
// To zapewnia, że linia będzie rysowana gładko, niezależnie od jej kąta.

// 	let x_incr = (dx / step); 
// 	let y_incr = (dy / step);
// x_incr i y_incr to wartości inkrementacji współrzędnych w każdym kroku.
// Jeśli linia jest bardziej pozioma, x_incr będzie większe niż y_incr.
// Jeśli linia jest bardziej pionowa, y_incr będzie większe niż x_incr.

// 	let x = x0; 
// 	let y = y0; 
// Początkowe wartości x i y ustawione na punkt początkowy (x0, y0).

// Pętla generująca punkty linii.
// 	for (let i = 0; i < step; i++) { 
// 		console.log(round(x) + " " + round(y)); 
// 		x += x_incr; 
// 		y += y_incr; 
// 	} 
// Pętla for wykonuje się step razy.
// console.log(round(x) + " " + round(y)) wypisuje współrzędne bieżącego punktu.
// Zaokrąglanie wartości x i y pozwala wyznaczyć piksele, które należy włączyć, aby linia była gładka.
// Po każdej iteracji x i y są zwiększane o x_incr i y_incr.

// Uruchomienie algorytmu.
// let x0 = 200, y0 = 180, x1 = 180, y1 = 160; 
// DDALine(x0, y0, x1, y1);
// Punkt początkowy (200, 180), końcowy (180, 160).
// Wywołanie funkcji DDALine(x0, y0, x1, y1) generuje punkty linii między tymi współrzędnymi.

// Algorytm DDA używa interpolacji liniowej, aby stopniowo przesuwać się od punktu startowego do końcowego.
// Oblicza kroki step i inkrementacje x_incr i y_incr, aby przechodzić po pikselach.
// Zaokrągla wartości x i y, aby dopasować je do rzeczywistych pikseli.
// Efektem jest poprawne wyświetlenie linii na siatce pikseli.
// Jest to podstawowy algorytm rysowania linii w grafice komputerowej, który działa bez użycia bibliotek graficznych.
