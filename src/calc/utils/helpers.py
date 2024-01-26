from src.calc.utils import constants


def celcius2kelvin(deg_clcs: float | int) -> float:
    """Given the temperature in Celcius returns temperature value in Kelvins"""
    return deg_clcs - constants.abs_zero_temp


def kelvin2celcius(deg_klvn: float | int) -> float:
    """Given the temperature in Kelvins returns temperature value in Celcius"""
    return deg_klvn + constants.abs_zero_temp
