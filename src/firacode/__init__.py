import fontforge
from psMat import scale

OLD_WIDTH = 1200
WIDTH = 975
SCALE_DOWN = float(WIDTH) / OLD_WIDTH

# TODO: use migu's glyph
MIGUMIGU = [
    (0x2026, ),  # '…' HORIZONTAL ELLIPSIS (Other_Punctuation)
    (0x2190, 0x2199),  # '←'..'↙' ARROWS (Math_Symbol, Other_Symbol)
    (0x25B2, ),  # '▲' BLACK UP-POINTING TRIANGLE (Other_Symbol)
    (0x25BC, ),  # '▼' BLACK DOWN-POINTING TRIANGLE (Other_Symbol)
    (0x25C6, 0x25C7),  # '◆'..'◇' BLACK|WHITE DIAMOND (Other_Symbol)
    (0x25CB, ),  # '○'  WHITE CIRCLE (Other_Symbol)
    (0x25CE, 0x25CF),  # '◎'..'●' BULLSEYE, BLACK CIRCLE (Other_Symbol)
    (0x25EF, ),  # '◯' LARGE CIRCLE (Other_Symbol)
]


def generate(source: str, output: str):
    font = fontforge.open(source)
    _remove_some_glyphs(font)
    _scale_glyphs(font)
    print(f'Generate {output}')
    font.generate(output)
    font.close()


def _scale_glyphs(font: fontforge.font):
    mat = scale(SCALE_DOWN)
    font.selection.all()
    for glyph in font.selection.byGlyphs:
        glyph.transform(mat)
        glyph.width = WIDTH


def _remove_some_glyphs(font: fontforge.font):
    for codepoints in MIGUMIGU:
        font.selection.select(('ranges', 'unicode'), min(codepoints), max(codepoints))
        font.clear()
