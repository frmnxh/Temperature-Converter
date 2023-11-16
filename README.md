# Temperature Conversion Code

This Python code provides functions for converting temperatures between Celsius, Kelvin, and Fahrenheit. It also includes example usages with manual input.

## Usage

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/temperature-conversion.git
    cd temperature-conversion
    ```

2. **Run the Code**

    Execute the script using a Python interpreter:

    ```bash
    python temperature_conversion.py
    ```

3. **Follow the Prompts**

    The script will prompt you to enter temperatures in Celsius, Kelvin, or Fahrenheit, and it will display the converted temperatures.

4. **Example Usage**

    ```python
    celsius_temp = float(input("Enter temperature in Celsius: "))
    kelvin_temp = celsius_to_kelvin(celsius_temp)
    print(f"{celsius_temp} Celsius is equal to {kelvin_temp} Kelvin.")
    
    # ... (repeat for other temperature conversions)
    ```

## Functions

### `celsius_to_kelvin(celsius: float) -> float`

Converts temperature from Celsius to Kelvin.

### `kelvin_to_celsius(kelvin: float) -> float`

Converts temperature from Kelvin to Celsius.

### `celsius_to_fahrenheit(celsius: float) -> float`

Converts temperature from Celsius to Fahrenheit.

### `fahrenheit_to_celsius(fahrenheit: float) -> float`

Converts temperature from Fahrenheit to Celsius.

### `kelvin_to_fahrenheit(kelvin: float) -> float`

Converts temperature from Kelvin to Fahrenheit.

### `fahrenheit_to_kelvin(fahrenheit: float) -> float`

Converts temperature from Fahrenheit to Kelvin.

## Contributions

Contributions are welcome! If you find any issues or have improvements to suggest, please open an issue or create a pull request.

## License

---

---

Feel free to customize the README based on your preferences and the specifics of your project.
