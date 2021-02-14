from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .patch import Patch

import fontforge

from . import patch_set


def generate(source: str, output: str):
    font = fontforge.open(source)
    _patch(font)
    print(f'Generated {output}')
    font.generate(output)
    font.close()


def _patch(font: fontforge.font):
    for filename, patches in patch_set.group_by_filename():
        symfont = fontforge.open(f'src/assets/glyphs/{filename}')

        for patch in patches:
            _copy_glyphs(font, symfont, patch)

        symfont.close()


def _copy_glyphs(font: fontforge.font, symfont: fontforge.font, patch: Patch):
    symfont.em = font.em
    index = patch.src_start or 0
    symfont.selection.select(('ranges', 'unicode'), patch.sym_start, patch.sym_end)
    for glyph in list(symfont.selection.byGlyphs):
        src_encoding = glyph.encoding
        if patch.src_start:
            if patch.exact:
                src_encoding = patch.src_start + (glyph.encoding - patch.sym_start)
            else:
                src_encoding = index
                index += 1
        symfont.selection.select(glyph.encoding)
        symfont.transform(patch.transform_matrix)
        symfont.copy()
        font.selection.select(src_encoding)
        font.paste()
