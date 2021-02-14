from datetime import datetime
from functools import lru_cache
from typing import TypedDict, cast

import fontforge


class SFNTNames(TypedDict):
    Copyright: str
    Family: str
    SubFamily: str
    UniqueID: str
    Fullname: str
    Version: str
    PostScriptName: str


class FiraCodeMN:

    def __init__(self, firacode: str, migu: str, *, now: datetime = datetime.now()):
        self.firacode = firacode
        self.migu = migu
        self.__now = now

        self.familyname = 'Fira Code MN'
        self.version = now.strftime('%Y.%m%d')

    @property
    def postscriptname(self):
        return f"FiraCodeMN-{self.style.replace(' ', '')}"

    @property
    def subfamily(self):
        return self.style

    @property
    def fullname(self):
        return f'{self.familyname} {self.style}'

    @property
    def uniqueid(self):
        return '; '.join([
            self.__fontforge_version(),
            self.fullname,
            self.__now.strftime('%Y%m%d'),
        ])

    @property
    def style(self):
        return self.__style.capitalize()

    def isregular(self):
        return 'Regular' in self.firacode

    def isbold(self):
        return 'Bold' in self.firacode

    @property
    def __style(self):
        if self.isregular():
            return 'regular'
        if self.isbold():
            return 'bold'
        return 'unknown'

    @property
    def copyright(self):
        firacode = self.sfnt_firacode()
        migu = self.sfnt_migu()
        return '\n'.join([
            firacode['Copyright'],
            firacode['UniqueID'],
            migu['Copyright'],
            migu['UniqueID'],
        ])

    def sfnt_firacode(self):
        return self.__sfnt_names_to_dict(self.firacode)

    def sfnt_migu(self):
        return self.__sfnt_names_to_dict(self.migu)

    @staticmethod
    @lru_cache
    def __sfnt_names_to_dict(path):
        font = fontforge.open(path)
        info = cast(SFNTNames, {k: v for (_, k, v) in font.sfnt_names})
        font.close()
        return info

    @staticmethod
    def __fontforge_version():
        return f'FontForge {fontforge.version()}'


class FiraCodeMNItalic(FiraCodeMN):

    @property
    def style(self):
        style = super().style
        if self.isregular():
            return style.replace('Regular', 'Italic')
        elif self.isbold():
            return style.replace('Bold', 'Bold Italic')
