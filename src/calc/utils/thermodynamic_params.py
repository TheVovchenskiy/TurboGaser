"""Модуль со всеми необходимыми функциями расчета термодинамических
параметров воздуха и продуктов сгорания"""
from numpy.polynomial.polynomial import Polynomial
from scipy import integrate


import src.calc.utils.fuel_params as fp


def C_pi(T: float | int, fuel: str | None = None) -> float:
    """Функция расчета истинной массовой теплоемкости воздуха и продуктов
    сгорания при коэффициенте полноты сгорания топлива (alpha) = 1.
    Если `fuel == None`, то считается для чистого воздуха."""
    if fuel is None:
        fuel = fp.AIR
    _T = T / 1000
    return Polynomial(fp.c_pi_coef[fuel])(_T)


def C_pm(T1: float | int, T2: float | int, fuel: str | None = None) -> float:
    """Функция расчета средней массовой теплоемкости воздуха и продуктов
    сгорания при коэффициенте полноты сгорания топлива (alpha) = 1 между
    температурами `T1` и `T2`. Если `fuel == None`, то считается для
    чистого воздуха. Если `T1 == T2`, то считается истинная массовая
    теплоемкость при этой температуре."""
    if T1 != T2:
        res, _ = integrate.quad(C_pi, T1, T2, (fuel,))
        return res
    return C_pi(T1, fuel)


def C_pg(T1: float | int, T2: float | int, alpha: float, fuel: str) -> float:
    """Функция расчета средней теплоемкости продуктов сгорания между
    температурами `T1` и `T2` при `alpha != 0`."""
    C_pv = C_pm(T1, T2)
    C_pg1 = C_pm(T1, T2, fuel)
    l_0 = fp.l_0[fuel]
    return C_pv + (1 + l_0) / (1 + alpha * l_0) * (C_pg1 - C_pv)


def R_g(alpha: float, fuel: str) -> float:
    """Функция расчета газовой постоянной продуктов сгорания."""
    return fp.R_g_coef[0] + fp.R_g_coef[1] / alpha


def k(C_p: float, R: float) -> float:
    """Функция расчета показателя адиабаты по теплоемкости и газовой
    постоянной."""
    return C_p / (C_p - R)


def alpha_sm(g_t_1: float, delta_g: float, g: float, fuel: str) -> float:
    """Функция определяющая коэффициент избытка воздуха продуктов сгорания
    после подмешивания охлаждающего воздуха.

    - `g_t_1` - относительный расход топлива до подмешивания
    - `delta_g` - относительный расход подмешивающегося воздуха, отнесенный
    к расходу на входе в установку
    - `g` - относительный расход чистого до подмешивания, отнесенный
    к расходу на входе в установку
    - `fuel` - тип топлива."""
    return (1 + delta_g / g) / (g_t_1 * fp.l_0[fuel])
