def generate_svg():
    svg_code = '''<?xml version="1.0" encoding="UTF-8"?>
    <svg width="500" height="300" xmlns="http://www.w3.org/2000/svg">
    
    <!-- Tło nieba -->
    <rect width="100%" height="100%" fill="lightblue" />

    <!-- Słońce -->
    <circle cx="400" cy="50" r="30" fill="yellow" stroke="orange" stroke-width="3" />

    <!-- Góry -->
    <polygon points="50,230 150,130 250,230" fill="gray" stroke="black" stroke-width="2"/>
    <polygon points="180,230 300,120 420,230" fill="darkgray" stroke="black" stroke-width="2"/>
    <polygon points="350,230 450,150 550,230" fill="dimgray" stroke="black" stroke-width="2"/>


    <!-- Chmury -->
    <ellipse cx="100" cy="50" rx="30" ry="20" fill="white" />
    <ellipse cx="130" cy="55" rx="35" ry="25" fill="white" />
    <ellipse cx="160" cy="50" rx="30" ry="20" fill="white" />

    <ellipse cx="300" cy="80" rx="30" ry="20" fill="white" />
    <ellipse cx="330" cy="85" rx="35" ry="25" fill="white" />
    <ellipse cx="360" cy="80" rx="30" ry="20" fill="white" />

    <!-- Drzewa -->
    <rect x="50" y="210" width="15" height="40" fill="saddlebrown" />
    <circle cx="57" cy="195" r="25" fill="green" />
    <circle cx="47" cy="190" r="20" fill="green" />
    <circle cx="67" cy="190" r="20" fill="green" />

    <rect x="400" y="210" width="15" height="40" fill="saddlebrown" />
    <circle cx="407" cy="195" r="25" fill="green" />
    <circle cx="397" cy="190" r="20" fill="green" />
    <circle cx="417" cy="190" r="20" fill="green" />

    <!-- Trawa -->
    <rect y="230" width="100%" height="70" fill="green" />

    </svg>'''

    file_path = "vector_art.svg"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(svg_code)

    print(f"Plik SVG został wygenerowany: {file_path}")

    # Automatyczne otwarcie pliku w przeglądarce
    import webbrowser, os
    webbrowser.open("file://" + os.path.abspath(file_path))

# 🔹 Wygenerowanie pliku SVG
generate_svg()
