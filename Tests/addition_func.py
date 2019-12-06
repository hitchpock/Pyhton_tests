"""
Модуль дополнительных функций, успользуемый в тестах.
"""


def generate_novalid_ip(ip, separator, symbol='-'):
    """
    Функция генерации невалидных ip адресов по заданному.
    Функция вставляет symbol перед каждой частью ip адреса, разделенной separator.
    Пример: '10.20.30.40' -> ['-10.20.30.40', '10.-20.30.40', ...]
    
    :param ip: ip адрес
    :type ip: str
    :param separator: разделитель
    :type separator: str
    :param symbol: символ, добавляющийся в каждую часть ip, defaults to '-'
    :type symbol: str, optional
    :return: Список невалидных ip адресов
    :rtype: list
    """
    ip_list = []
    part_list = ip.split(separator)

    for i in part_list:
        novalid_ip = separator.join(part.replace(part[0], symbol) if part == i else part for part in part_list)
        ip_list.append(novalid_ip)
    
    return ip_list


def preparation_predict(input_lst, predict):
    """
    функция преобразования входного массива к ожидаемому результату.
    
    :param input_lst: массив ip адресов, [ip1, ip2, ...]
    :type input_lst: list
    :param predict: ожидаемый результат.
    :type predict: str
    :return: двумерный массив вида [[ip1, predict], [ip2, predict], ...]
    :rtype: list(list)
    """
    result = [[x] for x in input_lst]
    list(map(lambda x: x.append(predict), result))
    return result
