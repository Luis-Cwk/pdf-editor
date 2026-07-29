# PDF Studio Editor

Editor de PDFs que corre 100% en el navegador (sin servidor). Permite:

- Cargar uno o varios PDFs e insertarlos en cualquier posicion.
- Insertar imagenes (PNG/JPG) convertidas a paginas PDF.
- Reordenar, eliminar y rotar paginas (90 / -90 grados).
- Combinar dos paginas seleccionadas en una sola (horizontal o vertical).
- Vista previa con zoom, ajuste a pantalla y Ctrl+rueda.
- Anotaciones en pagina: texto con tamano y color, y firma dibujada o desde imagen.
- Deshacer anotaciones (Ctrl+Z dentro de la vista previa).
- Llenar campos AcroForm (texto, checkbox, dropdown, option list, radio group) y opcionalmente aplanarlos.
- Exportar a PDF (incluyendo firmas y valores de formulario aplicados).
- Exportar a DOCX (renderizando cada pagina como imagen con layout fiel).

## Stack

HTML estatico + CSS + JavaScript. Usa las siguientes librerias cargadas desde CDN:

- [PDF.js](https://mozilla.github.io/pdf.js/) para lectura y render.
- [pdf-lib](https://github.com/Hopding/pdf-lib) para edicion, merge, formularios y exportacion.
- [docx](https://docx.js.org/) para exportacion a Word.

## Uso local

Como es HTML estatico, basta con servir la carpeta:

```bash
python -m http.server 8000
```

Y abrir `http://localhost:8000`.

## Despliegue

El proyecto esta pensado para desplegarse como sitio estatico (Vercel, Netlify, GitHub Pages, etc.).
No requiere build step.