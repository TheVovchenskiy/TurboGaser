from decimal import Decimal, ROUND_HALF_UP


def format_significant(value: int | float, significant_digits: int = 4) -> str:
    """Outputs given value in str with given `significant_digits` in it.
    Raisees `ValueError` if `significant_digits` <= 0"""
    if significant_digits <= 0:
        raise ValueError(
            "value of 'significant_digits' must be greater than 0"
        )
    if value == 0:
        return '0.' + '0' * (significant_digits - 1)

    d = Decimal(str(value)).normalize()
    _, digits, exponent = d.as_tuple()

    if len(digits) + exponent >= significant_digits:
        digits_to_keep = len(digits) + exponent
    elif 0 < len(digits) + exponent < significant_digits:
        digits_to_keep = significant_digits
    elif -significant_digits + 1 < len(digits) + exponent <= 0:
        digits_to_keep = len(digits) + exponent + significant_digits - 1
    else:
        digits_to_keep = 1

    rounded = d.quantize(
        Decimal(10) ** (len(digits) + exponent - digits_to_keep),
        rounding=ROUND_HALF_UP,
    )

    return str(rounded)


if __name__ == '__main__':
    print(format_significant(2.354654))       # 2.355
    print(format_significant(2.35))       # 2.355
    print(format_significant(2484.276854))    # 2484
    print(format_significant(12354312.7545))  # 12350000
    print(format_significant(0.000000023132))  # 0.00000002313

    print(format_significant(0.000001))
