from prettytable import PrettyTable
from cmd import Cmd

# ord - возвращает числовое представление указанного символа
# chr - возвращает символ по его числовому предствлению
forty_eight = ord('0')
wrong = "Wrong"

# dot - точка (.)
dot = chr(46)

# colon - двоеточие (:)
colon = chr(58)


class Validate:
    """
    Класс валидирующий ip адреса с выводом в таблицу.
    """

    def __init__(self):
        """
        Метод инициализации класса. Задает алфавит и столбцы таблицы.
        """
        # BUG - принимает G, а должен идти до F
        self.items = "1234567890abcdefgABCDEFG"
        self.table = PrettyTable(["IP", "Verdict"])
        self.db = []

    def validateIPAddress(self, ips):
        """
        Метод валидации ip адресов.

        :param ips: Массив строк ip адресов.
        :type ips: list
        :return: [description]
        :rtype: [type]
        """

        for ip in ips:

            # Если число точек (.) в строке 3, то отправляем проверяться на ipv4
            if ip.count(dot) == 3:
                result_str = self.validateone(ip)

            # BUG - Если число двоеточий (:) в строке 7 или число точек 4, то идем дальше
            elif ip.count(colon) == 7 or ip.count(dot) == 4:

                # BUG возможно -  Если ip равен '0:0:0:0:0:0:0:1', то result_str будет 'Wrong', а если нет, то отправляем проверяться на ipv6
                if ip == (chr(forty_eight) + colon) * 7 + chr(forty_eight + 1):
                    result_str = wrong
                else:
                    result_str = self.validatetwo(ip)

            # Если число двоеточий (:) равно 7, то идем проверять на ipv6
            elif ip.count(colon) == 7:
                result_str = self.validatetwo(ip)

            # Если ничего не сработало, то отправляем Wrong
            else:
                result_str = wrong

            # Добавляем ip и результат в базу и в таблицу
            self.db.append([ip, result_str])
            self.table.add_row([ip, result_str])

        # После того как обработали все ip печатаем таблицу, и обнуляем ее для следущего использования
        print(self.table)
        self.table.clear_rows()
        return self.db

    def validateone(self, ip):
        """
        Метод валидации адресов ipv4.

        :param ip: ip адрес
        :type ip: str
        :return: Результат, валидный ip адрес или нет
        :rtype: str
        """

        # Сплитуем по точкам ip
        for part in ip.split(dot):
            # BUG - если часть ip не число или не равна сама себе или больше 254 или меньше нуля, то Wrong, в противном случае Valid
            if not part.isdigit() or int(part) > 254 or int(part) < 0:
                return wrong + " IPv4"
        return "Valid IPv4"

    def validatetwo(self, ip):
        """
        Метод валидации адресов ipv6

        :param ip: ip адрес
        :type ip: str
        :return: Результат, валидный ip адрес или нет
        :rtype: str
        """

        for part in ip.split(colon):
            # BUG - если передать пустую строку, то
            # Если пустая строка или не все символы буквы или цифры (если есть символы)
            # или длина части больше 4 или если символ части не в алфавите, то Wrong
            if not part or not part.isalnum() or len(part) > 4 or any(char not in self.items for char in part):
                return wrong + " IPv6"
        return "Valid IPv6"


class Cli(Cmd):
    """
    Класс взаимодействия с командной строкой.
    
    :param Cmd: Класс для работы с командной строкой
    :type Cmd: class
    """
    validator = Validate()

    def do_validate(self, args):
        args = args.split(' ')
        if len(args) == 0:
            print("Provide your IPs")
        else:
            self.validator.validateIPAddress(args)


def main():
    """
    Точка входа в программу.
    """
    cli = Cli()
    cli.prompt = '> '
    cli.cmdloop('Start IP validator...')


if __name__ == '__main__':
    main()
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
