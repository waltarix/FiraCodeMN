from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
from typing import DefaultDict

from .patch import Patch


@lru_cache
def group_by_filename():
    dd: DefaultDict[str, list[Patch]] = defaultdict(list)
    for patch in patch_set():
        dd[patch.filename].append(patch)
    return dd.items()


@lru_cache
def patch_set():
    return [
        Patch(
            name='Seti-UI + Custom',
            filename='original-source.otf',
            sym_start=0xE4FA,
            sym_end=0xE534,
            src_start=0xE5FA,
            exact=False,
        ),
        Patch(
            name='Devicons',
            filename='devicons.ttf',
            sym_start=0xE600,
            sym_end=0xE6C5,
            src_start=0xE700,
            exact=False,
        ),
        Patch(
            name='Powerline Symbols',
            filename='PowerlineSymbols.otf',
            sym_start=0xE0A0,
            sym_end=0xE0A2,
            src_start=None,
            exact=True,
        ),
        Patch(
            name='Powerline Symbols',
            filename='PowerlineSymbols.otf',
            sym_start=0xE0B0,
            sym_end=0xE0B3,
            src_start=None,
            exact=True,
        ),
        Patch(
            name='Powerline Extra Symbols',
            filename='PowerlineExtraSymbols.otf',
            sym_start=0xE0A3,
            sym_end=0xE0A3,
            src_start=None,
            exact=True,
        ),
        Patch(
            name='Powerline Extra Symbols',
            filename='PowerlineExtraSymbols.otf',
            sym_start=0xE0B4,
            sym_end=0xE0C8,
            src_start=None,
            exact=True,
        ),
        Patch(
            name='Powerline Extra Symbols',
            filename='PowerlineExtraSymbols.otf',
            sym_start=0xE0CA,
            sym_end=0xE0CA,
            src_start=None,
            exact=True,
        ),
        Patch(
            name='Powerline Extra Symbols',
            filename='PowerlineExtraSymbols.otf',
            sym_start=0xE0CC,
            sym_end=0xE0D4,
            src_start=None,
            exact=True,
        ),
        Patch(
            name='Pomicons',
            filename='Pomicons.otf',
            sym_start=0xE000,
            sym_end=0xE00A,
            src_start=None,
            exact=True,
        ),
        Patch(
            name='Font Awesome',
            filename='FontAwesome.otf',
            sym_start=0xF000,
            sym_end=0xF2E0,
            src_start=None,
            exact=True,
        ),
        Patch(
            name='Font Awesome Extension',
            filename='font-awesome-extension.ttf',
            sym_start=0xE000,
            sym_end=0xE0A9,
            src_start=0xE200,
            exact=False,
        ),
        Patch(
            name='Power Symbols',
            filename='Unicode_IEC_symbol_font.otf',
            sym_start=0x23FB,
            sym_end=0x23FE,
            src_start=None,
            exact=True,
        ),
        Patch(
            name='Power Symbols',
            filename='Unicode_IEC_symbol_font.otf',
            sym_start=0x2B58,
            sym_end=0x2B58,
            src_start=None,
            exact=True,
        ),
        Patch(
            name='Material',
            filename='materialdesignicons-webfont.ttf',
            sym_start=0xF001,
            sym_end=0xF847,
            src_start=0xF500,
            exact=False,
        ),
        Patch(
            name='Weather Icons',
            filename='weathericons-regular-webfont.ttf',
            sym_start=0xF000,
            sym_end=0xF0EB,
            src_start=0xE300,
            exact=False,
        ),
        Patch(
            name='Font Logos (Font Linux)',
            filename='font-logos.ttf',
            sym_start=0xF300,
            sym_end=0xF32F,
            src_start=None,
            exact=True,
        ),
        Patch(
            name='Octicons',
            filename='octicons.ttf',
            sym_start=0xF000,
            sym_end=0xF105,
            src_start=0xF400,
            exact=False,
        ),
        Patch(
            name='Octicons',
            filename='octicons.ttf',
            sym_start=0x2665,
            sym_end=0x2665,
            src_start=None,
            exact=False,
        ),
        Patch(
            name='Octicons',
            filename='octicons.ttf',
            sym_start=0x26A1,
            sym_end=0x26A1,
            src_start=None,
            exact=False,
        ),
        Patch(
            name='Octicons',
            filename='octicons.ttf',
            sym_start=0xF27C,
            sym_end=0xF27C,
            src_start=0xF4A9,
            exact=False,
        ),
        Patch(
            name='Codicons',
            filename='codicon.ttf',
            sym_start=0xEA60,
            sym_end=0xEBEB,
            src_start=None,
            exact=True,
        ),
    ]
