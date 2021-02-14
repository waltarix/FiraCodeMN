import pytest

from font_patcher.patch_set import patch_set


@pytest.mark.parametrize(
    'function_name', [
        'is_setiui',
        'is_devicons',
        'is_powerline',
        'is_pomicons',
        'is_fontawesome_extension',
        'is_fontlogos',
        'is_powersymbols',
        'is_octicons',
        'is_material',
        'is_weathericons',
        'is_codicons',
    ]
)
def test_bar(function_name):
    assert any(map(lambda p: p.__getattribute__(function_name)(), patch_set()))
