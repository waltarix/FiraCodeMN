import fontforge

from .font_info import FiraCodeMN

ITALIC_ANGLE = -10
ASCENT = 1560
DESCENT = 390
ENCODING = 'UnicodeFull'
UNDERLINE_POS = -250
UNDERLINE_HEIGHT = 100
WIDTH = ASCENT + DESCENT
STYLE_PROPERTY = {
    'Regular': {
        'weight': 'Book',
        'os2_weight': 400,
        'panose_weight': 5,
        'panose_letterform': 2,
    },
    'Bold': {
        'weight': 'Bold',
        'os2_weight': 700,
        'panose_weight': 8,
        'panose_letterform': 2,
    },
    'Italic': {
        'weight': 'Book',
        'os2_weight': 400,
        'panose_weight': 5,
        'panose_letterform': 9,
    },
    'Bold Italic': {
        'weight': 'Bold',
        'os2_weight': 700,
        'panose_weight': 8,
        'panose_letterform': 9,
    },
}


def generate(firacode: str, migu: str, output: str):
    font = _new_font(firacode, migu)
    _merge(font, firacode, migu)
    font.selection.all()
    font.removeOverlap()
    font.autoHint()
    font.autoInstr()
    print(f'Generate {output}')
    font.generate(output)
    font.close()


def _new_font(firacode: str, migu: str):
    font_info = FiraCodeMN(firacode, migu)
    # TODO: classify
    prop = STYLE_PROPERTY[font_info.style]

    font = fontforge.font()
    font.ascent = ASCENT
    font.descent = DESCENT
    font.italicangle = ITALIC_ANGLE
    font.upos = UNDERLINE_POS
    font.uwidth = UNDERLINE_HEIGHT
    font.familyname = font_info.familyname
    font.copyright = font_info.copyright
    font.encoding = ENCODING
    font.fontname = font_info.postscriptname
    font.fullname = font_info.fullname
    font.version = font_info.version
    font.appendSFNTName('English (US)', 'SubFamily', font_info.subfamily)
    font.appendSFNTName('English (US)', 'UniqueID', font_info.uniqueid)
    font.weight = prop['weight']
    font.os2_weight = prop['os2_weight']
    font.os2_width = 5  # Medium (w/h = 1.000)
    font.os2_fstype = 4  # Printable Document (suitable for SF Mono)
    font.os2_vendor = 'N/A'
    font.os2_family_class = 2057  # SS Typewriter Gothic
    font.os2_panose = (
        2,  # Latin: Text and Display
        11,  # Nomal Sans
        prop['panose_weight'],
        9,  # Monospaced
        2,  # None
        2,  # No Variation
        3,  # Straight Arms/Wedge
        prop['panose_letterform'],
        2,  # Standard/Trimmed
        7,  # Ducking/Large
    )
    # winascent & windescent is for setting the line height for Windows.
    font.os2_winascent = ASCENT
    font.os2_windescent = DESCENT
    # the `_add` version is for setting offsets.
    font.os2_winascent_add = 0
    font.os2_windescent_add = 0
    # hhea_ascent, hhea_descent is the macOS version for winascent &
    # windescent.
    font.hhea_ascent = ASCENT
    font.hhea_descent = -DESCENT
    font.hhea_ascent_add = 0
    font.hhea_descent_add = 0
    # typoascent, typodescent is generic version for above.
    font.os2_typoascent = ASCENT
    font.os2_typodescent = -DESCENT
    font.os2_typoascent_add = 0
    font.os2_typodescent_add = 0
    # linegap is for gap between lines.  The `hhea_` version is for macOS.
    font.os2_typolinegap = 0
    font.hhea_linegap = 0
    return font


def _merge(font: fontforge.font, firacode: str, migu: str):
    font.mergeFonts(firacode)
    font.mergeFonts(migu)
