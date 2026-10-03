"""Create the printable journal from Docs/Engineering-Journal.md.

Optional dependency: python -m pip install reportlab
Run from the repository root: python tools/build_journal_pdf.py
"""
from pathlib import Path
import html
import re
from urllib.parse import quote, unquote

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'Docs/Engineering-Journal.md'
OUTPUT = ROOT / 'Docs/Engineering-Journal.pdf'
styles = getSampleStyleSheet()
styles.add(ParagraphStyle('BodyERA', fontName='Helvetica', fontSize=10.2, leading=15, textColor=colors.HexColor('#263747'), spaceAfter=9))
styles.add(ParagraphStyle('TitleERA', fontName='Helvetica-Bold', fontSize=29, leading=34, textColor=colors.HexColor('#0b1728'), spaceAfter=12))
styles.add(ParagraphStyle('ChapterERA', fontName='Helvetica-Bold', fontSize=17, leading=23, textColor=colors.HexColor('#0e7490'), spaceBefore=18, spaceAfter=11, keepWithNext=True))
styles.add(ParagraphStyle('EntryERA', fontName='Helvetica-Bold', fontSize=11.5, leading=16, textColor=colors.HexColor('#0b1728'), spaceBefore=9, spaceAfter=5, keepWithNext=True))
styles.add(ParagraphStyle('CellERA', parent=styles['BodyERA'], fontSize=9, leading=13, spaceAfter=0))

def inline(text):
    text = text.replace('−', '-').replace('→', 'to')
    text = html.escape(text)
    def link(match):
        label, path = match.groups()
        if path.startswith('http'):
            url = path
        else:
            resolved = (SOURCE.parent / unquote(path)).resolve().relative_to(ROOT).as_posix()
            url = 'https://github.com/WROCompetitionTeam2026/WRO-Competition-Practice/blob/main/' + quote(resolved)
        return f'<link href="{html.escape(url, quote=True)}" color="#0e7490">{label}</link>'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    text = re.sub(r'`([^`]+)`', r'<font name="Courier">\1</font>', text)
    return text

story = []
lines = SOURCE.read_text(encoding='utf-8').splitlines()
index = 0
while index < len(lines):
    line = lines[index].strip()
    if not line:
        index += 1
        continue
    if line.startswith('|'):
        rows = []
        while index < len(lines) and lines[index].strip().startswith('|'):
            row = [v.strip() for v in lines[index].strip().strip('|').split('|')]
            if not all(re.fullmatch(r'[-: ]+', v) for v in row):
                rows.append([Paragraph(inline(v), styles['CellERA']) for v in row])
            index += 1
        table = Table(rows, colWidths=[195, 300], repeatRows=1, hAlign='LEFT')
        table.setStyle(TableStyle([('BACKGROUND', (0,0),(-1,0),colors.HexColor('#e0f2fe')),
                                   ('VALIGN',(0,0),(-1,-1),'TOP'),
                                   ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, colors.HexColor('#f1f5f9')]),
                                   ('BOTTOMPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),9),
                                   ('LINEBELOW',(0,0),(-1,0),1,colors.HexColor('#0891b2'))]))
        story.extend([table, Spacer(1, 12)])
        continue
    if line.startswith('# '):
        story.append(Paragraph(inline(line[2:]), styles['TitleERA']))
    elif line.startswith('## '):
        story.append(Paragraph(inline(line[3:]), styles['ChapterERA']))
    elif line.startswith('### '):
        story.append(Paragraph(inline(line[4:]), styles['EntryERA']))
    elif line.startswith('- '):
        story.append(Paragraph(inline(line[2:]), styles['BodyERA'], bulletText='•'))
    else:
        parts = [line]
        while index+1 < len(lines) and lines[index+1].strip() and not lines[index+1].startswith(('#','|','- ')):
            index += 1
            parts.append(lines[index].strip())
        story.append(Paragraph(inline(' '.join(parts)), styles['BodyERA']))
    index += 1

def page(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(colors.HexColor('#0b1728'))
    canvas.rect(0, height-48, width, 48, fill=1, stroke=0)
    canvas.setFont('Helvetica-Bold', 10)
    canvas.setFillColor(colors.white)
    canvas.drawString(48, height-29, 'ERA  /  LOS 3 MOSQUETEROS')
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.HexColor('#67e8f9'))
    canvas.drawRightString(width-48, height-29, 'WRO FUTURE ENGINEERS 2026')
    canvas.setStrokeColor(colors.HexColor('#0891b2'))
    canvas.line(48, 42, width-48, 42)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor('#64748b'))
    canvas.drawString(48, 28, 'English presentation of the existing team notebook · 2 October 2026')
    canvas.drawRightString(width-48, 28, str(doc.page))
    canvas.restoreState()

document = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=50, leftMargin=50,
                             topMargin=72, bottomMargin=60, title='ERA — Engineering Journal',
                             author='Los 3 Mosqueteros', subject='English presentation of the supplied engineering notebook')
document.build(story, onFirstPage=page, onLaterPages=page)
print('Generated:', OUTPUT, OUTPUT.stat().st_size, 'bytes')
