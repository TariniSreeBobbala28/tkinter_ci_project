def convert_logic(val, mode):
    if mode == "Celsius to Fahrenheit":
        return (val * 9/5) + 32
    elif mode == "Fahrenheit to Celsius":
        return (val - 32) * 5/9
    elif mode == "Km to Miles":
        return val * 0.621371
    elif mode == "Miles to Km":
        return val / 0.621371
    elif mode == "Kg to Pounds":
        return val * 2.20462
    elif mode == "Pounds to Kg":
        return val / 2.20462
    return None