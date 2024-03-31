#Vincent Moses
from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "9b99631642666327eb57"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    try:
        response = get(url)
        response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful
        data = response.json().get('results', {})
    except Exception.RequestException as e:
        print(f"An error occurred: {e}")
        return []
    
    data = list(data.items())
    data.sort()
   
    return data   

def print_currencies(currencies):
    for name, currency in currencies:
        name =currency['currencyName']
        _id =currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()
    
    if len(data) == 0:
        print('Invalid currencies.')
        return
    
    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")
    
    return rate
    
        
def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    
    try:
        amount = float(amount)
    except:
        print("Invalid amoount.")
        return
    
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {currency2} = {converted_amount} {currency2} ")
    return converted_amount

def main():
    currencies = get_currencies()
    
    print("Welcome to the currency converter!")
    print("List - lists the diffrent currencies ")
    print("Convert - convert from one currency to another")
    print("Rate- Get the exchage rate of two currencies")
    print()
    
    while True:
        command = input("Enter a command (q to quit): ").lower()
        
        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
            print()
            print("List - lists the diffrent currencies ")
            print("Convert - convert from one currency to another")
            print("Rate- Get the exchage rate of two currencies")
            print()
        elif command == "convert":
            currency1 = input("Enter a base currency id: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
            print()
            print("List - lists the diffrent currencies ")
            print("Convert - convert from one currency to another")
            print("Rate- Get the exchage rate of two currencies")
            print()
        elif command  == "rate":
             currency1 = input("Enter a currency id: ").upper()
             currency2 = input("Enter a currency to convert to: ").upper()
             exchange_rate(currency1, currency2)
             print()
             print("List - lists the diffrent currencies ")
             print("Convert - convert from one currency to another")
             print("Rate- Get the exchage rate of two currencies")
             print()
        else:
            print("Unrecognized command!")
            
main()