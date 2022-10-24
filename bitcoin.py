import os
import sys


try:
    import requests
except:
    os.system("pip install requests")


def main():
    n = bcoins()
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except :
        sys.exit("Error getting current price")
    else:
        price = response.json()["bpi"]["USD"]["rate"]
        price = float(price.replace(",", ""))
        print(f"Value of {n} bitcoins = ${n*price}")


def bcoins():
    try:
        return float(sys.argv[1])
    except:
        return float(1)

if __name__=="__main__":
    main()
    input("\n Press any key to exit...")
