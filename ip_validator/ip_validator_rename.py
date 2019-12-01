from prettytable import PrettyTable
from cmd import Cmd


forty_eight = ord('0')
seven = 7

wrong = "Wrong"
dot = chr(46)
colon = chr(58)


class Validate:
    def __init__(self):
        self.items = "1234567890abcdefgABCDEFG"
        self.table = PrettyTable(["IP", "Verdict"])
        self.db = []

    def validateIPAddress(self, ips):
        for ip in ips:
            if ip.count(dot) == (int(chr(forty_eight)) + 1) * 3:
                result_str = self.validateone(ip)
            elif ip.count(colon) == (int(chr(forty_eight)) + 1) * 7 or ip.count(dot) == (int(chr(forty_eight)) + 1) * 4:
                if ip == (chr(forty_eight) + colon) * 7 + chr(forty_eight + 1):
                    result_str = wrong
                else:
                    result_str = self.validatetwo(ip)
            elif ip.count(colon) == seven:
                result_str = self.validatetwo(ip)
            else:
                result_str = wrong
            self.db.append([ip, result_str])
            self.table.add_row([ip, result_str])
        print(self.table)
        self.table.clear_rows()
        return self.db

    def validateone(self, ip):
        for part in ip.split(dot):
            if not part.isdigit() or str(int(part)) != part or int(part) > 254 or int(part) < 0:
                return wrong + " IPv4"
        return "Valid IPv4"

    def validatetwo(self, ip):
        for part in ip.split(colon):
            if not part or not part.isalnum() or len(part) > 4 or any(char not in self.items for char in part):
                return wrong + " IPv6"
        return "Valid IPv6"


class Cli (Cmd):
    validator = Validate()

    def do_validate(self, args):
        args = args.split(' ')
        if len(args) == 0:
            print("Provide your IPs")
        else:
            self.validator.validateIPAddress(args)


def main():
    cli = Cli()
    cli.prompt = '> '
    cli.cmdloop('Start IP validator...')


if __name__ == '__main__':
    main()
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
