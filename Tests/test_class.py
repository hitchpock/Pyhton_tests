import pytest
# from ip_validator.ip_validator import Validate
from ip_validator.ip_validator_source import Validate
from Tests.addition_func import generate_novalid_ip, preparation_predict


@pytest.fixture(scope='class')
def class_scope():
    yield


testdata_ipv4 = ['10.20.30.40',
                 '250.10.20.30',
                 '18.10.20.30']

testdata_ipv6 = ['2001:0DB8:3C4D:7777:0260:3EFF:FE15:9501',
                 '2001:0db8:11a3:09d7:1f34:8a2e:07a0:765d',
                 '1234:5678:90AB:CDEF:abcd:ef12:3456:7890']


@pytest.mark.usefixtures('class_scope')
class TestGoodInput():
    """
    Класс, проверяющий, что функция правильно обрабатывает валидный набор данных.
    """

    @pytest.mark.parametrize('input_ips', [testdata_ipv4])
    def test_good_input_ipv4(self, input_ips):
        """
        Метод тестирования ipv4.
        """

        result = preparation_predict(input_ips, 'Valid IPv4')

        assert Validate().validateIPAddress(input_ips) == result

    @pytest.mark.parametrize('input_ips', [testdata_ipv6])
    def test_good_input_ipv6(self, input_ips):
        """
        Метод тестирования ipv6.
        """

        result = preparation_predict(input_ips, 'Valid IPv6')

        assert Validate().validateIPAddress(input_ips) == result


@pytest.mark.usefixtures('class_scope')
class TestBadInput():
    """
    Класс, проверяющий, что функция правльно обрабатывает невалидный набор данных.
    Проверяем, что обрабатываются все части ip адреса и отлавливаются ненужные символы.
    """

    ipv4 = testdata_ipv4[0]
    bad_ipv4 = []
    for x in '!@#$%^&*;()_-+=<>?,/\\|~`qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
        bad_ipv4 += generate_novalid_ip(ipv4, '.', symbol=x)

    ipv6 = testdata_ipv6[0]
    bad_ipv6 = []
    for x in '!@#$%^&*;()_-+=<>?,/\\|~`qwrtyuiopshjklzxvnmgGQWRTYUIOPSHJKLZXVNM':
        bad_ipv6 += generate_novalid_ip(ipv6, ':', symbol=x)

    def test_bad_input_ipv4(self):
        """
        Метод тестирования ipv4. Проверяем, что Validator не пропускает никаких символов в ipv4.
        """

        result = preparation_predict(self.bad_ipv4, 'Wrong IPv4')

        assert Validate().validateIPAddress(self.bad_ipv4) == result

    @pytest.mark.xfail
    def test_bad_input_ipv6(self):
        """
        Метод тестирования ipv6. Проверяем, что Validator не пропускает никаких символов в ipv6.
        """

        result = preparation_predict(self.bad_ipv6, 'Wrong IPv6')

        assert Validate().validateIPAddress(self.bad_ipv6) == result


@pytest.mark.usefixtures('class_scope')
class TestExtremePoint():
    """
    Класс проверки крайних значений.
    """

    testdata_good_ipv4 = ['10.20.30.0',
                          '10.20.30.255']

    testdata_bad_ipv4 = ['10.20.30.-1',
                         '10.20.30.256']

    testdata_good_ipv6 = ['0:0:0:0:0:0:0:0',
                          '0:0:0:0:0:0:0:1',
                          'FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF']

    @pytest.mark.parametrize('input_ips_good,input_ips_bad',
                             [testdata_good_ipv4, testdata_bad_ipv4])
    @pytest.mark.xfail
    def test_extreme_point_ipv4(self, input_ips_good, input_ips_bad):
        """
        Метод проверки ipv4. Проверяем, учтины ли крйние значения входных данных.
        """

        result_good = preparation_predict(input_ips_good, 'Valid IPv4')
        result_bad = preparation_predict(input_ips_bad, 'Wrong IPv4')

        assert Validate().validateIPAddress(input_ips_good) == result_good
        assert Validate().validateIPAddress(input_ips_bad) == result_bad

    @pytest.mark.parametrize('input_ips', [testdata_good_ipv6])
    @pytest.mark.xfail
    def test_extreme_point_ipv6(self, input_ips):
        """
        Метод проверки ipv6 в верхнем регистре. Проверяем, учтины ли крйние значения входных данных.
        """

        result = preparation_predict(input_ips, 'Valid IPv6')

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

        input_ips = ['2001:DB8::EFF:FE15:9501', '2001::d1:0']

        result = preparation_predict(input_ips, 'Valid IPv6')

        assert Validate().validateIPAddress(input_ips) == result
