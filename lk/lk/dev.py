import time
from hashlib import md5 as hashlib_md5
import re


def __md5(_str):
    return hashlib_md5(_str.encode()).hexdigest()


def generate_order_idp(login, sum):
    _time = str(int(time.time()))
    return __md5(''.join([login, sum, _time]))

# print(type(generate_order_idp('9035021172', '10')))


s = 'logout'
print(re.match(r'^.*logout/.*$', s))
