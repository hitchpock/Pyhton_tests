import pytest
#from ip_validator.ip_validator import Validate
from ip_validator.ip_validator_source import Validate
from Tests.addition_func import generate_novalid_ip, preparation_predict


@pytest.fixture(scope='class')
def class_scope():
    #print("\n> Class setup")
    yield
    #print("> Class teardown")


@pytest.fixture(scope='function')
def func_scope():
    #print("   > Method setup")
    yield
    #print("\n   > Method teardown")


@pytest.mark.usefixtures('class_scope')
class TestGoodInput():
    """
    Класс, проверяющий, что функция правильно обрабатывает валидный набор данных.
    """

    def test_good_input_ipv4(self):
        """
        Метод тестирования ipv4.
        """
        input_ips = ['10.10.20.30',
                     '250.10.20.30',
                     '18.10.20.30']

        result = [['10.10.20.30', 'Valid IPv4', ],
                  ['250.10.20.30', 'Valid IPv4'], ['18.10.20.30', 'Valid IPv4']]

        assert Validate().validateIPAddress(input_ips) == result

    def test_good_input_ipv6(self):
        """
        Метод тестирования ipv6.
        """
        input_ips = ['2001:0DB8:3C4D:7777:0260:3EFF:FE15:9501',
                     '2001:0db8:11a3:09d7:1f34:8a2e:07a0:765d',
                     '1234:5678:90AB:CDEF:abcd:ef12:3456:7890']

        result = [['2001:0DB8:3C4D:7777:0260:3EFF:FE15:9501', 'Valid IPv6'],
                  ['2001:0db8:11a3:09d7:1f34:8a2e:07a0:765d', 'Valid IPv6'],
                  ['1234:5678:90AB:CDEF:abcd:ef12:3456:7890', 'Valid IPv6']]

        assert Validate().validateIPAddress(input_ips) == result


@pytest.mark.usefixtures('class_scope')
class TestBadInput():
    """
    Класс, проверяющий, что функция правльно обрабатывает невалидный набор данных.
    Проверяем, что обрабатываются все части ip адреса и отлавливаются ненужные символы.
    """

    ipv4 = '10.20.30.40'
    bad_ipv4 = []
    for x in '!@#$%^&*;()_-+=<>?,/\\|~`qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
        bad_ipv4 += generate_novalid_ip(ipv4, '.', symbol=x)

    ipv6 = '2001:0DB8:3C4D:7777:0260:3EFF:FE15:9501'
    bad_ipv6 = []
    for x in '!@#$%^&*;()_-+=<>?,/\\|~`qwrtyuiopshjklzxvnmgGQWRTYUIOPSHJKLZXVNM':
        bad_ipv6 += generate_novalid_ip(ipv6, ':', symbol=x)

    def test_bad_input_ipv4(self):
        """
        Метод тестирования ipv4. Проверяем, что Validator не пропускает никаких символов в ipv4.
        """
        input_ips = self.bad_ipv4
        result = preparation_predict(input_ips, 'Wrong IPv4')

        assert Validate().validateIPAddress(input_ips) == result

    @pytest.mark.xfail
    def test_bad_input_ipv6(self):
        """
        Метод тестирования ipv6. Проверяем, что Validator не пропускает никаких символов в ipv6.
        """
        input_ips = self.bad_ipv6
        result = preparation_predict(input_ips, 'Wrong IPv6')

        assert Validate().validateIPAddress(input_ips) == result


@pytest.mark.usefixtures('class_scope')
class TestExtremePoint():
    """
    Класс проверки крайних значений.
    """

    @pytest.mark.xfail
    def test_extreme_point_ipv4(self):
        """
        Метод проверки ipv4. Проверяем, учтины ли крйние значения входных данных.
        """
        input_ips = ['10.20.30.-1',
                     '10.20.30.0',
                     '10.20.30.255',
                     '10.20.30.256']

        result = [['10.20.30.-1', 'Wrong IPv4'],
                  ['10.20.30.0', 'Valid IPv4'],
                  ['10.20.30.255', 'Valid IPv4'],
                  ['10.20.30.256', 'Wrong IPv4']]

        assert Validate().validateIPAddress(input_ips) == result

    @pytest.mark.xfail
    def test_extreme_point_ipv6(self):
        """
        Метод проверки ipv6 в верхнем регистре. Проверяем, учтины ли крйние значения входных данных.
        """

        input_ips = ['0:0:0:0:0:0:0:0',
                     '0:0:0:0:0:0:0:1',
                     'FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF']

        input_ips_lower = [x.lower() for x in input_ips]

        result = [['0:0:0:0:0:0:0:0', 'Valid IPv6'],
                  ['0:0:0:0:0:0:0:1', 'Valid IPv6'],
                  ['FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF', 'Valid IPv6']]

        assert Validate().validateIPAddress(input_ips) == result

    def test_extreme_point_ipv6_lower(self):
        """
        Метод проверки ipv6 в нижнем регистре.
        """

        input_ips = ['ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff']

        result = [['ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'Valid IPv6']]

        assert Validate().validateIPAddress(input_ips) == result


@pytest.mark.usefixtures('class_scope')
class TestNotation():
    """
    Класс проверки ввода ip адреса в сокращенной нотации.
    """

    def test_zero_ipv6(self):
        """
        Метод тестирования функции на ввод ip адреса без ведущих нулей.
        """

        input_ips = ['2001:DB8:3C4D:777:0260:EFF:FE15:9501',
                     '2001:0db8:a3:09d7:1f34:e:07a0:765d']

        result = preparation_predict(input_ips, 'Valid IPv6')

        assert Validate().validateIPAddress(input_ips) == result

    @pytest.mark.xfail
    def test_short_ipv6(self):
        """
        Метод тестирования функции на ввод ipv6 в сокращенной нотации, с удаленными нулевыми хекстетами.
        """

        input_ips = ['2001:DB8::EFF:FE15:9501',
                     '2001::d1:0']
        
        result = preparation_predict(input_ips, 'Valid IPv6')
        
        assert Validate().validateIPAddress(input_ips) == result
