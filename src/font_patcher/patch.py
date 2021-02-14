from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import psMat


@dataclass
class Patch:
    name: str
    filename: str
    sym_start: int
    sym_end: int
    src_start: Optional[int] = None
    exact: bool = True

    def is_setiui(self):
        return self.name.startswith('Seti-UI')

    def is_devicons(self):
        return self.name == 'Devicons'

    def is_powerline(self):
        return self.name.startswith('Powerline')

    def is_pomicons(self):
        return self.name == 'Pomicons'

    def is_fontawesome_extension(self):
        return self.name == 'Font Awesome Extension'

    def is_fontlogos(self):
        return self.name == 'Font Logos (Font Linux)'

    def is_powersymbols(self):
        return self.name == 'Power Symbols'

    def is_octicons(self):
        return self.name == 'Octicons'

    def is_material(self):
        return self.name == 'Material'

    def is_weathericons(self):
        return self.name == 'Weather Icons'

    def is_codicons(self):
        return self.name == 'Codicons'

    @property
    def transform_matrix(self):
        x_ratio = 1.0
        y_ratio = 1.0
        x_diff = 0
        y_diff = 0

        if self.is_setiui():
            x_ratio = 1.1
            y_ratio = 1.1
            x_diff = -100
            y_diff = -450

        elif self.is_devicons():
            x_ratio = 1.05
            y_ratio = 1.05
            x_diff = -100
            y_diff = -250

        elif self.is_powerline():
            x_ratio = 0.95
            y_ratio = 0.88
            x_diff = 0
            y_diff = -30

        elif self.is_fontlogos():
            y_diff = -120

        elif self.is_fontawesome_extension():
            y_diff = -400

        elif self.is_pomicons():
            x_ratio = 1.2
            y_ratio = 1.2
            x_diff = -200
            y_diff = -300

        elif self.is_octicons():
            x_ratio = 0.95
            y_ratio = 0.95
            x_diff = 30
            y_diff = -100

        elif self.is_material():
            x_ratio = 1.1
            y_ratio = 1.1
            x_diff = -50
            y_diff = -250

        elif self.is_codicons():
            x_ratio = 0.9
            y_ratio = 0.9
            x_diff = 100
            y_diff = -400

        scale = psMat.scale(x_ratio, y_ratio)
        translate = psMat.translate(x_diff, y_diff)
        return psMat.compose(scale, translate)
