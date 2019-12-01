import pytest
from ip_validator.ip_validator import Validate


@pytest.fixture(scope='session', autouse=True)
def suite_data():
    print("\n> Suite setup")
    yield
    print("> Suite teardown")


@pytest.fixture(scope='function', autouse=True)
def case_data():
    print("   > Case setup")
    yield
    print("\n   > Case teardown")


def test_good_input():
    """
    Функция проверки на валидном наборе данных.
    """
    input_ips = [
        '10.10.20.30',
        '254.10.20.30',
        '18.10.20.30'
    ]
    result = [['10.10.20.30', 'Valid IPv4', ],
              ['254.10.20.30', 'Valid IPv4'], ['18.10.20.30', 'Valid IPv4']]

    assert Validate().validateIPAddress(input_ips) == result


def test_bad_input():
    """
    Функция проверки невалидных входных данных.
    """
    input_ips = [
        '-10.10.20.30',
        '10.-10.20.30',
        '10.10.-20.30',
        '10.10.20.-30',
    ]
    result = [['-10.10.20.30', 'Wrong IPv4', ], ['10.-10.20.30', 'Wrong IPv4'],
              ['10.10.-20.30', 'Wrong IPv4'], ['10.10.20.-30', 'Wrong IPv4']]

    assert Validate().validateIPAddress(input_ips) == result
