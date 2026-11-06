from PIL import Image, ImageDraw, ImageFont
import os

FONTS_DIR = r"C:/Users/petra/.opencode/skills/canvas-design/canvas-fonts"

# Lienzo cuadrado (Instagram / redes)
W, H = 1080, 1080
img = Image.new("RGB", (W, H), "#EFE7D6")  # crema cálido
draw = ImageDraw.Draw(img)

# Paleta
CREAM   = "#EFE7D6"
INK     = "#1A1A1A"
RULE    = "#1A1A1A"
ACCENT  = "#A8332B"   # carmín sobrio
MUTED   = "#6E665A"

def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS_DIR, name), size)

# Tipografías
f_display = font("YoungSerif-Regular.ttf", 220)      # display serif elegante
f_display_sm = font("YoungSerif-Regular.ttf", 86)    # subtítulo
f_sans = font("WorkSans-Regular.ttf", 22)            # etiquetas pequeñas
f_sans_b = font("WorkSans-Bold.ttf", 22)
f_mono = font("JetBrainsMono-Regular.ttf", 20)
f_mono_b = font("JetBrainsMono-Bold.ttf", 20)
f_label = font("InstrumentSans-Bold.ttf", 16)

# Marco: una hoja flotando — pequeña rotación implícita vía esquinas asimétricas
# Líneas finas decorativas que sugieren el borde de un documento
MARGIN_L = 110
MARGIN_R = 110
TOP_Y = 150

# --- Encabezado técnico (esquina superior izquierda) ---
draw.text((MARGIN_L, 70), "N.º 001", font=f_label, fill=MUTED)
draw.text((MARGIN_L, 92), "EDICIÓN PÚBLICA", font=f_label, fill=MUTED)

# Esquina superior derecha: clasificación
draw.text((W - MARGIN_R - 230, 70),  "HERRAMIENTA", font=f_label, fill=MUTED)
draw.text((W - MARGIN_R - 230, 92),  "EN EL NAVEGADOR", font=f_label, fill=MUTED)

# --- Línea separadora superior ---
draw.line([(MARGIN_L, 130), (W - MARGIN_R, 130)], fill=RULE, width=1)

# --- Bloque display ---
# Línea 1: "PDF"
draw.text((MARGIN_L, TOP_Y + 30), "PDF", font=f_display, fill=INK)
# Línea 2: "Studio" en cursiva-display (usamos serif regular, queda elegante)
draw.text((MARGIN_L, TOP_Y + 270), "Studio", font=f_display_sm, fill=INK)

# Acento rojo: palabra clave
# Colocada como un sello pequeño a la derecha del bloque display
draw.text((MARGIN_L + 540, TOP_Y + 305), "Editor", font=font("YoungSerif-Regular.ttf", 56), fill=ACCENT)

# --- Línea separadora media ---
draw.line([(MARGIN_L, TOP_Y + 410), (W - MARGIN_R, TOP_Y + 410)], fill=RULE, width=1)

# --- Cuerpo: tres "filas" técnicas tipo ficha de producto ---
Y0 = TOP_Y + 445
ROW_H = 70
rows = [
    ("FUNCION",    "Editar, unir, rotar páginas"),
    ("ANOTAR",     "Texto, firma dibujada o desde imagen"),
    ("FORMULARIOS","AcroForm — texto, checks, radios"),
    ("EXPORTAR",   "PDF  ·  DOCX"),
]
for i, (k, v) in enumerate(rows):
    y = Y0 + i * ROW_H
    # etiqueta a la izquierda
    draw.text((MARGIN_L, y + 6), k, font=f_label, fill=INK)
    # valor a la derecha
    draw.text((MARGIN_L + 240, y + 4), v, font=f_sans, fill=INK)
    # separador de fila
    if i < len(rows) - 1:
        draw.line([(MARGIN_L, y + 56), (W - MARGIN_R, y + 56)], fill="#C8BFAE", width=1)

# --- Línea separadora inferior ---
BOTTOM_RULE_Y = Y0 + len(rows) * ROW_H + 24
draw.line([(MARGIN_L, BOTTOM_RULE_Y), (W - MARGIN_R, BOTTOM_RULE_Y)], fill=RULE, width=1)

# --- Pie: precio + URL ---
FOOT_Y = BOTTOM_RULE_Y + 28
# Precio — destacado
draw.text((MARGIN_L, FOOT_Y), "GRATIS", font=font("WorkSans-Bold.ttf", 38), fill=ACCENT)
# Pequeña aclaración
draw.text((MARGIN_L + 145, FOOT_Y + 14), "100 % local · sin servidor", font=f_sans, fill=MUTED)

# URL — ancla tipográfica derecha
url_text = "pdfstudio.local"
bbox = draw.textbbox((0, 0), url_text, font=f_mono_b)
url_w = bbox[2] - bbox[0]
draw.text((W - MARGIN_R - url_w, FOOT_Y + 8), url_text, font=f_mono_b, fill=INK)

# --- Sello/marca inferior (esquina) ---
draw.text((MARGIN_L, H - 80), "▮  PDF STUDIO", font=f_label, fill=INK)
draw.text((W - MARGIN_R - 140, H - 80), "↗  ABRIR", font=f_label, fill=INK)

out = r"C:\Users\petra\agenteX\pdf-editor\ad-social.png"
img.save(out, "PNG", optimize=True)
print("ok", out)