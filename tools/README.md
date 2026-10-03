# Repository tools

These Python 3 tools inspect documentation and export original source. They do not change the robot's control logic. Source export and verification need no third-party dependencies; optional PDF generation uses ReportLab.

## Export a SPIKE project

```powershell
python tools/export_spike.py "Code/SPIKE Prime/ACTU-04-September/Version-08/program.llsp3"
```

Exports the original Word Blocks graph and a readable stack listing, or the original Python when the container stores Python. Also exports original project metadata.

## Verify the repository

```powershell
python tools/verify_repository.py
```

Checks local documentation links, the six vehicle photographs, original-file SHA-256 hashes, SPIKE archive integrity, source-export fidelity, JSON/SVG/Python syntax, normal GitHub file-size limits and preservation of the Word notebook's formatting/package parts.

The same verification runs in GitHub Actions. Passing it means the material is internally consistent; it does not mean the vehicle has passed physical track tests or all WRO submission requirements.

## Rebuild the printable journal

```powershell
python -m pip install reportlab
python tools/build_journal_pdf.py
```

Creates `Docs/Engineering-Journal.pdf` from the English Markdown journal, with page numbers and online source links. The Word source remains a separate original document.

[Documentation guide](../Docs/WRO-Documentation.md) · [Repository home](../README.md)
