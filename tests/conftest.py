import sys
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

if TYPE_CHECKING:
    import fontforge as Tfontforge
    import psMat as TpsMat

FONTFORGE_VERSION = '20201107'


@pytest.fixture
def fontforge_version():
    return FONTFORGE_VERSION


def mocked_fontforge():
    fontforge: Tfontforge = MagicMock()  # type: ignore
    fontforge.version.return_value = FONTFORGE_VERSION
    return fontforge


def mocked_psmat():
    psMat: TpsMat = MagicMock()  # type: ignore
    return psMat


sys.modules['fontforge'] = mocked_fontforge()
sys.modules['psMat'] = mocked_psmat()
