from datetime import datetime

from pytest_mock import MockFixture

from firacode_mn import FiraCodeMN


def test_uniqueid(fontforge_version, mocker: MockFixture):
    mocker.patch('fontforge.open')

    font = FiraCodeMN('Fira - Regular', 'Migu - Regular', now=datetime(2021, 3, 9))
    assert font.uniqueid == f'FontForge {fontforge_version}; Fira Code MN Regular; 20210309'


def test_copyright(mocker: MockFixture):
    fira = mocker.Mock(sfnt_names=(('N/A', 'Copyright', 'FiraCopy'), ('N/A', 'UniqueID', 'FiraUID')))
    migu = mocker.Mock(sfnt_names=(('N/A', 'Copyright', 'MiguCopy'), ('N/A', 'UniqueID', 'MiguUID')))
    mocker.patch('fontforge.open', side_effect=[fira, migu])

    font = FiraCodeMN('Fira - Regular', 'Migu - Regular')
    assert font.copyright == '\n'.join(['FiraCopy', 'FiraUID', 'MiguCopy', 'MiguUID'])
