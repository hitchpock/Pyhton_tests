from pprint import pprint
from Tests.addition_func import generate_novalid_ip

input_ips = ['2001:DB8:3C4D:777:0260:EFF:FE15:9501',
               '2001:0db8:a3:09d7:1f34:e:07a0:765d']

result = [[x] for x in input_ips]
pprint(result)
list(map(lambda x: x.append('Valid IPv6'), result))

pprint(result)

#assert Validate().validateIPAddress(input_ips) == result