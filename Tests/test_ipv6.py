import pytest
from ip_validator.ip_validator import Validate


def test_good_input():
    """
    Функция проверки на валидном наборе данных.
    Проверяем что обрабатываются все части ip адреса.
    """
    input_ips = [
        '2001:0DB8:3C4D:7777:0260:3EFF:FE15:9501',
        '2001:0db8:11a3:09d7:1f34:8a2e:07a0:765d',
        '21DA:00D3:0000:2F3B:02AA:00FF:FE28:9C5A'
    ]

    result = [['2001:0DB8:3C4D:7777:0260:3EFF:FE15:9501', 'Valid IPv6'],
              ['2001:0db8:11a3:09d7:1f34:8a2e:07a0:765d', 'Valid IPv6'],
              ['21DA:00D3:0000:2F3B:02AA:00FF:FE28:9C5A', 'Valid IPv6']]

    assert Validate().validateIPAddress(input_ips) == result


def test_bad_input():
    """
    Функция проверки невалидных входных данных.
    Проверяем, что обрабаотываются все части ip адреса
    """
    input_ips = [
        '-2001:0DB8:3C4D:7777:0260:3EFF:FE15:9501',
        '2001:-0DB8:3C4D:7777:0260:3EFF:FE15:9501',
        '2001:0DB8:-3C4D:7777:0260:3EFF:FE15:9501',
        '2001:0DB8:3C4D:-7777:0260:3EFF:FE15:9501',
        '2001:0DB8:3C4D:7777:-0260:3EFF:FE15:9501',
        '2001:0DB8:3C4D:7777:0260:-3EFF:FE15:9501',
        '2001:0DB8:3C4D:7777:0260:3EFF:-FE15:9501',
        '2001:0DB8:3C4D:7777:0260:3EFF:FE15:-9501',
    ]

    result = [['-2001:0DB8:3C4D:7777:0260:3EFF:FE15:9501', 'Wrong IPv6'],
              ['2001:-0DB8:3C4D:7777:0260:3EFF:FE15:9501', 'Wrong IPv6'],
              ['2001:0DB8:-3C4D:7777:0260:3EFF:FE15:9501', 'Wrong IPv6'],
              ['2001:0DB8:3C4D:-7777:0260:3EFF:FE15:9501', 'Wrong IPv6'],
              ['2001:0DB8:3C4D:7777:-0260:3EFF:FE15:9501', 'Wrong IPv6'],
              ['2001:0DB8:3C4D:7777:0260:-3EFF:FE15:9501', 'Wrong IPv6'],
              ['2001:0DB8:3C4D:7777:0260:3EFF:-FE15:9501', 'Wrong IPv6'],
              ['2001:0DB8:3C4D:7777:0260:3EFF:FE15:-9501', 'Wrong IPv6']]

    assert Validate().validateIPAddress(input_ips) == result
