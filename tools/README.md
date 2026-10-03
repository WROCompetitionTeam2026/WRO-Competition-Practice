# Herramientas del repositorio

Estas herramientas revisan las galerías y la documentación, y generan el PDF de la libreta. La verificación usa Python 3 y Git, sin paquetes adicionales. La generación del PDF utiliza ReportLab.

## Verificar el material publicado

```powershell
python tools/verify_repository.py
```

Revisa los enlaces, las fotos del carro, las capturas de los programas, las huellas de los archivos, la sintaxis de JSON/SVG/Python, los límites de tamaño y la conservación del formato de la libreta corregida.

También comprueba que los proyectos editables y las exportaciones del código del robot no formen parte de los archivos publicados. Los originales locales ignorados por Git no se incluyen en esa revisión.

La misma verificación se ejecuta en GitHub Actions. Estas comprobaciones revisan los archivos; no certifican el desempeño del carro en la pista ni todos los requisitos de WRO.

## Generar el PDF de la libreta

```powershell
python -m pip install reportlab
python tools/build_journal_pdf.py
```

Genera `Docs/Engineering-Journal.pdf` a partir de la libreta en español, con encabezados, enlaces y números de página. El documento original de Word se conserva por separado.

[Requisitos de documentación](../Docs/WRO-Documentation.md) · [Volver al inicio](../README.md)
