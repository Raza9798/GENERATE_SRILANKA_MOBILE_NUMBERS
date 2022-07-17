import requests
from random import randint
import random

def concat(default, num):
    num = str(num)
    providerCode = ['5', '7', '6', '1',]
    default = str("07" + random.choice(providerCode))
    return default+num

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def generate(inputCount):
    rowCount = 0;

    # while(True):
    while(rowCount < int(inputCount)):
        rowCount += 1;
        randomNum = random_with_N_digits(7)
        print (rowCount,"#", concat(0, randomNum))
    
    print("--------------------------------------------------")
    print("SUCESSFULLY GENERATED "+str(inputCount)+ " NUMBERS")

def main():
    try:
        inputCount = int(input('HOW MANY NUMBER YOU NEED TO GENERATE ? '))
        valid = True 
        print("GENERATING ",inputCount , " NUMBERS")
        print('-------------------------------------')
        generate(inputCount)
    except ValueError:
        print('INVALIDA AMOUNT ENTERED, TRY AGAIN')
        print('-------------------------------------')
        main()

    

if __name__ == "__main__":
    main()
