from typing import Tuple

import fontforge
import psMat

from firacode_mn.font_info import FiraCodeMNItalic


def generate(source: str, output: str):
    font = fontforge.open(source)
    _rename(source, font)
    _transform(font)
    font.generate(output)
    font.close()


# TODO: correct name
def _xrename(firacode: FiraCodeMNItalic, sfnt_name: Tuple[str, str, str]):
    (lang, name, value) = sfnt_name
    if name in ('SubFamily', 'UniqueID', 'Fullname', 'PostScriptName'):
        value = firacode.__getattribute__(name.lower())
    return (lang, name, value)


def _rename(firacode_mn_italic: str, font: fontforge.font):
    firacode = FiraCodeMNItalic(firacode_mn_italic, '')
    font.sfnt_names = tuple(_xrename(firacode, sfnt_name) for sfnt_name in font.sfnt_names)


def _transform(font: fontforge.font):
    font.selection.all()
    font.transform(psMat.skew(0.2))
    font.removeOverlap()
