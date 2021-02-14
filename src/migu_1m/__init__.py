from functools import lru_cache
from os import getenv

import fontforge
import psMat

ASCENT = 1560
DESCENT = 390
OLD_EM = 1000
EM = ASCENT + DESCENT
HANKAKU_KANA = (0xFF61, 0xFF9F)

try:
    SCALE = float(getenv('MIGU1M_SCALE', '82')) / 100
except ValueError:
    SCALE = 0.82
X_TO_CENTER = EM * (1 - SCALE) / 2


def generate(source: str, output: str):
    font = fontforge.open(source)
    _set_new_em(font)
    _set_proportion(font)
    print(f'Generate {output}')
    font.generate(output)
    font.close()


def _set_new_em(font: fontforge.font):
    '''
    This sets new ascent & descent and scale glyphs.  This sets new ascent &
    descent before it sets em.  When in inverse, it does not change ascent &
    descent.
    '''
    font.selection.all()
    font.unlinkReferences()
    font.ascent = int(ASCENT / EM * OLD_EM)
    font.descent = int(DESCENT / EM * OLD_EM)
    font.em = EM


def _set_proportion(font: fontforge.font):
    scale = psMat.scale(SCALE)
    font.selection.all()
    for glyph in font.selection.byGlyphs:
        is_hankaku_kana = glyph.encoding in _hankaku_kana_codepoints()
        x_to_center = X_TO_CENTER / 2 if is_hankaku_kana else X_TO_CENTER
        trans = psMat.translate(x_to_center, 0)
        mat = psMat.compose(scale, trans)
        glyph.transform(mat)
        glyph.width = EM // 2 if is_hankaku_kana else EM


@lru_cache
def _hankaku_kana_codepoints():
    return range(min(HANKAKU_KANA), max(HANKAKU_KANA) + 1)
