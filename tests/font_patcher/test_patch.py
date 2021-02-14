from pytest_mock import MockFixture

from font_patcher.patch import Patch


def test_p(mocker: MockFixture):
    a = mocker.patch('psMat.scale', create=True)
    a.return_value = 'scale'
    b = mocker.patch('psMat.translate', create=True)
    b.return_value = 'translate'
    c = mocker.patch('psMat.compose', create=True)
    c.return_value = 'compose'

    patch = Patch(name='name', filename='filename', sym_start=0, sym_end=0)
    assert patch.transform_matrix == 'compose'
    c.assert_called_once_with('scale', 'translate')
