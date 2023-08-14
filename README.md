# Unit Conversion Tool with Exchange Rates API

This program is a versatile unit conversion tool that enables conversion between various unit types, including currencies, temperatures, and lengths. It leverages the "exchangeratesapi.io" API to fetch up-to-date currency exchange rates.

## Features

The program offers the following unit conversion capabilities:

1. Currency Conversion: Converts monetary values from one currency to another using real-time exchange rates.
2. Temperature Conversion: Transforms values between Celsius and Fahrenheit units.
3. Length Conversion: Converts values among meter, foot, inch, and centimeter units.

## Usage

1. Ensure you have the `requests` module installed by running `pip install requests`.

2. Run the program and follow the prompts in the menu to select the desired conversion.

## How It Works

1. The program starts by setting the base currency for conversions and fetching the latest exchange rates from the "exchangeratesapi.io" API.

2. Users can choose among the available conversion options: currency, temperature, or length.

3. For currency conversion, users provide the value, source currency, and target currency. The program retrieves exchange rates to calculate the converted value.

4. For temperature conversion, users input the value and select the source and target temperature units. The program applies the appropriate conversion formulas.

5. For length conversion, users provide the value and select source and target length units. The program utilizes predefined conversion factors for accurate results.

6. The program displays the conversion outcome or an error message if invalid units are provided.

## Notes

- The exchange rates used for currency conversions are sourced from the "exchangeratesapi.io" API. Please be aware that these rates are fictional and do not reflect real-world exchange rates.

- Ensure that you input valid selections based on the available options.

- The code can be extended to include additional unit conversion types or enhance error handling.

