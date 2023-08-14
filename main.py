import requests

def get_exchange_rates(base_currency, app_id):
    url = f"https://openexchangerates.org/api/latest.json?base={base_currency}&app_id={app_id}"
    response = requests.get(url)
    data = response.json()
    return data["rates"]


def currency_converter(amount, from_currency, to_currency, exchange_rates):
    if from_currency == to_currency:
        return amount
    
    if from_currency in exchange_rates and to_currency in exchange_rates:
        converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
        return converted_amount
    else:
        return None
    
def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        converted_value = (value * 9/5) + 32
        return converted_value
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        converted_value = (value - 32) * 5/9
        return converted_value
    else:
        return None

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meter": 1,
        "foot": 3.28084,
        "inch": 39.3701,
        "centimeter": 100
    }
    
    if from_unit in conversion_factors and to_unit in conversion_factors:
        converted_value = value * conversion_factors[to_unit] / conversion_factors[from_unit]
        return converted_value
    else:
        return None

def main():
    base_currency = "USD"
    app_id = "YOUR_APP_ID_HERE"  # Replace with your API access key
    exchange_rates = get_exchange_rates(base_currency, app_id)
    
    print("Unit Conversion Calculator")
    print("Available options:")
    print("1. Currency Conversion")
    print("2. Temperature Conversion")
    print("3. Length Conversion")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the source currency: ")
        to_currency = input("Enter the target currency: ")
        converted_amount = currency_converter(amount, from_currency, to_currency, exchange_rates)
        if converted_amount is not None:
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        else:
            print("Invalid currency units.")
    # Rest of the code remains the same

if __name__ == "__main__":
    main()