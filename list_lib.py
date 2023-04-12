def product(numbers):
    result = 1

    for number in numbers:
        result *= number

    if any(isinstance(number, float) for number in numbers):
        return float(result)
    else:
        return int(result)
